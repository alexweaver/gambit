
from abc import ABCMeta, abstractmethod, abstractproperty
from hashlib import md5
from os import path
from request_manager import RequestManager

class WebCrawler(object):
    __metaclass__ = ABCMeta

    def __init__(self, data):
        self._schema = {}

        for k, v in self.raw_schema.iteritems():
            self._schema[k] = self.raw_schema[k] % data

    @abstractproperty
    def raw_schema(self):
        return

    @property
    def schema(self):
        return self._schema

    def crawl(self, *args, **kwargs):
        return dict(self._crawl(*args, **kwargs))

    def _crawl(self, save_dir=None, force=False):

        if save_dir is None:
            raise ValueError('No save directory specified')

        for key, url in self.schema.iteritems():
            
            filename = md5(url).hexdigest()
            filename = path.join(save_dir, filename)

            if not force and path.exists(filename):
                with open(filename, 'rb') as f:
                    yield key, filename
                    continue

            response = RequestManager.get(url)
            if response.status_code != 200:
                yield key, filename
                continue

            content = response.content
            with open(filename, 'w+') as f:
                f.write(content)
                yield key, filename
                continue