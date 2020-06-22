
from selenium import webdriver

driver = webdriver.Chrome('/root/campingman/chromedriver')
driver.implicitly_wait(3)

driver.get('https://google.com')
