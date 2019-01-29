from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.catalog, name='catalog'),
    path('category/<pk>/', mainapp.catalog, name='category'),
    path('product/<pk>/', mainapp.product, name='product'),

    path('category/<pk>/page/<page>', mainapp.catalog, name='page'),
]