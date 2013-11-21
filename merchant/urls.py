from django.conf.urls import patterns, url
from merchant import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^catalog/category/(?P<id>\d+)/$', views.product_list, name='product_list'),
        url(r'^catalog/(?P<path>.+)/', views.catalog, name='catalog'),
        url(r'^test/$', views.test, name='test'),
)

       