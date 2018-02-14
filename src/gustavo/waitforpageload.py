'''
Created on Dec 30, 2017

@author: gustavo
'''
import time 


class WaitForPageLoad(object):

    def __init__(self, browser):
        self.browser = browser
    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def old_page_loaded_(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def page_has_loaded(self):
        self.new_page = self.browser.find_element_by_tag_name('html')
        return self.new_page.id == self.old_page.id

    def wait_for_page_redirect(self):
        while self.page_has_loaded():
            time.sleep(0.5)
        return

    def __exit__(self, *_):
        print ("__exit__")
        while self.page_has_loaded :
            print ("waiting to exit")
