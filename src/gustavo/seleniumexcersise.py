'''
Created on Feb 12, 2018

@author: gustavo
'''
import unittest
from selenium import webdriver
from waitforpageload import WaitForPageLoad
from pageobjects.login_page import LoginPage
from pageobjects.online_courses_page import OnlineCoursesPage
from pageobjects.webdevelopmentpage import WebDevelopmentPage
from pageobjects.seleniumpage import SeleniumPage
from pageobjects.seleniumexercisepage import SeleniumExercisePage

 
class SeleniumExercise(unittest.TestCase):
    SPARKBEYONDSITE='http://www.udemy.com/'
    browser = webdriver.Chrome(executable_path=r'/mnt/working/usr/local/bin/chromedriver')
    UDEMY_TITLE = "Online Courses - Learn Anything, On Your Schedule | Udemy"
    #TODO: extract EMAIL and PASSWORD as external arguments
    EMAIL = "gpipman@gmail.com"
    PASSWORD = "123456" 
    ONLINE_COURSES = "Online Courses - Anytime, Anywhere | Udemy" 
    FREE =  'Free' 
    SELENIUM = 'Selenium'

    def setUp(self):
        sep = SeleniumExercisePage(self.browser)
        self.browser.get(self.SPARKBEYONDSITE)
        self.browser.set_window_position(3000, 200, "current")
        sep.checkPage(self.browser)
        pass


    def tearDown(self):
        self.browser.close()
        pass


    def testName(self):
        # Define PageObjects
        wp = WaitForPageLoad(self.browser)
        lg = LoginPage(self.browser)
        oc = OnlineCoursesPage(self.browser)
        wbd = WebDevelopmentPage(self.browser)
        se = SeleniumPage(self.browser)

        lg.login(self.browser,self.EMAIL,self.PASSWORD)
        wp.old_page_loaded_()
        wp.wait_for_page_redirect()
        oc.selectwebdevelopmentfromcategories(self.browser)
        wp.wait_for_page_redirect()
        # WebDevelopment Search Selenium Courses
        wbd.seleniumsearch(self.browser)
        wp.wait_for_page_redirect()
        free_courses = se.search4freecourses(self.browser)
        assert free_courses > 2 and free_courses < 10
        # Verify Selenium word in courses and all are Free
        [selenium_list, free_list] = se.selenium_free_list(self.browser)
        for i in range(0,len(free_list)):
            if free_list[i] != self.FREE:
                assert False
        name_list_splitted = " ".join(selenium_list).split()
        keyword_list = [self.SELENIUM]
        if any(word in name_list_splitted for word in keyword_list):
            assert True
        else:
            assert False
        pass
         


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    