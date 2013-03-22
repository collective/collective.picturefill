from Products.Five.browser import BrowserView
from collective.picturefill.common import getPictures


class PictureFill(BrowserView):
    """Tag renderer for dexterity"""

    def update(self):
        self.context_url = self.context.absolute_url()
        self.fieldname = self.request.get('field', 'image')
        base_url = self.context_url + '/@@images/' + self.fieldname
        self.alt = self.context.Title()
        self.pictures, self.noscript = getPictures(base_url)

    def __call__(self):
        self.update()
        return self.index()
