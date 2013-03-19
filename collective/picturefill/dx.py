from plone.namedfile import scaling

_marker = scaling._marker


class ImageScale(scaling.ImageScale):
    def tag(self, height=_marker, width=_marker, alt=_marker,
            css_class=None, title=_marker, **kwargs):
        """ """
        import pdb;pdb.set_trace()
        super(ImageScale, self).tag(height=height, width=width, alt=alt,
            css_class=css_class, title=title, **kwargs)


class ImageScaling(scaling.ImageScaling):
    """ view override to use picturefill"""
    ImageScale = ImageScale
