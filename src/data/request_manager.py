
from bs4 import BeautifulSoup
import hashlib
import os
import requests
import time
import urlparse

class RequestManager(object):

    host_intervals = {'boardgamegeek.com': 1}
    last_request_log = {}

    @staticmethod
    def get(url):
        host = urlparse.urlsplit(url).netloc

        wait = 5
        if host in RequestManager.host_intervals:
            wait = RequestManager.host_intervals[host]
        
        if host not in RequestManager.last_request_log:
            RequestManager.last_request_log[host] = time.time()
            return requests.get(url)

        delta = time.time() - RequestManager.last_request_log[host]

        if (wait > delta):
            time.sleep(max(wait, 0))

        RequestManager.last_request_log[host] = time.time()
        return requests.get(url)