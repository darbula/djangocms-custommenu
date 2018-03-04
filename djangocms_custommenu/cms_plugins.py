# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from . import models


class CustomMenuPlugin(CMSPluginBase):
    model = models.CustomMenu
    name = _('Custom menu')
    module = _('Custom menu')
    render_template = 'djangocms_custommenu/custommenu/base.html'

    fieldsets = [
        (None, {
            'description': _(
                "Check documentation here http://docs.django-cms.org/en/"
                "release-3.4.x/reference/navigation.html"
            ),
            'fields': (
                'menu_type',
                'template',
                'classes',
                'configuration',
            )
        }),
        ("Show menu options", {
            'classes': ('collapse',),
            'fields': (
                'root_page',
                'start_level',
                'end_level',
                'extra_inactive',
                'extra_active',
            )
        }),
        ("Show sub menu options", {
            'classes': ('collapse',),
            'fields': (
                'levels',
                'root_level',
                'nephews',
            )
        }),
    ]


plugin_pool.register_plugin(CustomMenuPlugin)


class AutoMenuPlugin(CMSPluginBase):
    """ Creates in-page anchor (scroll to) menu using javascript. """
    model = models.AutoMenu
    name = _('Auto Menu')
    module = _('Custom menu')

    fieldsets = [
        (None, {
            'fields': (
                'selector',
                'template',
            )
        }),
    ]

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_custommenu/automenu/{}.html'\
            .format(instance.template)


plugin_pool.register_plugin(AutoMenuPlugin)


class BreadcrumbsPlugin(CMSPluginBase):
    name = _('Breadcrumbs')
    module = _('Custom menu')
    render_template = 'djangocms_custommenu/breadcrumbs/default.html'


plugin_pool.register_plugin(BreadcrumbsPlugin)
