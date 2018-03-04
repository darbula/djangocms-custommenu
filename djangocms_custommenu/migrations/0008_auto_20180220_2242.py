# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-20 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_custommenu', '0007_auto_20180220_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stylemenu',
            name='menu_type',
            field=models.CharField(choices=[(b'show_menu', 'Show menu'), (b'show_menu_below_id', 'Show menu below page'), (b'show_sub_menu', 'Show sub menu')], default=b'show_menu', help_text='Check documentation here http://docs.django-cms.org/en/release-3.4.x/reference/navigation.html', max_length=255, verbose_name='Menu type'),
        ),
        migrations.AlterField(
            model_name='stylemenu',
            name='template',
            field=models.CharField(choices=[(b'default', 'Default'), (b'zoom-masonry', 'Zoom masonry'), (b'dropdown-image', 'Dropdown image'), (b'footer-menu-item', 'Footer menu item')], default=b'default', max_length=255, verbose_name='Template'),
        ),
    ]
