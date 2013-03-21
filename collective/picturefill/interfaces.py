from zope import schema
from zope import interface


class IPictureFill(interface.Interface):
    """the picture fill schema"""

    alt = schema.TextLine(title=u"Alt of the picture")
    src_small = schema.URI(title=u"URL for small")
    src_medium = schema.URI(title=u"URL for medium")
    src_large = schema.URI(title=u"URL for large")
    src_extralarge = schema.URI(title=u"URL for extra large")
    media_medium = schema.ASCIILine(title=u"media for medium",
                                    default="(min-width: 400px)")
    media_large = schema.ASCIILine(title=u"media for large",
                                   default="(min-width: 800px)")
    media_extralarge = schema.ASCIILine(title=u"media for extra large",
                                        default="(min-width: 1000px)")
