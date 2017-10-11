from __future__ import absolute_import, unicode_literals

from django.db import models
from django.shortcuts import render
from django.http import HttpResponseRedirect

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
                                                PageChooserPanel, InlinePanel, \
                                                StreamFieldPanel
from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel



class HomePage(Page):
    logo = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='Логотип')
    carousel_title = models.TextField('Слоган', max_length=40, blank=True)
    intro_header = models.TextField('Заголовок', max_length=40, blank=True)
    intro_body = RichTextField('Основной текст', blank=True)
    intro_hashtags = models.TextField('Хэштэги', max_length=40, blank=True)
    column1_header = models.CharField('Заголовок', max_length=40, blank=True)
    column1_body = RichTextField('Текст', max_length=500, blank=True)
    column2_header = models.CharField('Заголовок', max_length=40, blank=True)
    column2_body = RichTextField('Текст', max_length=500, blank=True)
    column3_header = models.CharField('Заголовок', max_length=40, blank=True)
    column3_body = RichTextField('Текст', max_length=500, blank=True)
    form_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True)
    form_header = models.CharField('Заголовок', max_length=40, blank=True)
    form_intro = RichTextField('Текст', max_length=500, blank=True)
    small_columns_title = models.CharField('Общий заголовок', max_length=40, blank=True)
    small_columns_intro = RichTextField('Общий текст', max_length=500, blank=True)
    small_column1_header = models.CharField('Заголовок 1', max_length=40, blank=True)
    small_column1_body = RichTextField('Текст 1', max_length=500, blank=True)
    small_column2_header = models.CharField('Заголовок 2', max_length=40, blank=True)
    small_column2_body = RichTextField('Текст 2', max_length=500, blank=True)
    small_column3_header = models.CharField('Заголовок 3', max_length=40, blank=True)
    small_column3_body = RichTextField('Текст 3', max_length=500, blank=True)
    small_column4_header = models.CharField('Заголовок 4', max_length=40, blank=True)
    small_column4_body = RichTextField('Текст 4', max_length=500, blank=True)


    content_panels = Page.content_panels + [
        ImageChooserPanel('logo'),
        FormSubmissionsPanel(),
        FieldPanel('carousel_title', classname='text-center'),
        MultiFieldPanel([
            FieldPanel('intro_header', classname='text-center'),
            FieldPanel('intro_body'),
            FieldPanel('intro_hashtags'),
        ], heading='Раздел приветствия'),
        MultiFieldPanel([
            FieldPanel('column1_header', classname='text-center'),
            FieldPanel('column1_body'),
        ], heading='Верхняя колонка 1 (Самолёт)'),
        MultiFieldPanel([
            FieldPanel('column2_header', classname='text-center'),
            FieldPanel('column2_body'),
        ], heading='Верхняя колонка 2 (Сердце)'),
        MultiFieldPanel([
            FieldPanel('column3_header', classname='text-center'),
            FieldPanel('column3_body'),
        ], heading='Верхняя колонка 3 (Валюта)'),
        MultiFieldPanel([
            FieldPanel('form_header', classname='text-center'),
            FieldPanel('form_intro'),
            ImageChooserPanel('form_image'),
        ], heading='Форма заявки'),
        MultiFieldPanel([
            FieldPanel('small_columns_title', classname='text-center'),
            FieldPanel('small_columns_intro'),
        ], heading='Нижняя секция'),
        MultiFieldPanel([
            FieldPanel('small_column1_header', classname='text-center'),
            FieldPanel('small_column1_body'),
        ], heading='Колонка 1 (Карта)'),
        MultiFieldPanel([
            FieldPanel('small_column2_header', classname='text-center'),
            FieldPanel('small_column2_body'),
        ], heading='Колонка 2 (Телефон)'),
        MultiFieldPanel([
            FieldPanel('small_column3_header', classname='text-center'),
            FieldPanel('small_column3_body'),
        ], heading='Колонка 3 (Почта)'),
        MultiFieldPanel([
            FieldPanel('small_column4_header', classname='text-center'),
            FieldPanel('small_column4_body'),
        ], heading='Колонка 4 (Время работы)'),
        InlinePanel('carousel_images', label='Carousel images'),
    ]

    def serve(self, request, *args, **kwargs):
        from home.forms import RequestForm
        from django.contrib import messages

        if request.method == 'POST':
            form = RequestForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            messages.info(request, 'Что-то пошло не так')
            return HttpResponseRedirect('/')

        else:
            form = RequestForm()
            return render(request, 'home/home_page.html', {
                'page': self,
                'form': form,
                })


class CarouselImage(Orderable):
    page = ParentalKey(HomePage, related_name='carousel_images')
    image = models.ForeignKey(
                'wagtailimages.Image',
                null=True,
                blank=True,
                on_delete=models.SET_NULL,
                related_name='+'
            )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class TouristRequest(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    num_adults = models.IntegerField()
    num_kids = models.IntegerField()
    where = models.CharField(max_length=100)
    budget = models.IntegerField()
    currency = models.CharField(max_length=100)
    comment = models.CharField(max_length=10000)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
