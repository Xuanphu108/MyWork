#!/usr/bin/python
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

profile = webdriver.ChromeOptions()
profile.add_argument('--proxy-server=153.149.168.38:3128')

#firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
#firefox_capabilities['marionette'] = True
#firefox_capabilities['binary'] = '/usr/local/bin/geckodriver'
#driver = webdriver.Firefox(capabilities=firefox_capabilities)

#profile = webdriver.FirefoxProfile()
#profile.set_preference("network.proxy.type",1)
#profile.set_preference("network.proxy.http",'46.102.106.59')
#profile.set_preference("network.proxy.http_port",'13228')

#profile.set_preference("network.proxy.ssl",'46.102.106.59')
#profile.set_preference("network.proxy.ssl_port",'13228')
#driver = webdriver.Firefox(profile)

driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver',chrome_options=profile)
driver.get('https://whoer.net')
time.sleep(3)
driver.close()
