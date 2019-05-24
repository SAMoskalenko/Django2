from django.urls import path, re_path
import mainapp.views as mainapp

from django.views.decorators.cache import cache_page


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.catalog, name='catalog'),
    # path('category/<pk>/', mainapp.catalog, name='category'),
    re_path(r'^category/(?P<pk>\d+)/$', mainapp.catalog, name='category'),
    re_path(r'^category/(?P<pk>\d+)/ajax/$', cache_page(3600)(mainapp.catalog_ajax)),
    path('product/<pk>/', mainapp.product, name='product'),

    # path('category/<pk>/page/<page>', mainapp.catalog, name='page'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.catalog, name='page'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/ajax/$', cache_page(3600)(mainapp.catalog_ajax)),
]
