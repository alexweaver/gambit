
from abc import ABCMeta, abstractmethod, abstractproperty
from get_url_content import get_url_content

class WebResource(object):
	__metaclass__ = ABCMeta

	def __init__(self, id):
		self.id = id
		self.url_schema = self.id 

	@property
	def url_schema(self):
		return self._url_schema

	@url_schema.setter
	def url_schema(self, id):
		self.set_url_schema(id)

	@abstractmethod
	def set_url_schema(self, id):
		return

	def data(self, tag):
		return get_url_content(self.url_schema[tag])