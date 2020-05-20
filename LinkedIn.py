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

# 1) Visit your own profile
time.sleep(35)
visitingProfileID = '/in/chaba-josa/'
fullLink = "https://www.linkedin.com" + visitingProfileID
browser.get(fullLink)


# -----------------------------------------------------------------------------------------

# 2) Connect with profile suggestions 
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

# -----------------------------------------------------------------------------------------

# 3) Query Positions (Not Completed)
# search-global-typeahead__input always-show-placeholder

# parameterArray  = []
# def searchJobs (JobSearchArray, usLocation):
#     time.sleep(3)
#     soup = BeautifulSoup(browser.page_source, 'html.parser')

#     for i in JobSearchArray:
#         currentSearch = JobSearchArray[JobSearchArray.index(i)].split()
#         print(currentSearch)
#         print(f"https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=101318387&keywords={currentSearch[0]}%20{currentSearch[1]}&location={usLocation}%2C%20United%20States")
#         parameterArray.append(f"https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=101318387&keywords={currentSearch[0]}%20{currentSearch[1]}&location={usLocation}%2C%20United%20States")

#         time.sleep(3)
#         for i in parameterArray:
#             browser.get(parameterArray[parameterArray.index(i)])


# searchJobs(["FrontEnd Developer"],"Florida")

# Researched from
# https://www.youtube.com/watch?v=d6EQnjj-Bx0 For DMs
# https://youtu.be/_GcEkRzjjGI For John Fisher Bot
# https://www.youtube.com/watch?v=j37IGnnImv4 #For Job Applications and overall navigation.
# https://github.com/fdupuis659/LinkedIn-Automatic-Job-Applier

