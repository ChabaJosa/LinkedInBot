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

time.sleep(2)

elementID   = browser.find_element_by_id('username')
elementID.send_keys(username)

time.sleep(3)

elementID   = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

# Visit your own profile
time.sleep(35)
visitingProfileID = '/in/chaba-josa/'
fullLink = "https://www.linkedin.com" + visitingProfileID
browser.get(fullLink)

# Connect with suggestions 
visitedProfiles = []
profilesQueued  = []

def getNewProfileIDs(soup, profilesQueued):
    profilesID=[]
    pav=soup.find('section',{"class": "pv-profile-section pv-browsemap-section profile-section artdeco-container-card ember-view"})
    all_links = pav.findAll("a", {"class":"pv-browsemap-section__member-container mt4 pv-browsemap-section__member-container-line ember-view"})
    for link in all_links:
        userID = link.get("href")
        if((userID not in profilesQueued) and (userID not in visitedProfiles)):
            profilesID.append(userID)
    return profilesID 

getNewProfileIDs(BeautifulSoup(browser.page_source, 'html.parser'), profilesQueued)


# https://www.youtube.com/watch?v=d6EQnjj-Bx0