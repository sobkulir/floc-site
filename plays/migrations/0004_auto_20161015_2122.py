# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-15 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plays', '0003_auto_20161015_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='short_description',
            field=models.CharField(help_text='Použite 170 znakov.', max_length=170, verbose_name='krátky popis'),
        ),
    ]
