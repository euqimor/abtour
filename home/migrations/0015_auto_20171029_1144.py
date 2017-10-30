# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20171028_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerspage',
            name='offers_intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=500, verbose_name='Общий текст'),
        ),
        migrations.AddField(
            model_name='offerspage',
            name='offers_title',
            field=models.CharField(blank=True, max_length=40, verbose_name='Общий заголовок'),
        ),
    ]
