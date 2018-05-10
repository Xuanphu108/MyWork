import os, time
from config import DATABASE
import function_webdriver
from selenium import webdriver
# Information users
user_name = DATABASE['user_name']
password = DATABASE['password']
textSearch = DATABASE['textSearch']

def execute():
    function_webdriver.get_URL('https://www.facebook.com/')
    function_webdriver.login(user_name, password)
    search_page = function_webdriver.get_URL('https://www.facebook.com/search/str/' + textSearch + '/stories-keyword/today/date/stories/intersect')
    function_webdriver.see_more_link()
    print ('Done')

def main():
    print('OK')

if __name__ == '__main__':
    #execute()
    main()
    #function_webdriver.quit()
