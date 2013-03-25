from ZPublisher.tests.testPublish import Request


class FakeContext(object):

    def __init__(self):
        self.id = "myid"
        self.title = "a title"
        self.description = "a description"
        self.creators = ["myself"]
        self.date = "a date"
        self._modified = "modified date"
        self.remoteUrl = ''  # fake Link

    def getId(self):
        return self.id

    def Title(self):
        return self.title

    def Creators(self):
        return self.creators

    def Description(self):
        return self.description

    def Date(self):
        return self.date

    def modified(self):
        return self._modified

    def getPhysicalPath(self):
        return ('/', 'a', 'not', 'existing', 'path')

    def absolute_url(self):
        return "http://nohost.com/" + self.id


class FakeRequest(Request):

    def __init__(self):
        Request.__init__(self)
        self.args = {}

    def __setitem__(self, name, value):
        self.args[name] = value

    def get(self, a, b=''):
        return self.args.get(a, b)


class FakeBrain(object):
    def __init__(self):
        self.Title = "a title"
        self.Description = ""
        self.getId = "myid"
        self.portal_type = "Image"

    def getURL(self):
        return "http://nohost.com/myid"

    def getObject(self):
        ob = FakeContext()
        ob.title = self.Title

        return ob


class FakeTile(object):

    def __init__(self):
        self.data = {'title': 'a title'}
        self.request = FakeRequest()
        self.url = 'http://nohost.com/@@mytiletype/mytile'


class FakeProperty(object):
    def __init__(self):
        self.photo_max_size = 400
        self.thumb_max_size = 80

    def getProperty(self, name, default=None):
        return getattr(self, name, default)


def fake_get_property(self):
    return FakeProperty()
