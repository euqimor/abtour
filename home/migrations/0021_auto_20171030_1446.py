# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 11:46
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20171030_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_page',
            name='bottom_section_text',
        ),
        migrations.AlterField(
            model_name='contact_page',
            name='text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=2000, verbose_name='Основной текст'),
        ),
    ]
