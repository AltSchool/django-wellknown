================
FORKED: REDUCED TO BAREBONES SERVING MODEL RESOURCES FROM DB TO SIMPLIFY (markine)
================

================
django-wellknown
================

Django application to provide easy administration of site-meta URIs.

Installation
============

Be sure to add ``wellknown`` to ``INSTALLED_APPS`` in settings.py. Additionally, add the following entry to urls.py::

	urls(r'^', include('wellknown.urls')),

Run ``./manage.py syncdb``

Usage
=====

Model resources
---------------

Resources may be stored in the database to make it easy for non-technical users to edit. The following fields are available on a Resource:

* ``path``: the path that maps to the resource
* ``content``: the content that will be served when the resource is requested
* ``content_type``: the content_type with which the content will be returned, defaults to ``text/plain``
