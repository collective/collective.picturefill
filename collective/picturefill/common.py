from Products.Five.browser import BrowserView
from plone.app.imaging.utils import getAllowedSizes


def getPictures(base_url, sizes):
    """Return a list of pictures.
    A picture: {'src': base_url/thumb, 'media': "(max-width: 300px)"}
    """
    pictures = []
    widths = []
    names = {}
    for name in sizes:
        width = sizes[name][0]
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

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.sizes = []
        self.pictures = []
        self.noscript = ""
        self.fieldname = ""
        self.base_url = ""
        self.alt = ""

    def update(self):
        self.context_url = self.context.absolute_url()
        if not self.fieldname:
            self.fieldname = self.request.get('field', 'image')
        if not self.base_url:
            base_url = self.context_url + '/@@images/' + self.fieldname + '/'
            self.base_url = base_url
        if not self.alt:
            self.alt = self.context.Title()
        if not self.sizes:
            self.sizes = getAllowedSizes()
        if not self.pictures or not self.noscript:
            pictures = getPictures(self.base_url, self.sizes)
            self.pictures, self.noscript = pictures

    def __call__(self):
        self.update()
        return self.index()
