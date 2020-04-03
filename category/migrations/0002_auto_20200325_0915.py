# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-25 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('Magical', 'Magical'), ('Historical', 'Historical'), ('Voodoo', 'Voodoo'), ('Christian', 'Christian'), ('Ancient', 'Ancient')], default='', max_length=50),
        ),
    ]