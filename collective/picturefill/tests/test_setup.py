import unittest2 as unittest
from collective.picturefill.tests import base
from plone.browserlayer import utils
from Products.CMFCore.utils import getToolByName


class TestSetup(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_browserlayer(self):
        layers = [layer.__identifier__ for layer in utils.registered_layers()]
        self.assertIn('collective.picturefill.layer.Layer', layers)

    def test_javascript(self):
        jsregistry = getToolByName(self.portal, 'portal_javascripts')
        picturefill = jsregistry.getResource('++resource++picturefill.min.js')
        self.assertIsNotNone(picturefill)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
