#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#import time
#driver = webdriver.Firefox()
#driver.get("https://www.facebook.com")
#print ("Opened facebook")

#user = 'caaiip75051@piepie.cf'
#password = 'qeqeqe123'
#username_box = driver.find_element_by_id('email')
#username_box.send_keys(user)
#print ("Email Id entered")
#time.sleep(1)

#password_box = driver.find_element_by_id('pass')
#password_box.send_keys(password)
#print ("Password entered")

#login_box = driver.find_element_by_id('loginbutton')
#login_box.click()
#print ("Done")
#time.sleep(2)
#logout=driver.find_element_by_id("userNavigationLabel")
#logout.click()
#time.sleep(2)
#logout2=driver.find_element_by_css_selector("li._54ni:nth-child(12) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)")
#logout2.click()



#Python Mechanize Browser Facebook Login Cookies Script v.0.004a
#***************************************************************

# Import
from mechanize import mechanize
import cookielib

# Browser
br = mechanize.Browser()

# User Agent
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Iceweasel/31.5.0')]

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser Optons
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.set_handle_gzip(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Input
Username = str(raw_input("Username: "))
Password = str(raw_input("Password: "))

# Login
br.open('https://www.facebook.com/login.php?login_attempt=1')
br.select_form(nr=0)
br.form['email'] = Username
br.form['pass'] = Password
html = br.submit()

# Test Cookies
contents = html.read()
if '<div class="fsl fwb fcb">Cookies Required</div>' in contents:
   print ("[!] Cookies Failed")
   print (cj)

# Test Login
title = br.title()
if 'Log into Facebook | Facebook' in title:
   print ('[!] Login Failed')
if '<div id="userNavigationLabel" class="_50__"></div>' in contents:
   print ('[*] Successful Login')

#***************************************************************
# End of File
#***************************************************************
