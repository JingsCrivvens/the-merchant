from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from tinymce import models as tinymce_models

from datetime import datetime    
      
class Product(models.Model):  
    category = models.ForeignKey('CatalogCategory', related_name='products')  
    name = models.CharField(max_length=300)  
    slug = models.SlugField(max_length=150)  
    description = tinymce_models.HTMLField() #models.TextField()  
    photo = models.ImageField(upload_to='product_photo',  blank=True)  
    manufacturer = models.CharField(max_length=300,  blank=True)  
    price_in_dollars = models.DecimalField(max_digits=6,decimal_places=2)
    
    def path(self):
        return self.category.path()
        
    def __unicode__(self):        
        return self.name     
        
class Catalog(models.Model):  
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)  
    publisher = models.CharField(max_length=300)  
    description = models.TextField()  
    pub_date = models.DateTimeField(default=datetime.now)
    def __unicode__(self):        
        return self.name

def getCatalogCategoryName(catCat):
    name = ''
    if (catCat.parent):
        name = getCatalogCategoryName(catCat.parent) + ' > ' + catCat.name
    else:
        name = catCat.name
    return  name   

class CatalogCategory(MPTTModel):  
    catalog = models.ForeignKey('Catalog', blank=True, null=True, related_name='categories')  
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')  
    name = models.CharField(max_length=300)  
    slug = models.SlugField(max_length=150)  
    description = models.TextField(blank=True)
    
    class MPTTMeta:
        order_insertion_by = ['name']
    
    def path(self):
        if (self.catalog):
            return u'%s: %s' % (self.catalog.name, getCatalogCategoryName(self))
        else:
            return getCatalogCategoryName(self)
            
    def __unicode__(self):
        return u'%s: %s' % (self.catalog.name, getCatalogCategoryName(self))      



