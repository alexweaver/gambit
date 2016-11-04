
from hashlib import md5
from os import path
from request_manager import RequestManager

class Crawler(object):

    def __init__(self, schema):
        self._schema = schema

    @property
    def schema(self):
        return self._schema

    def crawl(self, key=None, force=False):

        if key is None:
            raise ValueError('No key specified')

        filename = self.schema.local(key)
        url = self.schema.url(key)
        
        if not force and path.exists(filename):
            return True
    
        response = RequestManager.get(url)
        if response.status_code != 200:
            return False
    
        content = response.content
        with open(filename, 'w+') as f:
            f.write(content)
            return True