#!/usr/bin/python
import time
from selenium import webdriver
from selenium.webdriver import FirefoxProfile, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import DATABASE

host_port = DATABASE['host_port']
enable_change_proxy = DATABASE['enable_change_proxy']

class function_webdriver():

    def __init__(self):
        self.profile = webdriver.ChromeOptions()
        if enable_change_proxy:
            self.profile = self.change_proxy(host_port, self.profile)
        else:
            self.profile = self.clear_proxy(self.profile)
        self.driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver', chrome_options=self.profile)
        #self.driver.maximize_window()


    def change_proxy(self, host_port, profile: object = None):
        if profile is None:
            profile = webdriver.ChromeOptions()
        profile.add_argument('--proxy-server=host_port')
        return profile

    def clear_proxy(self, profile = None):
        if profile is None:
            profile = webdriver.ChromeOptions()
        profile.add_argument('--no-proxy-server')
        return profile

    def login(self, user_name, password):
        print("Opened facebook")
        username_box = self.driver.find_element_by_id('email')
        username_box.send_keys(user_name)
        print("Email Id entered")
        time.sleep(1)
        password_box = self.driver.find_element_by_id('pass')
        password_box.send_keys(password)
        print("Password entered")
        login_box = self.driver.find_element_by_id('loginbutton')
        login_box.click()
        print("Done")
        return True

    def logout(self):
        logout1 = self.driver.find_element_by_css_selector("#userNavigationLabel")
        logout1.click()
        time.sleep(2)
        logout2 = self.driver.find_element_by_css_selector(
            "li._54ni:nth-child(12)>a:nth-child(1)>span:nth-child(1)>span:nth-child(1)")
        logout2.click()
        return True

    def get_URL(self, url):
        self.driver.get(url)
        return self.driver.get(url)

    #def click_bookmark(self):


    def load(self):
        self.driver.get('https://www.facebook.com')

    def quit(self):
        return self.clear_proxy(self.profile)

    def see_more_link(self):
        all_pages = self.driver.find_elements_by_class_name('see_more_link')
        for i in all_pages:
            i.click()




####################################################-execute-###########################################################
C = function_webdriver()
C.change_proxy(host_port)
C.get_URL('https://whoer.net')
C.get_URL('https://www.facebook.com')
user_name = DATABASE['user_name']
password = DATABASE['password']
C.login(user_name, password)
C.logout()


