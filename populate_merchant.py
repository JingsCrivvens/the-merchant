
import os
import sys

def populate():

    new=add_menuItem("New","linkToCategories")
    secondhand=add_menuItem("Second Hand","linkToCategories")
    antiques=add_menuItem("Antiques","linkToCategories")
    farmShop=add_menuItem("Farm Shop","linkToCategories")
    blindCraft=add_menuItem("Blindcraft","linkToCategories")
    Valuations=add_menuItem("Valuations","Page")
    furniture=add_Cat("Furniture",True,False)
    pictures=add_Cat("Pictures",True,False)
    lighting=add_Cat("Lighting",True,False)
    bedroom=add_Cat("Bedroom",True,False)
    tables=add_Cat("Tables",False,True)
    chairs=add_Cat("Chairs",False,True)
    beds=add_Cat("Beds",False,True)
    wardrobes=add_Cat("Wardrobes",False,True)
    portraits=add_Cat("portraits",False,True)
    landscapes=add_Cat("Landscapes",False,True)
    tableLamps=add_Cat("Table Lamps",False,True)
    chandeliers=add_Cat("Chandeliers",False,True)
    prod=add_product(new,furniture,chairs,"leather Chair",20)
    prod=add_product(new,furniture,chairs,"Reclining chair",30)
    prod=add_product(new,furniture,tables,"Mahogany table",20)
    prod=add_product(secondhand,furniture,tables,"Mahogany table",40)
    prod=add_product(secondhand,furniture,tables,"Pine table",50)
    prod=add_product(secondhand,furniture,tables,"Dining table",40)
    prod=add_product(new,pictures,landscapes,"Ben Wyvis",20)
    prod=add_product(new,pictures,landscapes,"Ben Nevis",20)
    prod=add_product(new,pictures,portraits,"Mr Bean",20)
    prod=add_product(new,lighting,tableLamps,"Bedside light",30)
    prod=add_product(new,lighting,tableLamps,"Fluorescent light",20)
    prod=add_product(new,lighting,chandeliers,"20 piece chandelier",45)

    
    # Print out what we have added to the user.
    for c in Category.objects.all():
        # print "- {0}".format(str(c))
        print c.name
        for p in Product.objects.filter(category=c):
            print p.name

def add_menuItem(name,renderAs ):
    m = MenuItem()
    m.name=name
    m.renderAs=renderAs
    m.save()    
    return m
def add_product(menuItem,category,subCategory,name, price):
    p = Product()
    p.name=name
    p.menuItem=menuItem
    p.category=category
    p.subCategory=subCategory
    p.price=price
    p.save()    
    return p

def add_Cat(name,atTop,atBottom):
    c=Category()
    c.name=name
    c.atTop=atTop
    c.atBottom=atBottom
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting merchant population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inverness_merchants_project.settings')
    from merchant.models import Category, Product, MenuItem
    populate()
