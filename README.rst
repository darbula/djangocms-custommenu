django CMS custommenu
=====================


**django CMS custommenu** is a set of plugins for `django CMS <http://django-cms.org>`_ that allow you to publish menu in the same way as it can be done via `menu template tags <http://docs.django-cms.org/en/latest/reference/navigation.html>`_ hard coded in the template.


Requirements
------------

* Python 2.7, 3.3 or higher
* Django 1.8 or higher


Installation
------------

For a manual install:

* run ``pip install djangocms-custommenu``
* add ``djangocms_custommenu`` to your ``INSTALLED_APPS``
* run ``python manage.py migrate djangocms_custommenu``


Configuration
-------------

You are encouraged to adapt and override provided templates to your project's requirements and optionally provide additional template choices by adding a ``DJANGOCMS_CUSTOMMENU_TEMPLATES`` or ``DJANGOCMS_CUSTOMMENU_AUTOMENU_TEMPLATES`` settings::

    DJANGOCMS_CUSTOMMENU_TEMPLATES = [
        ('feature', _('Featured Version')),
    ]

You'll need to create the appropriate folders and files inside ``templates/djangocms_custommenu/`` otherwise you will get a *template does not exist* error.
