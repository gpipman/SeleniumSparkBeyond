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

class LoginPage(object):
    '''
    classdocs
    '''
    #browser = webdriver.Chrome(executable_path=r'/mnt/working/usr/local/bin/chromedriver')
    DELAY = 30 # seconds
    ONLINE_COURSES = "Online Courses - Anytime, Anywhere | Udemy" 
    def __init__(self, browser):
        '''
        Constructor
    '''
    def check_page(self, browser):
            # Check if we are in the Online Courses
        login = WebDriverWait(browser, self.DELAY).until(EC.presence_of_element_located((By.TAG_NAME, 'title')))
        assert (login.get_attribute('text') == self.ONLINE_COURSES),"We aren't in the right page"

    def login_btn(self,browser):
        btn = browser.find_element_by_class_name("btn")
        btn.click()
        return btn 

    def wait4loginbox(self,browser,EMAIL,PASSWORD):
        myElem = WebDriverWait(browser, self.DELAY).until(EC.presence_of_element_located((By.CLASS_NAME, "loginbox-v4__header")))
        self.email(browser).send_keys(EMAIL)
        self.password(browser).send_keys(PASSWORD)
        self.submit(browser).click()

    def email(self,browser):
        email = browser.find_element_by_class_name("emailinput")
        return email

    def password (self,browser):
        password =browser.find_element_by_id("id_password")
        return password

    def submit(self,browser):
        submit = browser.find_element_by_name("submit")
        return submit
    