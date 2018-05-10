#!/usr/bin/python
import time
from selenium import webdriver
from selenium.webdriver import FirefoxProfile, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import DATABASE

host = DATABASE['host']
port = DATABASE['port']
enable_change_proxy = DATABASE['enable_change_proxy']

class function_webdriver():

    def __init__(self):
        self.profile = FirefoxProfile()
        if enable_change_proxy:
            self.profile = self.change_proxy(host, port, self.profile)
        else:
            self.profile = self.clear_proxy(self.profile)
        self.profile.update_preferences()
        self.driver = webdriver.Firefox(firefox_profile=self.profile)
        self.driver.maximize_window()


    def change_proxy(self, host, port, profile: object = None):
        if profile is None:
            profile = FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", host)
        profile.set_preference("network.proxy.http_port", int(port))
        profile.set_preference("network.proxy.ssl", host)
        profile.set_preference("network.proxy.ssl_port", int(port))
        profile.update_preferences()
        return profile

    def clear_proxy(self, profile = None):
        if profile is None:
            profile = FirefoxProfile()
        profile.set_preference("network.proxy.type", 0)
        profile.update_preferences()
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
        logout = self.driver.find_element_by_id("userNavigationLabel")
        logout.click()
        time.sleep(1)
        logout2 = self.driver.find_element_by_css_selector(
            "li._54ni:nth-child(12) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)")
        logout2.click()
        return True

    def get_URL(self, url):
        self.driver.get(url)
        return self.driver.get(url)

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
C.change_proxy(host, port)
C.get_URL('https://whoer.net')
C.get_URL('https://www.facebook.com')
user_name = DATABASE['user_name']
password = DATABASE['password']
C.login(user_name, password)
C.logout()


