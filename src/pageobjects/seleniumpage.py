'''
Created on Feb 13, 2018

@author: gustavo
'''
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SeleniumPage(object):
    '''
    classdocs
    '''
    SELENIUM = 'Online Courses - Anytime, Anywhere | Udemy'
    DELAY = 30 # seconds
    TEXT = 'text'
    TITLE = 'title'
    MESSAGE = "We aren't in the right page"
    OUTERHTML = 'outerHTML'
    INNERTEXT = 'innerText'
    FILTERS_XPATH = '//*[@id="filters-bar-container"]/div[1]/div[1]/button/span[2]'
    PRICECONTAINER_CSS = "div[class='filter--filter-container--2BpVy']"
    PAIDFREE_CSS = "span[class='filter--filter-option-text--3nAaz']"
    FREECOUNT_CSS = "span[class='filter--filter-option-count--3QA7t']"
    FREE_CHECK_BOX_CLASS = "checkbox-label"
    FREE = 'Free'
    def __init__(self, browser):
        '''
        Constructor
        '''
    def check_page(self, browser):
        # Check if we are in the Online Courses
        selenium = WebDriverWait(browser, self.DELAY).until(EC.presence_of_element_located((By.TAG_NAME, 'title')))
        assert (selenium.get_attribute(self.TEXT) == self.SELENIUM),self.MESSAGE
        
    def filters(self, browser):
        filters = browser.find_element_by_xpath(self.FILTERS_XPATH)
        return filters

    def price_container(self, browser):
        price_container = browser.find_elements_by_css_selector(self.PRICECONTAINER_CSS)
        return price_container[4]

    def paid_free(self, browser):
        paid_free = self.price_container(browser).find_elements_by_css_selector(self.PAIDFREE_CSS)
        return paid_free[1]
    
    def free_count(self, browser):
        free_count = self.price_container(browser).find_elements_by_css_selector(self.FREECOUNT_CSS)
        return free_count[1]

    def free_check_box (self, browser):
        free_check_box = browser.find_elements_by_class_name(self.FREE_CHECK_BOX_CLASS)
        for i in range(0,len(free_check_box)):
            if self.FREE in free_check_box[i].get_attribute(self.INNERTEXT):
                free_check_box[i].click()
                return free_check_box[i]
            
    def search4freecourses(self,browser):
        self.check_page(browser)
        time.sleep(5)
        filters = self.filters(browser)
        filters.click()
        free_count = self.free_count(browser)
        self.free_check_box (browser)
        time.sleep(5)
        free_courses = int(free_count.get_attribute('innerText'))
        return free_courses

    def selenium_free_list(self, browser):
            price_list = []
            name_list =[]
            container = browser.find_elements_by_class_name("col-md-9")
            while len(container) == 0:
                container = browser.find_elements_by_class_name("col-md-9")
            if len(container) > 0:
                price = container[0].find_elements_by_class_name("ml5")
                course = container[0].find_elements_by_tag_name("h1")
                time.sleep(10)
                for i in range(0,len(price)):
                    price_list.append(price[i].get_attribute('innerText'))
                for i in range(0,len(course)):
                    name_list.append(course[i].get_attribute('innerText'))
            return  (name_list, price_list)

                
            
        

    
        