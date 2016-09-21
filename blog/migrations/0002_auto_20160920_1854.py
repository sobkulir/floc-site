# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='posted',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='čas pridania'),
        ),
    ]