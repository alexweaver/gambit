
from web_crawler import WebCrawler

class BoardgameCrawler(WebCrawler):

    raw_schema = \
    {
        'stats': 'https://boardgamegeek.com/xmlapi2/thing?id=%(id)s&stats=1'
    }

    def __init__(self, data):
        super(BoardgameCrawler, self).__init__(data)