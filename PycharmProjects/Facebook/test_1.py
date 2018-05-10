#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

#usr = "caaiip75051@piepie.cf"
#pwd = "qeqeqe123"

# Uncomment below lines to load in headless mode
'''
#from pyvirtualdisplay import Display
#import selenium.webdriver.support.ui as ui
#display = Display(visible=0, size=(1024, 768))
#display.start()
'''

#driver = webdriver.Firefox()  # or you can use Chrome(executable_path="/usr/bin/chromedriver")

#driver.get("http://www.facebook.com")

#assert "Facebook" in driver.title
#elem = driver.find_element_by_id("email")
#elem.send_keys(usr)
#elem = driver.find_element_by_id("pass")
#elem.send_keys(pwd)
#elem.send_keys(Keys.RETURN)
#driver.close()
# display.stop()        #Uncomment to load in headless mode

#import mechanize
#import sys
#from bs4 import BeautifulSoup

#reload(sys)
#sys.setdefaultencoding('utf8')
#browser = mechanize.Browser()
#browser.set_handle_robots(False)
#cookies = mechanize.CookieJar()
#browser.set_cookiejar(cookies)
#browser.addheaders = [('User-agent',
                       'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]

#browser.set_handle_refresh(False)
#url = 'https://www.facebook.com/login'
#browser.open(url)
#browser.select_form(nr=0)  # This is login-password form ->nr = number = 0

#browser.form['email'] = "<your facebook email>"
#browser.form['pass'] = "<your facebook password>"
#response = browser.submit()
#soup = BeautifulSoup(response, 'html.parser')
#print
#soup  # redirect output to a html file and open in browser to confirm that facebook is logged in or not.


