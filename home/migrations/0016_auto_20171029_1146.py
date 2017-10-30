# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 08:46
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20171029_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerspage',
            name='offers_title',
        ),
        migrations.AlterField(
            model_name='offerspage',
            name='offers_intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=500, verbose_name='Описание'),
        ),
    ]
