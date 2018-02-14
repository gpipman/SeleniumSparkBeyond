'''
Created on Feb 14, 2018

@author: gustavo
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SeleniumExercisePage(object):
    '''
    classdocs
        '''
    DELAY = 30 # seconds  
    UDEMY_TITLE = "Online Courses - Learn Anything, On Your Schedule | Udemy"



    def __init__(self, browser):
        '''
        Constructor
        '''
    def checkPage(self,browser):
        WebDriverWait(browser, self.DELAY).until(EC.presence_of_element_located((By.TAG_NAME, 'title')))
        udemytitle = browser.find_element_by_tag_name("title")
        assert (udemytitle.get_attribute('text') == self.UDEMY_TITLE),"We aren't in the right page"
    
        