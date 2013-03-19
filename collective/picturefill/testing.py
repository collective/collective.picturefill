from plone.app.testing import *
import collective.picturefill


FIXTURE = PloneWithPackageLayer(
    zcml_filename="configure.zcml",
    zcml_package=collective.picturefill,
    additional_z2_products=[],
    gs_profile_id='collective.picturefill:default',
    name="collective.picturefill:FIXTURE"
)

INTEGRATION = IntegrationTesting(
    bases=(FIXTURE,), name="collective.picturefill:Integration"
)

FUNCTIONAL = FunctionalTesting(
    bases=(FIXTURE,), name="collective.picturefill:Functional"
)
