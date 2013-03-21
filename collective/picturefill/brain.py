from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.globalrequest import getRequest

class PictureFill(object):
    def __init__(self, context):
        self.context = context

        self.item_url = self.context.getURL()
        self.fieldname = 'image'
        BASE = self.item_url + '/@@images/' + self.fieldname
        self.alt = self.context.Title
        self.src_small = BASE + '/mini'
        self.src_medium = BASE + '/preview'
        self.src_large = BASE + '/large'
        self.src_extralarge = BASE
        self.media_medium = "(min-width: 400px)"
        self.media_large = "(min-width: 800px)"
        self.media_extralarge = "(min-width: 1000px)"
        self.request = getRequest()  # support viewpagetemplatefile

    def __call__(self):
        return self.index()

    index = ViewPageTemplateFile('picturefill.pt')
