'''
Created on Feb 13, 2018

@author: gustavo
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from gustavo.waitforpageload import WaitForPageLoad
class OnlineCoursesPage(object):
    '''
    classdocs
    '''
    DELAY = 30 # seconds
    ONLINE_COURSES = "Online Courses - Anytime, Anywhere | Udemy"   
   
    def __init__(self, browser):
        '''
        Constructor
        '''
    def check_page(self, browser):
                # Check if we are in the Online Courses
        onlineCourses = WebDriverWait(browser, self.DELAY).until(EC.presence_of_element_located((By.TAG_NAME, 'title')))
        print onlineCourses.get_attribute('text')
        assert (onlineCourses.get_attribute('text') == self.ONLINE_COURSES),"We aren't in the right page"
        
    def categories(self, browser):
        categories = browser.find_element_by_class_name("ellipsis")
        print categories.get_attribute('outerHTML')
        return categories

    def development(self, browser):
        development = browser.find_elements_by_xpath('//*[contains(text(), "Development") and @class="menu__title"]')
        print development[0].get_attribute('outerHTML')
        return development[0]

    def webdevelopment(self, browser):
        webdevelopment = browser.find_elements_by_xpath('//*[contains(text(), "Web Development") and @class="menu__title"]')
        print webdevelopment[0].get_attribute('outerHTML')
        return webdevelopment[0]

    def hover(self, browser,webelement):
        hover = ActionChains(browser).move_to_element(webelement).click().perform()
        return hover

    def selectwebdevelopmentfromcategories(self, browser):
        wp = WaitForPageLoad(browser)
        self.check_page(browser)
        categories = self.categories(browser)
        ActionChains(browser).move_to_element(categories).perform()
        development = self.development(browser)
        ActionChains(browser).move_to_element(development).perform()
        webdevelopment = self.webdevelopment(browser)
        wp.old_page_loaded_()
        ActionChains(browser).move_to_element(webdevelopment).click().perform()

        
        

        