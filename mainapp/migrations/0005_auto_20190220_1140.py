# Generated by Django 2.1.5 on 2019-02-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='fullname',
            field=models.CharField(max_length=500),
        ),
    ]
