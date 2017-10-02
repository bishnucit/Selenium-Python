import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging as log

class ScraperTest(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        #self.driver.set_preference('--disable-popup-blocking')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        

    def test_verify_links_not_same(self):
        log.warning("Starting test of verifying links are not same below search box")
        self.driver.get("https://moat.com/")
        log.warning("opening site")
        temp = ""
        target = self.driver.find_elements_by_xpath('//*[@id="search-bar"]/div/div[1]/span')
        
        for paths in target:
            temp = temp + paths.text

        links =  ' '.join(temp.split(' ')[3:])
        log.warning("the links below the search box are " + str(links))
        log.warning("Reloading server to check the links again")
        self.driver.refresh()
        next1 =  ""
        target = self.driver.find_elements_by_xpath('//*[@id="search-bar"]/div/div[1]/span')
        for paths in target:
            next1 = next1 + paths.text
        new_links = ' '.join(next1.split(' ')[3:])
        log.warning("The new links are " + new_links)
        self.assertNotEqual(str(links), str(new_links))
        log.warning("test_verify_links_not_same completed")
        


##    def test_stale_ad_in_main_page(self):
##
##        log.warning("Starting test of verifying links are not same below search box")
##        self.driver.get("https://moat.com/")
##        log.warning("opening site")
##        temp = ""
##        target = self.driver.find_elements_by_xpath('//*[@id="search-bar"]/div/div[1]/span')
##        
##        for paths in target:
##            temp = temp + paths.text
##
##        links =  ' '.join(temp.split(' ')[3:])
##        log.warning("the links below the search box are " + str(links))
##        log.warning("Reloading server to check the links again")
##        time.sleep(2100)
##        next1 =  ""
##        target = self.driver.find_elements_by_xpath('//*[@id="search-bar"]/div/div[1]/span')
##        for paths in target:
##            next1 = next1 + paths.text
##        new_links = ' '.join(next1.split(' ')[3:])
##        log.warning("The new links are " + new_links)
##        self.assertNotEqual(str(links), str(new_links))
##        log.warning("test_verify_links_not_same completed")
        
    def tearDown(self):
         
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
