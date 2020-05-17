import os, random, sys, time

try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

from selenium       import webdriver 
from bs4            import BeautifulSoup

#Done with imports
browser     = webdriver.Chrome('driver/chromedriver.exe')
browser.get("https://www.linkedin.com/uas/login")

file        = open('config.txt')
lines       = file.readlines()
username    = lines[0]
password    = lines[1]

time.sleep(5)

elementID   = browser.find_element_by_id('username')
elementID.send_keys(username)

time.sleep(5)

elementID   = browser.find_element_by_id('password')
elementID.send_keys(password)
