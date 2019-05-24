from django.test import TestCase
from mainapp.models import Product, Category


class ProductsTestCase(TestCase):

    def setUp(self):
        category = Category.objects.create(name="аксессуары")
        self.product_1 = Product.objects.create(name='бита', category=category, price=200, quantity=33)
        self.product_2 = Product.objects.create(name='ловушка', category=category, price=250, quantity=3, is_active=False)
        self.product_3 = Product.objects.create(name='защита', category=category, price=300, quantity=4)


    def test_product_get(self):
        product_1 = Product.objects.get(name="бита")
        product_2 = Product.objects.get(name="ловушка")
        self.assertEqual(product_1, self.product_1)
        self.assertEqual(product_2, self.product_2)

    def test_product_print(self):
        product_1 = Product.objects.get(name="бита")
        product_2 = Product.objects.get(name="ловушка")
        self.assertEqual(str(product_1), 'бита')
        self.assertEqual(str(product_2), 'ловушка')


    def test_product_get_items(self):
        product_1 = Product.objects.get(name="бита")
        product_3 = Product.objects.get(name="защита")

        products = product_1.get_items()

        self.assertEqual(list(products), [product_1, product_3])
