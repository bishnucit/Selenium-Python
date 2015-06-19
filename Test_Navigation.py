from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://marketplace-dev.allizom.org/")
driver.implicitly_wait(12)
#assert "Develop Apps" in driver.page_source
driver.find_element_by_xpath("//*[@id='footer']/ul/li[3]/a").click()
driver.implicitly_wait(5)
assert "Developers | Firefox Marketplace" in driver.title

print "Running new TestCase "
#assert "API Reference" in driver.page_source
driver.find_element_by_xpath("//*[@id='site-header']/div/div/a[1]").click()
assert "App Development API Reference - App Center | MDN" in driver.title
driver.back()
print "Test Case successfully ran"
print "Running new TestCase "
#assert "Support" in driver.page_source
driver.find_element_by_xpath("//*[@id='site-header']/div/div/a[2]").click()
assert "Support | Developers | Firefox Marketplace" in driver.title
driver.back()
print "Test Case successfully ran"
print "Running new TestCase "
#assert "Submit an app" in driver.page_source
driver.find_element_by_xpath("//*[@id='site-header']/div/div/a[3]").click()
assert "Sign in / Sign up" in driver.page_source
driver.back()
print "Test Case successfully ran"
print "Running new TestCase "
#assert "My Submissions" in driver.page_source
driver.find_element_by_xpath("//*[@id='site-header']/div/div/a[4]").click()
#assert "proceed" in driver.page_source
driver.back()
print "Test Case successfully ran"
print "Running new TestCase "
#assert "Marketplace" in driver.page_source
driver.find_element_by_xpath("//*[@id='site-header']/div/div/a[5]").click()
assert "Firefox Marketplace" in driver.title
driver.back()
print "All Test Cases Passed"

driver.close()