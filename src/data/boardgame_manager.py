
from abc import ABCMeta, abstractmethod, abstractproperty
from web_crawler import WebCrawler

class ResourceManager(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self._crawler = WebCrawler()

	def set_url_schema(self, schema):
		self._crawler.url_schema = schema
		return self

class BoardgameManager(ResourceManager):

	def __init__(self):
		super(BoardgameManager, self).__init__()






# has to have crawler
# 