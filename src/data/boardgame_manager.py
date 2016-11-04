
from abc import ABCMeta, abstractmethod, abstractproperty
from web_crawler import WebCrawler

class ResourceManager(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self._crawler = WebCrawler()
		self._parser = None
		
	@property
	def crawler(self):
		return self._crawler

	@property
	def parser(self):
		return self._parser

class BoardgameManager(ResourceManager):

	def __init__(self):
		super(BoardgameManager, self).__init__()






# has to have crawler
# 