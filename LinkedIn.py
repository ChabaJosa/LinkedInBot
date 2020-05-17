import os, random, sys, time

try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

from selenium       import webdriver 
from bs4            import BeautifulSoup

#Done with imports

browser  = webdriver.Chrome('driver/chromedriver.exe')