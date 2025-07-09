import time

from utils.wait_utils import WaitUtils
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver, 10)

    #返回到首页
    def back_home(self):
        #点击首页
        self.driver.find_element(By.CLASS_NAME, 'title').click()
        time.sleep(2)