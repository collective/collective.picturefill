from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.globalrequest import getRequest
from collective.picturefill.common import getPictures


class PictureFill(object):
    def __init__(self, context):
        self.context = context

        self.item_url = self.context.getURL()
        self.fieldname = 'image'
        base_url = self.item_url + '/@@images/' + self.fieldname + '/'
        self.alt = self.context.Title
        self.pictures, self.noscript = getPictures(base_url)
        self.request = getRequest()  # support viewpagetemplatefile

    def __call__(self):
        return self.index()

    index = ViewPageTemplateFile('picturefill.pt')
