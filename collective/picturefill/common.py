from Products.Five.browser import BrowserView
from plone.app.imaging.utils import getAllowedSizes


def getPictures(base_url, sizes=None):
    """Return a list of pictures.
    A picture: {'src': base_url/thumb, 'media': "(max-width: 300px)"}
    """
    pictures = []
    if sizes is None:
        sizes = getAllowedSizes()
    widths = []
    names = {}
    for name in sizes:
        width, height = sizes[name]
        widths.append(width)
        names[str(width)] = name
    widths.sort()
    noscript = ""
    for width in widths:
        if width > 128 and not noscript:
            noscript = base_url + name
        name = names[str(width)]
        image = {'src': base_url + name, 'media': "(max-width: %spx)" % width}
        pictures.append(image)
    image = {'src': base_url[:-1], 'media': "(min-width: %spx)" % widths[-1]}
    pictures.append(image)

    #try to find a width > 128px for the noscript image
    return pictures, noscript


class PictureFill(BrowserView):
    """Tag renderer for dexterity"""

    def update(self):
        self.context_url = self.context.absolute_url()
        self.fieldname = self.request.get('field', 'image')
        base_url = self.context_url + '/@@images/' + self.fieldname + '/'
        self.alt = self.context.Title()
        self.pictures, self.noscript = getPictures(base_url)

    def __call__(self):
        self.update()
        return self.index()
