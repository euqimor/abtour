# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 16:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0005_auto_20171027_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logo',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='logo',
            name='page',
        ),
        migrations.AddField(
            model_name='homepage',
            name='logo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Логотип', to='wagtailimages.Image'),
        ),
        migrations.DeleteModel(
            name='Logo',
        ),
    ]
