# Generated by Django 2.1.7 on 2019-03-19 08:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_auto_20190319_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 21, 8, 42, 47, 48283, tzinfo=utc)),
        ),
    ]