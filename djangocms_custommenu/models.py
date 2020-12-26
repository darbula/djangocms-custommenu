# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin


# Add additional choices through the ``settings.py``.
def get_custommenu_templates():
    return [
        ('default', _('Default')),
    ] + getattr(
        settings,
        'DJANGOCMS_CUSTOMMENU_TEMPLATES',
        [],
    )


@python_2_unicode_compatible
class CustomMenu(CMSPlugin):
    menu_type = models.CharField(
        verbose_name=_('Menu type'),
        max_length=255,
        choices=(
            ("show_menu", _("Show menu")),
            ("show_menu_below_id", _("Show menu below page")),
            ("show_sub_menu", _("Show sub menu")),
        ),
        default="show_menu",
        help_text=_(
            "Check documentation here http://docs.django-cms.org/en/"
            "release-3.4.x/reference/navigation.html"),
    )
    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_custommenu_templates(),
        default=get_custommenu_templates()[0][0],
        max_length=255,
    )

    # for show_menu and show_menu_below_id
    root_page = models.ForeignKey(
        "cms.Page",
        verbose_name=_("Root page"),
        blank=True,
        null=True,
        help_text=_("Menu tree starts from this page. "
                    "Warning: selected page MUST have its ID set in "
                    "advanced settings."),
	on_delete=models.SET_NULL)
    start_level = models.PositiveSmallIntegerField(
        _("Start level"),
        default=0,
        help_text=_("From which level the navigation should be rendered.")
    )
    end_level = models.PositiveSmallIntegerField(
        _("End level"),
        default=100,
        help_text=_("At which level the navigation tree should stop.")
    )
    extra_inactive = models.PositiveSmallIntegerField(
        _("Extra inactive"),
        default=0,
        help_text=_("How many levels of navigation should be displayed if a "
                    "node is not a direct ancestor or descendant of the "
                    "current active node.")
    )
    extra_active = models.PositiveSmallIntegerField(
        _("Extra active"),
        default=100,
        help_text=_("How many levels of descendants of the currently active "
                    "node should be displayed.")
    )

    # for show_sub_menu
    levels = models.PositiveSmallIntegerField(
        _("Levels"),
        default=100,
        help_text=_("At which level the navigation tree should stop.")
    )
    root_level = models.PositiveSmallIntegerField(
        _("Root level"),
        blank=True,
        null=True,
        help_text=_("At what level, if any, the menu should have its root.")
    )
    nephews = models.PositiveSmallIntegerField(
        _("Nephews"),
        default=100,
        help_text=_("How many levels of nephews (children of siblings) "
                    "are shown.")
    )

    classes = models.CharField(
        blank=True,
        help_text=_("Comma separated list of classes to add to the element."),
        max_length=255,
    )
    configuration = models.TextField(
        blank=True,
        help_text=_('Custom configuration.'),
    )

    def get_menu_template(self):
        return 'djangocms_custommenu/custommenu/{}.html'\
            .format(self.template)

    def get_classes(self):
        return ' '.join(item.strip() for item in self.classes.split(',') if item.strip())

    # Add an app namespace to related_name to avoid field name clashes
    # with any other plugins that have a field with the same name as the
    # lowercase of the class name of this model.
    # https://github.com/divio/django-cms/issues/5030
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    def __str__(self):
        return "Custom menu %s %s %s" % \
            (str(self.pk), self.template,
             self.root_page.get_menu_title() if self.root_page else "")


# Add additional choices through the ``settings.py``.
def get_automenu_templates():
    return [
        ('default', _('Default')),
    ] + getattr(
        settings,
        'DJANGOCMS_CUSTOMMENU_AUTOMENU_TEMPLATES',
        [],
    )


@python_2_unicode_compatible
class AutoMenu(CMSPlugin):
    selector = models.CharField(
        max_length=255,
        verbose_name=_('Selector'),
        help_text=_("Selector for elements that should become anchors.")
    )
    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_automenu_templates(),
        default=get_automenu_templates()[0][0],
        max_length=255,
    )

    # Add an app namespace to related_name to avoid field name clashes
    # with any other plugins that have a field with the same name as the
    # lowercase of the class name of this model.
    # https://github.com/divio/django-cms/issues/5030
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
    )

    def __str__(self):
        return "Auto Menu %s" % str(self.pk)
