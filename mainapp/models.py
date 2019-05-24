from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=30,blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    pic = models.ImageField(upload_to='products')
    fullname = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=500, blank=True)
    details = models.CharField(max_length=500, blank=True)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='категория активна', default=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('category', 'name').select_related()


class MainBanners(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=30)
    pic = models.ImageField(upload_to='banners')
    href = models.URLField(max_length=100)

    def __str__(self):
        return self.name
