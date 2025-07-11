import time

from selenium.webdriver import Keys, ActionChains

from utils.wait_utils import WaitUtils
from selenium.webdriver.common.by import By


class HotWordPage:
    def __init__(self, driver):
        self.wait = WaitUtils(driver, 30)
        self.driver = driver


    #点击更多应用，打开专有词汇界面
    def click_more_app_and_open_hot_word_page(self):
        #点击更多应用
        self.driver.find_element(By.XPATH, '/html/body/section/section/main/section'
                                           '/aside/div/div/div/div/div[3]/div/span').click()
        time.sleep(2)
        #点击专有词汇管理
        self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main'
                                           '/div[2]/div[1]/div/div/div/div[2]/div').click()

    #切换热词界面的tab页
    def switch_hot_word_page_tab(self,tab_name):
        if tab_name == '人名':
            self.driver.find_element(By.CSS_SELECTOR, '#tab-1').click()
        elif tab_name == '地名':
            self.driver.find_element(By.CSS_SELECTOR, '#tab-2').click()
        elif tab_name == '其他热词':
            self.driver.find_element(By.CSS_SELECTOR, '#tab-3').click()
        time.sleep(2)


    #搜索热词
    def search_hot_word(self,search_key):
        #判断一下当前是否有热词
        if self.wait.wait_for_element_clickable((By.XPATH, '/html/body/section/section/main/section/main/div[2]'
                                              '/div[2]/div/div[2]/div/button/span')):
            return
        else:
            #点击搜索框
            search_input = self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main'
                                                              '/div[2]/div[2]/div/div[1]/div/div/input')
            search_input.click()
            #输入要查找的热词
            search_input.send_keys(search_key)
            #点击查找
            self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main'
                                               '/div[2]/div[2]/div/div[1]/div/button[1]').click()

    #增加热词
    def add_hot_word(self,search_key):
        # # 判断一下当前是否有热词
        # if self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/div[2]'
        #                                                   '/div[2]/div/div[2]/div/button/span'):
        #     #点击添加热词
        #     self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/div[2]'
        #                                                   '/div[2]/div/div[2]/div/button/span').click()
        # else:
        time.sleep(2)
        #点击管理热词
        self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main'
                                           '/div[2]/div[2]/div/div[1]/button/span').click()
        time.sleep(2)
        #获取输入框
        input_box = self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/div[2]/div[2]/div/div[3]'
                                                       '/div[2]/div/div[2]/div[1]/div/div[1]/textarea')
        # input_box.click()
        input_box.send_keys(search_key)



    #热词点击保存
    def hot_word_save(self):
        self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main'
                                           '/div[2]/div[2]/div/div[3]/div[2]/div/div[2]'
                                           '/div[1]/div/div[2]/div/button[2]').click()
        time.sleep(2)
        self.wait.wait_for_element_visible((By.CSS_SELECTOR,
                                            'body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small'))
        # 弹窗点击确定
        confirm_btn = self.driver.find_element(By.CSS_SELECTOR,
                                               'body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small')
        ActionChains(self.driver).move_to_element(confirm_btn).click().perform()
        # 点击保存

        # # 点击确定
        # self.wait.wait_for_element_clickable((By.XPATH, '/html/body/div[2]/div/div[3]/span/button[2]'))
        # # self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/span/button[2]').click()
        # self.driver.execute_script("document.querySelector('.el-button.el-button--primary.el-button--small').click();")


    #热词点击取消
    def hot_word_cancel(self):
        # 点击取消
        self.driver.find_element(By.XPATH, '/html/body/section/section/main'
                                           '/section/main/div[2]/div[2]/div/div[3]/div[2]/div/div[2]'
                                           '/div[1]/div/div[2]/div/button[1]/span').click()
        self.wait.wait_for_element_visible((By.CSS_SELECTOR,
                                            'body > div:nth-child(8) > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small'))
        # 弹窗点击确定
        confirm_btn = self.driver.find_element(By.CSS_SELECTOR,
                                               'body > div:nth-child(8) > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small')

        ActionChains(self.driver).move_to_element(confirm_btn).click().perform()


        # time.sleep(2)
        # #弹窗点击确定离开
        # self.wait.wait_for_element_clickable((By.XPATH, '/html/body/div[2]/div/div[3]/span/button[2]'))
        # self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/span/button[2]').click()
        # self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/span/button[2]').click()

    #删除全部热词
    def delete_hot_word(self):
        #判断是否有热词
        if self.wait.wait_for_element_visible((By.XPATH, '/html/body/section/section/main/section/main/div[2]'
                                                          '/div[2]/div/div[2]/div/button/span')):
             return
        else:
            # 点击管理热词
            self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main'
                                               '/div[2]/div[2]/div/div[1]/button/span').click()
            #点击人名、地名、其他热词
            # self.switch_hot_word_page_tab('人名')
            self.search_hot_word(Keys.CONTROL, 'a')
            #键盘按下backspace
            self.search_hot_word(Keys.BACKSPACE)
            # self.switch_hot_word_page_tab('地名')
            # self.search_hot_word(Keys.CONTROL, 'a')
            # # 键盘按下backspace
            # self.search_hot_word(Keys.BACKSPACE)
            # self.switch_hot_word_page_tab('其他热词')
            # self.search_hot_word(Keys.CONTROL, 'a')
            # # 键盘按下backspace
            # self.search_hot_word(Keys.BACKSPACE)
            #点击保存
            self.hot_word_save()


    #点击确定离开
    def click_confirm_leave(self):
        # self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/span/button[2]').click()
        self.wait.wait_for_element_visible((By.XPATH,
                                            '/html/body/div[2]/div/div[3]/span/button[2]'))
        # 弹窗点击确定
        confirm_btn = self.driver.find_element(By.XPATH,
                                               '/html/body/div[2]/div/div[3]/span/button[2]')

        ActionChains(self.driver).move_to_element(confirm_btn).click().perform()


    #点击下一个
    def click_next(self):
        self.wait.wait_for_element_visible((By.XPATH, '/html/body/section/section/main/section'
                                                       '/main/div[2]/div[2]/div/div[1]/div/button[1]'))
        self.driver.find_element(By.XPATH, '/html/body/section/section/main/section'
                                                       '/main/div[2]/div[2]/div/div[1]/div/button[2]').click()