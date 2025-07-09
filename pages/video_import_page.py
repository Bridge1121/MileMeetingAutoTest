import os
import time

from selenium.webdriver.common.by import By

from utils.wait_utils import WaitUtils
from utils.constant_parameters import *


class VideoImportPage:
    def __init__(self, driver):
        self.wait = WaitUtils(driver, 20)
        self.driver = driver

    #上传中文音频
    def upload_video_chinese(self,video_path=UPLOAD_FILE_PATH):
        if video_path!=None:
            #点击导入音频
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]').click()
            #点击选择音频文件
            # choose_btn = self.driver.find_element_by_xpath('/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[1]/text()')
            # choose_btn.click()
            # #打开文件
            # os.open(video_path)
            upload_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
            # 3. 直接传入文件路径（无需点击系统弹窗）
            upload_input.send_keys(video_path)

            #选择所有ai工具
            #主题摘要
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main'
                                              '/div[2]/article/div/div[1]/div/div/div[2]/div/'
                                              'div[2]/div[1]/div[2]/div/label[3]/span[1]/span').click()
            #语篇规整
            self.driver.find_element(By.XPATH,'//*[@id="app"]/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label[3]/span[1]/span').click()
            #代办信息
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label[4]/span[1]/span').click()
            #发言总结
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label[5]/span[1]/span').click()
            #QA整理
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label[6]/span[1]/span').click()
            time.sleep(10)
            # 等待上传完成
            self.wait.wait_for_element_clickable((By.XPATH,
                                                  '/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/footer/span[2]/div[2]'))
            self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/'
                                               'div[2]/article/div/div[1]/div/div/div[2]/footer/span[2]/div[2]').click()