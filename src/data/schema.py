
from hashlib import md5
from os import path

class Schema(object):

    def __init__(self, raw, data, repo):
        
        self._repo = repo

        self._schema = {}
        for k, v in raw.iteritems():
            self._schema[k] = v % data

    @property
    def schema(self):

        return self._schema

    @property
    def repo(self):

        return self._repo

    def url(self, key):

        return self.schema[key]

    def local(self, key):

        url = self.schema[key]
        filename = md5(url).hexdigest()
        filename = path.join(self.repo, filename)
        return filename