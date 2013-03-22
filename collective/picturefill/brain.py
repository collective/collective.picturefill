from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.globalrequest import getRequest
from collective.picturefill.common import getPictures
from plone.app.imaging.utils import getAllowedSizes


class PictureFill(object):
    def __init__(self, context):
        self.context = context

        self.alt = self.context.Title
        self.fieldname = ""
        self.sizes = []
        self.pictures = []
        self.noscript = ""
        self.request = None
        self.context_url = ""
        self.base_url = ""

    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        if not self.request:
            self.request = getRequest()  # support viewpagetemplatefile
        if not self.fieldname:
            self.fieldname = 'image'
        if not self.context_url:
            self.context_url = self.context.getURL()
        if not self.base_url:
            self.base_url = self.context_url + '/@@images/' + self.fieldname + '/'
        if not self.sizes:
            self.sizes = getAllowedSizes()
        if not self.pictures or not self.noscript:
            pictures = getPictures(self.base_url, self.sizes)
            self.pictures, self.noscript = pictures

    index = ViewPageTemplateFile('picturefill.pt')
