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

    def test_upgrades(self):
        profile = 'collective.picturefill:default'
        setup = self.portal.portal_setup
        upgrades = setup.listUpgrades(profile, show_old=True)
        self.assertTrue(len(upgrades) > 0)
        for upgrade in upgrades:
            upgrade['step'].doStep(setup)


class TestUninstall(base.IntegrationTestCase):
    """Test if the addon uninstall well"""

    def setUp(self):
        super(TestUninstall, self).setUp()
        qi = self.portal['portal_quickinstaller']
        qi.uninstallProducts(products=['collective.picturefill'])

    def test_uninstall_browserlayer(self):
        from collective.picturefill.layer import Layer
        layers = utils.registered_layers()
        self.assertNotIn(Layer, layers)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
