
import re

from web_resource import WebResource

class BoardgameResource(WebResource):

	def __init__(self, id):
		super(BoardgameResource, self).__init__(id)

	def set_url_schema(self, id):
		
		self._url_schema = {}
		base_api_url = 'https://boardgamegeek.com/xmlapi2/thing?id=%s' % id
		self._url_schema['stats'] = base_api_url + '&type=boardgame&stats=1'

	def get_description(self):

		text = self.data('stats').find('items').find('item').find('description').get_text()
		text = str(text)

		# text = re.sub('\&\#[0-9]{2}', '', text)
		# text = re.sub(';', '', text)

		return text