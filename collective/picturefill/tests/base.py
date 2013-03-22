import unittest2 as unittest
from plone.app import testing
import collective.picturefill
from collective.picturefill.tests.fake import FakeContext, FakeRequest


FIXTURE = testing.PloneWithPackageLayer(
    zcml_filename="configure.zcml",
    zcml_package=collective.picturefill,
    additional_z2_products=[],
    gs_profile_id='collective.picturefill:default',
    name="collective.picturefill:FIXTURE"
)

INTEGRATION = testing.IntegrationTesting(
    bases=(FIXTURE,), name="collective.picturefill:Integration"
)

FUNCTIONAL = testing.FunctionalTesting(
    bases=(FIXTURE,), name="collective.picturefill:Functional"
)


class UnitTestCase(unittest.TestCase):

    def setUp(self):
        self.request = FakeRequest()
        self.context = FakeContext()
        sizes = {'mini': (200, 200), 'thumb': (128, 128), 'large': (768, 768)}
        self.sizes = sizes


class IntegrationTestCase(unittest.TestCase):

    layer = INTEGRATION

    def setUp(self):
        super(IntegrationTestCase, self).setUp()
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Image', 'myimage')
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Member'])
        self.image = self.portal['myimage']
        from plone.app.imaging.utils import getAllowedSizes
        self.sizes = getAllowedSizes()
