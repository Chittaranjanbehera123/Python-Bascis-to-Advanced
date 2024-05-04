# Request Module in Python 
# The Python Requests Module is an HTTP Library that enables developer to send HTTP requests in python . This module enables enables you to send 
# HTTP requests in Python. This module enables you to send HTTP requests using python code and makes it possible to interact with APIs and web services. 

# Installations:
# Pip install requests

# Get Request:
# once you have installed the requests module, You can start using it to send HTTP requests. Here is simple example that sends aGET requests to the Google homepage: 
import requests
from bs4 import BeautifulSoup
url="https://www.google.com"

r= requests.get(url)