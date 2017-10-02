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
                
    def test_verify_search_result_count(self):
        log.warning("Starting test to verify search result count")
        add_count = 0
        self.driver.get("https://moat.com/")
        log.warning("opening site")
        search_text = self.driver.find_element_by_xpath('//*[@id="pro-landing-search-box"]')
        search_text.send_keys('Insight')
        search_text.send_keys(Keys.ENTER)
        log.warning("searching for text insight")
        time.sleep(6)
        
        source = self.driver.page_source
        source = source.encode('utf-8')
        add_count = source.count('.jpg')
        log.warning("going back to search page")
        self.driver.back()
        log.warning("searching for text Bellroy")
        search_text = self.driver.find_element_by_xpath('//*[@id="pro-landing-search-box"]')
        search_text.clear()
        search_text.send_keys('Bellroy')
        search_text.send_keys(Keys.ENTER)
        time.sleep(6)
        source = self.driver.page_source
        source = source.encode('utf-8')

        add_count1 = source.count('.jpg')
        log.warning("Number of Insight Ad shown in the search result page is " + str(add_count))
        
        log.warning("Number of Bellroy Ad is shown in the search result page is " + str(add_count1))

        self.assertTrue(add_count > 30)
        self.assertTrue(add_count1 > 30)

        log.warning("test_verify_search_result_count_completed")



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
