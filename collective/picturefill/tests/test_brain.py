import unittest2 as unittest
from collective.picturefill.tests import base
from collective.picturefill import brain
from collective.picturefill.tests.fake import FakeBrain, FakeRequest


class UnitTestBrain(base.UnitTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_picturefill(self):
        ibrain = FakeBrain()
        ibrain.Title = 'a title'
        picturefill = brain.PictureFill(ibrain)
        picturefill.request = FakeRequest()
        picturefill.sizes = self.sizes
        picturefill.update()
        self.assertEqual(picturefill.alt, 'a title')
        self.assertEqual(picturefill.context_url, 'http://nohost.com/myid')
        self.assertEqual(picturefill.fieldname, 'image')
        base_url = 'http://nohost.com/myid/@@images/image/'
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
        ibrain = FakeBrain()
        picturefill = brain.PictureFill(ibrain)
        picturefill.update()

        base_url = 'http://nohost.com/myid/@@images/image/'
        self.assertEqual(picturefill.base_url, base_url)

        def index():
            return "rendered"
        picturefill.index = index
        self.assertEqual(picturefill(), "rendered")


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
