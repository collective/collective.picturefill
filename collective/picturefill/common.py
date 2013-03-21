from Products.Five.browser import BrowserView

class PictureFill(BrowserView):
    """Tag renderer for dexterity"""

    def update(self):
        self.context_url = self.context.absolute_url()
        self.fieldname = self.request.get('field', 'image')
        BASE = self.context_url + '/@@images/' + self.fieldname
        self.alt = self.context.Title()
        self.src_small = BASE + '/mini'
        self.src_medium = BASE + '/preview'
        self.src_large = BASE + '/large'
        self.src_extralarge = BASE
        self.media_medium = "(min-width: 400px)"
        self.media_large = "(min-width: 800px)"
        self.media_extralarge = "(min-width: 1000px)"

    def __call__(self):
        self.update()
        return self.index()
