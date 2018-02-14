'''
Created on Feb 13, 2018

@author: gustavo
'''
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from gustavo.waitforpageload import WaitForPageLoad
class WebDevelopmentPage(object):
    '''
    classdocs
    '''
    WEBDEVELOPMENT = 'Web Development Online Courses: Build and Enhance Websites'
    TEXT = 'text'
    TITLE = 'title'
    DELAY = 30 # seconds
    MESSAGE = "We aren't in the right page"
    SEARCHNAME = "q"
    SELENIUM = "Selenium"

    def __init__(self, browser):
        '''
        Constructor
        '''
    def check_page(self, browser):
            # Check if we are in the Online Courses
        webdevelopment = WebDriverWait(browser, self.DELAY).until(EC.presence_of_element_located((By.TAG_NAME, self.TITLE)))
        print webdevelopment.get_attribute(self.TEXT)
        assert (webdevelopment.get_attribute(self.TEXT) == self.WEBDEVELOPMENT), self.MESSAGE
        
    def search(self, browser):
        search = browser.find_element_by_name(self.SEARCHNAME)
        return search 
    
    def seleniumsearch (self, browser):
        wp = WaitForPageLoad(browser)
        self.check_page(browser)
        wp.old_page_loaded_()
        search = self.search(browser)
        search.send_keys(self.SELENIUM)
        search.submit()
     
     
   
    