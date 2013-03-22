import unittest2 as unittest
from collective.picturefill.tests import base
from collective.picturefill.view import PictureFill


class UnitTestView(base.UnitTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_picturefill_view(self):
        view = PictureFill(self.context, self.request)
        view.sizes = self.sizes
        view.update()
        self.assertEqual(view.alt, 'a title')
        self.assertEqual(view.context_url, 'http://nohost.com/myid')
        self.assertEqual(view.fieldname, 'image')
        base_url = 'http://nohost.com/myid/@@images/image/'
        self.assertEqual(view.base_url, base_url)


class IntegrationTestCommon(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_picturefill_view(self):
        pass
#        view = self.image.restrictedTraverse('@@picturefill')
#        render = view()
#        self.assertEqual(len(view.pictures), 8)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
