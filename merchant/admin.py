from django.contrib import admin
from merchant.models import Product , Catalog, CatalogCategory 

from mptt.admin import MPTTModelAdmin
#from merchant.models import Node

#admin.site.register(Node, MPTTModelAdmin)

class CatalogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','path')    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','path')    
         
admin.site.register(Product,ProductAdmin)
admin.site.register(Catalog)
admin.site.register(CatalogCategory,CatalogCategoryAdmin)
