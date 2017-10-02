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
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        #self.driver.set_preference('--disable-popup-blocking')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        


    def test_share_add(self):
        log.warning("Starting test to test share option in ad")
        self.driver.get("https://moat.com/")
        log.warning("opening site")
        search_text = self.driver.find_element_by_xpath('//*[@id="pro-landing-search-box"]')
        search_text.send_keys('Insight')
        search_text.send_keys(Keys.ENTER)
        log.warning("searching for text insight")
        time.sleep(10)
        log.warning("Hovering over the first ad to click on share link")
        add = self.driver.find_element_by_xpath('//*[@id="er-app"]/div/div[4]/div[1]/div[2]/div[1]')
        Hover = ActionChains(self.driver).move_to_element(add)
        Hover.perform()

        sharebutton = self.driver.find_element_by_xpath('//*[@id="er-app"]/div/div[4]/div[1]/div[1]/div[4]/div/div/a')
        sharebutton.click()

        log.warning("clicked on share button")
        time.sleep(5)
        self.driver.save_screenshot("sharelink.png")
        log.warning("copy link button is visible for user to share ad")
        log.warning("test_share_add completed" )


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
