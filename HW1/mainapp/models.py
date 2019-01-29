from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    pic = models.ImageField(upload_to='products')
    fullname = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    details = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='категория активна', default=True)

    def __str__(self):
        return self.name


class MainBanners(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=30)
    pic = models.ImageField(upload_to='banners')
    href = models.URLField(max_length=100)

    def __str__(self):
        return self.name
