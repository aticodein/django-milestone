# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-04 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_auto_20200304_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='product_image',
            field=models.ImageField(default='', upload_to='', verbose_name=products.models.Product),
        ),
    ]
