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

time.sleep(3)
def getNewProfileIDs(soup, profilesQueued):
    print("Started function")
    profilesID=[]

    pav=soup.find('section',{"class": "pv-profile-section pv-browsemap-section profile-section artdeco-container-card ember-view"})
    print("Here's the first scrape")
    print(pav)

    all_links = pav.findAll("a", {"pv-browsemap-section__member ember-view"})
    print("Here's the second scrape")
    print(all_links)

    for link in all_links:
        userID = link.get("href")
        if((userID not in profilesQueued) and (userID not in visitedProfiles)):
            profilesID.append(userID)
            print(userID)
    return profilesID 

getNewProfileIDs(BeautifulSoup(browser.page_source, 'html.parser'), profilesQueued)


# https://www.youtube.com/watch?v=d6EQnjj-Bx0