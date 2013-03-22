import unittest2 as unittest
from collective.picturefill.tests import base
from collective.picturefill import common


class UnitTestCommon(base.UnitTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_getPictures(self):
        base_url = 'http://nohost/plone/myimage/@@images/image/'
        sizes = {'mini': (200, 200), 'thumb': (128, 128), 'large': (768, 768)}
        pictures, noscript = common.getPictures(base_url, sizes=sizes)
        self.assertEqual(len(pictures), 4)
        thumb_url = base_url + 'thumb'
        self.assertEqual(noscript, thumb_url)
        for picture in pictures[:-1]:
            self.assertTrue(picture['src'].startswith(base_url))
            self.assertTrue(picture['media'].startswith('(max-width: '))
            self.assertTrue(picture['media'].endswith('px)'))
            width = picture['media'][12:-3]
            self.assertTrue(width.isdigit())
        #test the last
        picture = pictures[-1]
        self.assertTrue(picture['src'].startswith(base_url[:-1]))
        self.assertTrue(picture['media'].startswith('(min-width: '))
        self.assertTrue(picture['media'].endswith('px)'))
        width = picture['media'][12:-3]
        self.assertTrue(width.isdigit())


class IntegrationTestCommon(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_getPictures(self):
        base_url = 'http://nohost/plone/myimage/@@images/image/'
        pictures, noscript = common.getPictures(base_url)
        self.assertEqual(len(pictures), 8)
        thumb_url = base_url + 'thumb'
        self.assertEqual(noscript, thumb_url)
        for picture in pictures[:-1]:
            self.assertTrue(picture['src'].startswith(base_url))
            self.assertTrue(picture['media'].startswith('(max-width: '))
            self.assertTrue(picture['media'].endswith('px)'))
            width = picture['media'][12:-3]
            self.assertTrue(width.isdigit())
        #test the last
        picture = pictures[-1]
        self.assertTrue(picture['src'].startswith(base_url[:-1]))
        self.assertTrue(picture['media'].startswith('(min-width: '))
        self.assertTrue(picture['media'].endswith('px)'))
        width = picture['media'][12:-3]
        self.assertTrue(width.isdigit())


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)