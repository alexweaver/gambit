
from bs4 import BeautifulSoup
import hashlib
import os
import requests

def get_url_content(url, timeout=100):
    
    filename = hashlib.md5(url).hexdigest()
    filename = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw", filename)
    
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return BeautifulSoup(f.read(), 'lxml')
            
    response = requests.get(url, timeout=timeout)
    content = response.content
        
    with open(filename, 'w+') as f:
    	f.write(content)
       	return BeautifulSoup(content, 'lxml')