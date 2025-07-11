import time

from selenium.webdriver import ActionChains

from utils.wait_utils import WaitUtils
from selenium.webdriver.common.by import By
import pyautogui


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver, 10)

    # def open(self):
    #     self.driver.get("https://10.12.7.166:9443/")




    def logout(self):
        #点击头像
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/main/section/aside/div/div/div/span/span/div/img').click()
        self.wait.wait_for_element_visible((By.XPATH, '/html/body/div/div[1]/div[2]/div/div/span'))
        #点击退出登录
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div/span').click()

        #点击确定退出
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/main/section/div/div/div[3]/span/button[1]').click()

    #开始实时转写，然后退出登录
    def logout_transcription(self):
        self.wait.wait_for_element_visible((By.XPATH, '/html/body/section/section/main/section/main/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[1]'))
        #开始实时转写
        self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[1]').click()
        #点击开始会议
        self.driver.find_element(By.XPATH, '/html/body/section/div[12]/div/div[2]/div/div[3]/button').click()
        time.sleep(3)
        #点击允许使用麦克风
        ActionChains(self.driver).move_by_offset(636,380).click().perform()
        time.sleep(5)
        #点击头像
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/main/section/aside/div/div/div/span/span/div/img').click()
        self.wait.wait_for_element_visible(("xpath", '/html/body/div/div[1]/div[2]/div/div/span'))
        #点击退出登录
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div/span').click()
        time.sleep(2)
        #点击结束并退出
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[2]/span').click()