from Products.Five.browser import BrowserView
from plone.app.imaging.utils import getAllowedSizes
from collective.picturefill.common import getPictures


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
