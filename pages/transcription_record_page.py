import time
from telnetlib import EC

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import wait

from utils.wait_utils import WaitUtils

from selenium.webdriver.common.by import By

#转写记录页面
class TranscriptionRecordPage:
    def __init__(self, driver):
        self.wait = WaitUtils(driver, 10)
        self.driver = driver

    #打开会议记录
    def open_transcription_record(self):
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/aside'
                                          '/div/div/div/div/div[2]/div/span').click()



    #搜索会议记录，进入并返回
    def search_transcription_record_click_and_back(self,search_title="20"):
        #点击搜索框
        search_input = self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/div[1]/form/div/div/input')
        search_input.click()
        #输入搜索内容
        search_input.send_keys(search_title)
        search_input.send_keys(Keys.ENTER)
        #选择第二页
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[2]/div/ul/li[2]').click()
        #点击并进入记录
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]').click()
        #返回
        back_btn = self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div[1]/div[1]/a/i')
        back_btn.click()
        #清空搜索框
        search_input.clear()
        time.sleep(2)


    #修改分页设置
    def modify_page_setting(self):
        #点击分页下拉框
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[2]/div/span[2]/div/div[1]/input').click()
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[1]/span').click()
        time.sleep(2)
        #点击页面跳转按钮
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[2]/div/button[2]/i').click()
        time.sleep(2)
        #点击会议记录并返回
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]').click()
        #返回
        back_btn = self.driver.find_element(By.XPATH,
            '/html/body/section/section/main/section/main/div[2]/div/div/div[1]/div[1]/a/i')
        back_btn.click()
        time.sleep(2)
        #页面跳转输入框
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section'
                                          '/main/div[2]/div/div/div/div[2]'
                                          '/div[2]/div/span[3]/div/input').send_keys('1')




    #列表文件名称修改，全删除不输入，修改后不保存，输入40个字符，输入英文数字特殊字符
    def modify_file_name(self,new_name="hhhhh测试哈哈哈哈哈哈哈enenenne13543646243432!@$$"):
        #hover到会议标题上
        file_item = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/section/main/section/main/div[2]/div/div/div/div[2]'
                       '/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div/div/div')))
        ActionChains(self.driver).move_to_element(file_item).perform()
        #等待编辑图标出现
        edit_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app"]/section/main/section/main/div[2]/div/div/div/div[2]'
                       '/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div/div/div/div[1]/span[1]/span[2]')))
        edit_btn.click()
        #删除原本的会议名称
        file_input = self.driver.find_element(By.XPATH,'//*[@id="app"]/section/main/section/main/div[2]/div/div/div/div[2]/div[1]/div[1]'
                                                       '/div[3]/table/tbody/tr[2]/td[2]/div/div/div/div[1]/span[1]/div[1]/input')
        for i in range(len(file_input.get_attribute('value'))):
            file_input.send_keys(Keys.BACKSPACE)
        #空着直接保存，保存失败
        file_input.send_keys(Keys.ENTER)
        #输入新的会议名称
        file_input.send_keys(new_name)
        #不保存
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/main/section/main/div[2]/div/div/div/div[2]/div[1]/div[1]'
                                          '/div[3]/table/tbody/tr[2]/td[2]/div/div'
                                          '/div/div[1]/span[1]/div[2]/img[2]').click()
        #重新点击编辑
        file_item = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/section/main/section/main/div[2]/div/div/div/div[2]'
                       '/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div/div/div')))
        ActionChains(self.driver).move_to_element(file_item).perform()
        # 等待编辑图标出现
        edit_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app"]/section/main/section/main/div[2]/div/div/div/div[2]'
                       '/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div/div/div/div[1]/span[1]/span[2]')))
        edit_btn.click()
        # 删除原本的会议名称
        file_input = self.driver.find_element(By.XPATH,
                                              '//*[@id="app"]/section/main/section/main/div[2]/div/div/div/div[2]/div[1]/div[1]'
                                              '/div[3]/table/tbody/tr[2]/td[2]/div/div/div/div[1]/span[1]/div[1]/input')
        for i in range(len(file_input.get_attribute('value'))):
            file_input.send_keys(Keys.BACKSPACE)
        file_input.send_keys(new_name)
        file_input.send_keys(Keys.ENTER)


    #分享会议记录
    def share_transcription_record(self):
        #1.在列表页进行分享
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div'
                                          '/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[3]/div/i[1]').click()
        #todo 复制链接，新打开一个浏览器窗口，粘贴
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/main/section/main/div[2]/div/div/div'
                                          '/div[2]/div[1]/div[2]/div/div/div[2]/div[8]/button').click()
        time.sleep(2)
        #关闭分享窗口
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div'
                                          '/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[3]/div/i[1]').click()
        #2.进入会议记录详情分享
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/main/section/main/div[2]/div/div/div/div[2]/div[1]/div[1]'
                                          '/div[3]/table/tbody/tr[2]/td[2]/div/div/div/div[1]/span[1]/span[1]').click()
        #点击分享
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/main/section/main/div[2]'
                                          '/div/div/div[1]/div[3]/button').click()
        #点击复制链接
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/main/section/main/div[2]/div'
                                          '/div/div[1]/div[5]/div/div/div[2]/div[8]/button').click()
        #关闭分享窗口
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/main/section/main/div[2]/div'
                                          '/div/div[1]/div[5]/div/div/div[1]/button/i').click()
        #返回
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/main/section/main'
                                          '/div[2]/div/div/div[1]/div[1]/a/i').click()


    #下载转写记录、ai摘要、翻译、音频
    def download_transcription_record_files(self):
        #进入会议记录点击下载
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/main/section/main/div[2]/div/div/div'
                                          '/div[2]/div[1]/div[1]/div[3]/table/tbody'
                                          '/tr[2]/td[2]/div/div/div/div[1]/span[1]/span[1]').click()
        #点击下载
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/main/section'
                                          '/main/div[2]/div/div/div[1]/div[3]/span/span/span/span').click()
        #下载ai摘要
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]').click()
        #hover到更多
        file_item = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]')
        ActionChains(self.driver).move_to_element(file_item).perform()
        #下载转写记录
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]').click()
        #下载音频
        audio_download_btn = self.wait.wait_for_element_clickable(
            (By.XPATH, '/html/body/div[1]/div[1]/div[3]/div/div[1]'))
        audio_download_btn.click()
        #下载翻译
        translate_download_btn = self.wait.wait_for_element_clickable(
            (By.XPATH, '/html/body/div[1]/div[1]/div[3]/div/div[4]'))
        translate_download_btn.click()


    #删除会议记录（单个和批量删除），删除确认弹窗取消再确定
    def delete_transcription_record(self):
        pass


    #批量删除会议记录,未勾选不可点击，复选框点击再取消
    def delete_transcription_record_batch(self):
        pass
