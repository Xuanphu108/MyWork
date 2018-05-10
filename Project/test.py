#!/usr/bin/python
from selenium import webdriver
 
#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument("--test-type")
#options.binary_location = "/usr/lib/chromium-browser"
#driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')
 
#driver.get('http://imgur.com/')
 
#images = driver.find_elements_by_tag_name('img')
#for image in images:
#    print(image.get_attribute('src'))
 
#driver.close()


import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

#http = httplib2.Http()
#status, response = http.request('http://www.nytimes.com')
#print (status, response)
#for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
#    if link.has_attr('href'):
#        print link['href']

from selenium.webdriver.common.keys import Keys
from time import sleep
import time

#user=" "
#password=" "
#driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
#driver.get('https://www.facebook.com/')
#print ("Opened facebook")
#username_box = driver.find_element_by_id('email')
#username_box.send_keys(user)
#print ("Email Id entered")
#time.sleep(1)
#password_box = driver.find_element_by_id('pass')
#3password_box.send_keys(password)
#print ("Password entered")
 
#login_box = driver.find_element_by_id('loginbutton')
#login_box.click()


 
#print ("Done")

#time.sleep(5)
#driver.get('https://www.facebook.com/search/str/i%20want%20this%20shirt/stories-keyword/today/date/stories/intersect')
 

#list_of_elements = ["img"]
#for tag_name in list_of_elements:
#    for element in driver.find_elements_by_tag_name(tag_name)
#       print element

#import numpy as np
#import matplotlib.pyplot as plt
#from sklearn import svm

# XOR dataset and targets
#X = np.c_[(0, 0),
#          (1, 1),
#          #---
#          (1, 0),
#          (0, 1)].T
#Y = [0]*2 + [1]*2
# figure number
#fignum = 1

# fit the model
#for kernel in ('sigmod', 'poly', 'rbf'):
#  clf = svm.SVC(kernel = kernel, gamma = 4, coef0 = 0)
#  clf.fit

import mechanize
import sys
from bs4 import BeautifulSoup
reload(sys)  
sys.setdefaultencoding('utf8')
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
     
browser.set_handle_refresh(False)
url = 'https://www.facebook.com/login'
browser.open(url)
browser.select_form(nr = 0)       #This is login-password form ->nr = number = 0
   
browser.form['email'] = "<your facebook email>"
browser.form['pass'] = "<your facebook password>"
response = browser.submit()
soup = BeautifulSoup(response,'html.parser')
print soup #redirect output to a html file and open in browser to confirm that facebook is logged in or not.
