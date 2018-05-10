#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import time
import imp
from urllib import urlretrieve
from httplib import BadStatusLine


#user=input('Enter Email Id:')
user="voagki27393@piapia.gq" 
#pass=input('Enter Password:')
password="qeqeqe123" 
#capabilities = DesiredCapabilities.FIREFOX.copy()
#capabilities['marionette'] = False 
#driver = webdriver.Firefox(capabilities=capabilities)
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')


driver.get('https://www.facebook.com/')

#assert "facebook" in driver.title

print ("Opened facebook")
#sleep(1)
 
username_box = driver.find_element_by_id('email')
username_box.send_keys(user)
print ("Email Id entered")
time.sleep(1)
 
password_box = driver.find_element_by_id('pass')
password_box.send_keys(password)
print ("Password entered")
 
login_box = driver.find_element_by_id('loginbutton')
login_box.click()

print ("Done")
#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument("--test-type")
#options.binary_location = "/usr/lib/chromium-browser/chromedriver"
#browser = webdriver.Chrome(chrome_options=options)


time.sleep(5)
driver.get('https://www.facebook.com/search/str/i%20want%20this%20shirt/stories-keyword/today/date/stories/intersect')


#images= driver.find_elements_by_tag_name('img')
#print (images)
#for image in images:
# print (image)
#  if (image.size.get('width')>450):
#    print (image)
#    image.click()
#    time.sleep(2)
#    image.send_keys(Keys.ESCAPE)
#    print(image.get_attribute('src'))
#    time.sleep(1)
#time.sleep(5)

#list_of_elements = [
child = driver.find_elements_by_css_selector("a[rel='theater']")
for element in child:
  print (element)
  likes = element.find_element_by_css_selector('span data-hover=/"tooltip/"')
  print (likes)
  #element.click()
  #time.sleep(5)
  #element.send_keys(Keys.ESCAPE)  
  time.sleep(2)


#body = driver.find_element_by_tag_name('body')
#numberofscrolls = 100
#for i in range(10):
#  body.send_keys(Keys.ESCAPE)
#  time.sleep(1)
#for i in range(numberofscrolls):
#  body.send_keys(Keys.PAGE_DOWN)
#  body.send_keys(Keys.ESCAPE)
#  print("Scroll Count: {0}".format(i + 1))
#  time.sleep(1)


time.sleep(5)
logout1 = driver.find_element_by_css_selector("#userNavigationLabel")
logout1.click()
time.sleep(2)
logout2 = driver.find_element_by_css_selector("li._54ni:nth-child(12)>a:nth-child(1)>span:nth-child(1)>span:nth-child(1)").click()
#driver.close
input('Press anything to quit')
driver.quit()
print("Finished")
