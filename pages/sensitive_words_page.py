from utils.wait_utils import WaitUtils
from selenium.webdriver.common.by import By

class SensitiveWordsPage:
    def __init__(self, driver):
        self.wait = WaitUtils(driver, 60)
        self.driver = driver


    #打开敏感词管理界面
    def open_sensitive_words_page(self):
        #点击更多
        self.driver.find_element(By.XPATH,'/html/body/section/section/main'
                                          '/section/aside/div/div/div/div/div[3]/div/span').click()
        #点击敏感词管理
        self.driver.find_element(By.XPATH,'/html/body/section/section/main'
                                          '/section/main/div[2]/div[1]/div'
                                          '/div/div/div[1]/div/div/p').click()



    #添加敏感词
    def add_sensitive_words(self,sensitive_words):
        #点击添加敏感词
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section'
                                          '/main/div[2]/div/div/div/div[2]/button/span').click()
        add_input = self.driver.find_element(By.XPATH,'/html/body/section/section/main'
                                                      '/section/main/div[2]/div[2]/div/div[2]/div[1]/div')
        add_input.send_keys(sensitive_words)
        #点击确认
        self.driver.find_element(By.XPATH,'/html/body/section/section/main'
                                          '/section/main/div[2]/div[2]/div/div[3]/span/button[2]').click()


    #删除敏感词
    def delete_sensitive_words(self):
        pass


    #搜索敏感词
    def search_sensitive_words(self,sensitive_words):
        #判断搜索框是否存在
        if self.wait.wait_for_element_visible((By.XPATH,'/html/body/section/section/main'
                                                        '/section/main/div[2]/div/div/div'
                                                        '/div[1]/div/div/input')):
            self.driver.find_element(By.XPATH,'/html/body/section/section/main'
                                            '/section/main/div[2]/div/div/div'
                                            '/div[1]/div/div/input').send_keys(sensitive_words)
        else:
            return
