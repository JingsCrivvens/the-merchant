from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from merchant.models import Product
from merchant.models import CatalogCategory
from merchant.models import Catalog


def test(request):
    context = RequestContext(request)                 
                
    context_dict = {}
                    
    #return render_to_response('merchant/categories.html', context_dict, context)
    return render_to_response('merchant/index.html', context_dict, context)
    
def index(request):
    catalog = Catalog.objects.get(name='New')
    
    return render_to_response("merchant/base.html",
                          {'request':'Index',
                          'nodes':CatalogCategory.objects.filter(catalog=catalog),
                          'catalog':catalog,
                          'catalogs':Catalog.objects.all()},
                          context_instance=RequestContext(request))
def catalog(request,path):
    context = RequestContext(request)  
    #menu_url = 'Blindcraft|Beds|Double Beds'
    # parse the menu_url string split by '|' ie 'new|furniture|tables'
    c = Catalog.objects.get(slug=path.split('/')[0])
    products = set()
    for cc in CatalogCategory.objects.filter(catalog=c):
        if (cc.catalog.id==c.id):
            for p in getProduct_list(cc):
                products.add(p)
        
    return render_to_response("merchant/product_list.html",
                          {'nodes':CatalogCategory.objects.filter(catalog=c),
                          'catalog':c,
                          'products': products,
                          'catalogs':Catalog.objects.all()},
                          context_instance=RequestContext(request))
                          
def getProduct_list(catalogCategory):
    p=[]
    for child_0 in CatalogCategory.objects.filter(parent=catalogCategory):
        for child_1 in CatalogCategory.objects.filter(parent=child_0):
            for child_2 in CatalogCategory.objects.filter(parent=child_1):
                for child_3 in CatalogCategory.objects.filter(parent=child_2):
                    for prod in Product.objects.all():
                        if (prod.category == child_3):
                            p.append(prod)
                for prod in Product.objects.all():            
                    if (prod.category == child_2):
                        p.append(prod)
            for prod in Product.objects.all():            
                if (prod.category == child_1):
                    p.append(prod) 
        for prod in Product.objects.all():                                
            if (prod.category == child_0):
                p.append(prod)
    #products = []
    #for child in CatalogCategory.objects.filter(parent=catalogCategory):
    #    products = getProduct_list(p,child)
    #    for product in products:
    #        p.append(product)
        
    for product in Product.objects.all():
        if (product.category == catalogCategory):
            p.append(product)
    return p
    
def product_list(request,id):
    context = RequestContext(request)                 
    catCategory =  CatalogCategory.objects.get(id=id)            
    c = catCategory.catalog
    products = []
    products = getProduct_list(catCategory)
    return render_to_response("merchant/product_list.html",
                          {'nodes':CatalogCategory.objects.filter(catalog=c),
                          'catalog': c,
                          'catCategory': catCategory,
                          'catalogs':Catalog.objects.all(),
                          'products':products},
                          context_instance=RequestContext(request))
  
