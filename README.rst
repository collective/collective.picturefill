Introduction
============

This addon install picturefill_ in Plone and provide a suite of tools to
display images from different kind of components such as brain, dexterity object
or archetypes object.

version: https://github.com/scottjehl/picturefill/tree/00936788c29059834bc78b119fc45ebc3bc056eb

How to install
==============

.. image:: https://pypip.in/v/collective.picturefill/badge.png
    :target: https://crate.io/packages/collective.picturefill/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/collective.picturefill/badge.png
    :target: https://crate.io/packages/collective.picturefill/
    :alt: Number of PyPI downloads

.. image:: https://secure.travis-ci.org/collective/collective.picturefill.png
    :target: http://travis-ci.org/#!/collective/collective.picturefill

.. image:: https://coveralls.io/repos/collective/collective.picturefill/badge.png?branch=master
    :alt: Coverage
    :target: https://coveralls.io/r/collective/collective.picturefill


This addon can be installed has any other addons. please follow official
documentation_

How to use
==========

in template::

    tal:content="structure myimage_object/@@polyfill"

in python::

    from collective.picturefill.interfaces import IPictureFill
    IPictureFill(brain)()

CSS: You should use this tricks if you want in your theme that picturefill
fit the exact size of the container::

    div[data-picture] img{
        width: 100%;
    }

Credits
=======

Companies
---------

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact Makina Corpus <mailto:python@makina-corpus.org>`_

People
------

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to
.. _picturefill: https://github.com/scottjehl/picturefill
