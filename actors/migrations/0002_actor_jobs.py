# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='jobs',
            field=models.CharField(default='Herec', help_text='Vymenujte úlohy daného človeka. Napr. Režisér a herec', max_length=255, verbose_name='Úlohy'),
        ),
    ]