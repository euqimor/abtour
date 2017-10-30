# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20171030_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecOfferRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('num_adults', models.IntegerField()),
                ('num_kids', models.IntegerField()),
                ('comment', models.CharField(max_length=10000)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
