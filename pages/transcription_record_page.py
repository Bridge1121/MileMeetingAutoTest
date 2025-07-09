import time

from selenium.webdriver import Keys

from utils.wait_utils import WaitUtils

#转写记录页面
class TranscriptionRecordPage:
    def __init__(self, driver):
        self.wait = WaitUtils(driver, 10)
        self.driver = driver

    #打开会议记录
    def open_transcription_record(self):
        self.driver.find_element_by_xpath('/html/body/section/section/main/section/aside/div/div/div/div/div[2]/div/span').click()



    #搜索会议记录，进入并返回
    def search_transcription_record_click_and_back(self,search_title="20"):
        #点击搜索框
        search_input = self.driver.find_element_by_xpath('/html/body/section/section/main/section/main/div[2]/div/div/div/div[1]/form/div/div/input')
        search_input.click()
        #输入搜索内容
        search_input.send_keys(search_title)
        search_input.send_keys(Keys.ENTER)
        #选择第二页
        self.driver.find_element_by_xpath('/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[2]/div/ul/li[2]').click()
        #点击并进入记录
        self.driver.find_element_by_xpath('/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]').click()
        #返回
        back_btn = self.driver.find_element_by_xpath('/html/body/section/section/main/section/main/div[2]/div/div/div[1]/div[1]/a/i')
        back_btn.click()
        #清空搜索框
        search_input.clear()
        time.sleep(2)


    #修改分页设置
    def modify_page_setting(self):
        #点击分页下拉框
        self.driver.find_element_by_xpath('/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[2]/div/span[2]/div/div[1]/input').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]/span').click()
        time.sleep(2)
        #点击页面跳转按钮
        self.driver.find_element_by_xpath('/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[2]/div/button[2]/i').click()
        time.sleep(2)
        #点击会议记录并返回
        self.driver.find_element_by_xpath('/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]').click()
        #返回
        back_btn = self.driver.find_element_by_xpath(
            '/html/body/section/section/main/section/main/div[2]/div/div/div[1]/div[1]/a/i')
        back_btn.click()
        time.sleep(2)
        #页面跳转输入框
        self.driver.find_element_by_xpath('/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[2]/div/span[3]/div/input').send_keys('1')





