import unittest2 as unittest
from collective.picturefill.tests import base
from collective.picturefill import tile
from collective.picturefill.tests.fake import FakeTile, FakeRequest


class UnitTestBrain(base.UnitTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_picturefill(self):
        itile = FakeTile()
        itile.Title = 'a title'
        picturefill = tile.PictureFill(itile)
        picturefill.request = FakeRequest()
        picturefill.sizes = self.sizes
        picturefill.update()
        self.assertEqual(picturefill.alt, 'a title')
        tile_url = 'http://nohost.com/@@mytiletype/mytile'
        self.assertEqual(picturefill.context_url, tile_url)
        self.assertEqual(picturefill.fieldname, 'picture')
        base_url = tile_url + '/@@images/picture/'
        self.assertEqual(picturefill.base_url, base_url)

        def index():
            return "rendered"
        picturefill.index = index
        self.assertEqual(picturefill(), "rendered")


class IntegrationTestCommon(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_picturefill_request(self):
        itile = FakeTile()
        picturefill = tile.PictureFill(itile)
        picturefill.update()

        tile_url = 'http://nohost.com/@@mytiletype/mytile'
        base_url = tile_url + '/@@images/picture/'
        self.assertEqual(picturefill.base_url, base_url)

        def index():
            return "rendered"
        picturefill.index = index
        self.assertEqual(picturefill(), "rendered")


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
