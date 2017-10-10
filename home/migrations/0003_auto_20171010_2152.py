# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 18:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='homepage',
            name='carousel_title',
            field=models.TextField(blank=True, max_length=40, verbose_name='Слоган'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='column1_body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=500, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='column1_header',
            field=models.CharField(blank=True, max_length=40, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='column2_body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=500, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='column2_header',
            field=models.CharField(blank=True, max_length=40, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='column3_body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=500, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='column3_header',
            field=models.CharField(blank=True, max_length=40, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='form_header',
            field=models.CharField(blank=True, max_length=40, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='form_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='form_intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=500, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Основной текст'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_hashtags',
            field=models.TextField(blank=True, max_length=40, verbose_name='Хэштэги'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_header',
            field=models.TextField(blank=True, max_length=40, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='logo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Логотип', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='small_column1_body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=500, verbose_name='Текст 1'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='small_column1_header',
            field=models.CharField(blank=True, max_length=40, verbose_name='Заголовок 1'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='small_column2_body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=500, verbose_name='Текст 2'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='small_column2_header',
            field=models.CharField(blank=True, max_length=40, verbose_name='Заголовок 2'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='small_column3_body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=500, verbose_name='Текст 3'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='small_column3_header',
            field=models.CharField(blank=True, max_length=40, verbose_name='Заголовок 3'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='small_column4_body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=500, verbose_name='Текст 4'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='small_column4_header',
            field=models.CharField(blank=True, max_length=40, verbose_name='Заголовок 4'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='small_columns_intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, max_length=500, verbose_name='Общий текст'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='small_columns_title',
            field=models.CharField(blank=True, max_length=40, verbose_name='Общий заголовок'),
        ),
        migrations.AddField(
            model_name='carouselimage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel_images', to='home.HomePage'),
        ),
    ]
