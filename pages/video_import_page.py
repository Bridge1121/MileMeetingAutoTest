import os
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from utils.wait_utils import WaitUtils
from utils.constant_parameters import *


class VideoImportPage:
    def __init__(self, driver):
        self.wait = WaitUtils(driver, 60)
        self.driver = driver

    # 批量上传视频文件，清空文件
    def upload_all_video_files_and_clear(self, video_dir_path=UPLOAD_VIDEO_DIR, video_suffixes=VIDEO_SUFFIXES):
        count = 0
        for filename in os.listdir(video_dir_path):
            if filename.lower().endswith(video_suffixes):
                if count>=10:
                    break
                file_path = os.path.join(video_dir_path, filename)
                count=count+1
                print(f"🔄 正在上传：{file_path}")
                upload_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
                # 3. 直接传入文件路径（无需点击系统弹窗）
                upload_input.send_keys(file_path)
        #点击删除单个文件
        self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div'
                                           '/div[1]/div[3]/table/tbody/tr[2]/td[3]/div/div/i[1]').click()
        # 等待上传完成
        time.sleep(UPLOAD_INTERVAL)
        # 清空文件
        self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/div[2]/article'
                                           '/div/div[1]/div/div/div[2]/footer/span[2]/div[1]').click()
        time.sleep(2)

    # 批量上传音频文件，清空文件
    def upload_all_audio_files_and_clear(self, audio_dir_path=UPLOAD_VIDEO_DIR, audio_suffixes=VIDEO_SUFFIXES):
        count = 0
        for filename in os.listdir(audio_dir_path):
            if filename.lower().endswith(audio_suffixes):
                if count >= 10:
                    break
                file_path = os.path.join(audio_dir_path, filename)
                count = count + 1
                print(f"🔄 正在上传：{file_path}")
                upload_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
                # 3. 直接传入文件路径（无需点击系统弹窗）
                upload_input.send_keys(file_path)
        # 点击删除单个文件
        self.driver.find_element(By.XPATH,
                                 '/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div'
                                 '/div[1]/div[3]/table/tbody/tr[2]/td[3]/div/div/i[1]').click()
        # 等待上传完成
        time.sleep(UPLOAD_INTERVAL)
        # 清空文件
        self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/div[2]/article'
                                           '/div/div[1]/div/div/div[2]/footer/span[2]/div[1]').click()
        time.sleep(2)

    #上传中文音频，输入热词
    def upload_video_chinese(self,video_path=UPLOAD_CH_FILE_PATH):
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
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label[3]/span[1]/span').click()
            time.sleep(2)
            #代办信息
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label[4]/span[1]/span').click()
            #发言总结
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label[5]/span[1]/span').click()
            #QA整理
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label[6]/span[1]/span').click()
            time.sleep(UPLOAD_INTERVAL)
            #输入热词
            self.driver.find_element(By.XPATH,'//*[@id="app"]/section/main/section/main/div[2]/article'
                                              '/div/div[1]/div/div/div[2]/div/div[2]'
                                              '/div[1]/div[3]/div/div/input').send_keys("打野")
            # 等待上传完成
            self.wait.wait_for_element_clickable((By.XPATH,
                                                  '/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/footer/span[2]/div[2]'))
            self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/'
                                               'div[2]/article/div/div[1]/div/div/div[2]/footer/span[2]/div[2]').click()
            time.sleep(10)
            #点击会议记录
            self.wait.wait_for_element_clickable((By.XPATH,
                                                  '/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]'
                                                  '/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div[1]/span[1]/span[1]'))
            self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]'
                                              '/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div[1]/span[1]/span[1]').click()
            #查看会议纪要
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div[3]/div[2]'
                                              '/div/div[1]/div/div[1]/div/div/div/div[3]/span').click()
            #返回列表页
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]'
                                              '/div/div/div[1]/div[1]/a/i').click()
            time.sleep(2)

    #上传英文音频
    def upload_video_english(self,video_path=UPLOAD_EH_FILE_PATH):
        if video_path!=None:
            #点击导入音频
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]'
                                              '/div/div/div[1]/div[2]/div[2]/div/div/div[1]').click()
            #选择英文
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]'
                                              '/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]'
                                              '/div[1]/div/div[4]/div').click()
            time.sleep(2)
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
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]'
                                              '/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]'
                                              '/div[2]/div/label[3]/span[1]/span').click()
            time.sleep(2)
            #代办信息
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]'
                                              '/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]'
                                              '/div[2]/div/label[4]/span[1]/span').click()
            #发言总结
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]'
                                              '/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]'
                                              '/div[2]/div/label[5]/span[1]/span').click()
            #QA整理
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main'
                                              '/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]'
                                              '/div[1]/div[2]/div/label[6]/span[1]/span').click()
            time.sleep(UPLOAD_INTERVAL)
            # 等待上传完成
            self.wait.wait_for_element_clickable((By.XPATH,
                                                  '/html/body/section/section/main/section/main/div[2]'
                                                  '/article/div/div[1]/div/div/div[2]/footer/span[2]/div[2]'))
            self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/'
                                               'div[2]/article/div/div[1]/div/div/div[2]/footer/span[2]/div[2]').click()


    #上传粤语音频
    def upload_video_yuewen(self,video_path=UPLOAD_YY_FILE_PATH):
        if video_path!=None:
            #点击导入音频
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]'
                                              '/div/div/div[1]/div[2]/div[2]/div/div/div[1]').click()
            #选择粤语
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]'
                                              '/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]'
                                              '/div[1]/div/div[2]/div').click()
            time.sleep(2)
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
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]'
                                              '/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]'
                                              '/div[2]/div/label[3]/span[1]/span').click()
            time.sleep(2)
            #代办信息
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]'
                                              '/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]'
                                              '/div[2]/div/label[4]/span[1]/span').click()
            #发言总结
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]'
                                              '/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]'
                                              '/div[2]/div/label[5]/span[1]/span').click()
            #QA整理
            self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main'
                                              '/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]'
                                              '/div[1]/div[2]/div/label[6]/span[1]/span').click()
            time.sleep(UPLOAD_INTERVAL)
            # 等待上传完成
            self.wait.wait_for_element_clickable((By.XPATH,
                                                  '/html/body/section/section/main/section/main/div[2]'
                                                  '/article/div/div[1]/div/div/div[2]/footer/span[2]/div[2]'))
            self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/'
                                               'div[2]/article/div/div[1]/div/div/div[2]/footer/span[2]/div[2]').click()

    # 上传四川话音频
    def upload_video_sichuan(self, video_path=UPLOAD_SC_FILE_PATH):
        if video_path != None:
            # 点击导入音频
            self.driver.find_element(By.XPATH,
                                     '/html/body/section/section/main/section/main/div[2]/div/div'
                                     '/div[1]/div[2]/div[2]/div/div/div[1]').click()
            #点击选择四川话
            self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main'
                                               '/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]'
                                               '/div[1]/div[1]/div/div[3]/div').click()
            # 点击选择音频文件
            # choose_btn = self.driver.find_element_by_xpath('/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[1]/text()')
            # choose_btn.click()
            # #打开文件
            # os.open(video_path)
            upload_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
            # 3. 直接传入文件路径（无需点击系统弹窗）
            upload_input.send_keys(video_path)

            # 选择所有ai工具
            # 主题摘要
            self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main'
                                               '/div[2]/article/div/div[1]/div/div/div[2]/div/'
                                               'div[2]/div[1]/div[2]/div/label[3]/span[1]/span').click()
            # 语篇规整
            self.driver.find_element(By.XPATH,
                                     '/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label[3]/span[1]/span').click()
            time.sleep(2)
            # 代办信息
            self.driver.find_element(By.XPATH,
                                     '/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label[4]/span[1]/span').click()
            # 发言总结
            self.driver.find_element(By.XPATH,
                                     '/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label[5]/span[1]/span').click()
            # QA整理
            self.driver.find_element(By.XPATH,
                                     '/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/label[6]/span[1]/span').click()
            time.sleep(UPLOAD_INTERVAL)
            # 等待上传完成
            self.wait.wait_for_element_clickable((By.XPATH,
                                                  '/html/body/section/section/main/section/main/div[2]/article/div/div[1]/div/div/div[2]/footer/span[2]/div[2]'))
            self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/'
                                               'div[2]/article/div/div[1]/div/div/div[2]/footer/span[2]/div[2]').click()


    #上传文件时输入热词
    def input_hot_word_while_upload(self, hot_word):
        # 输入热词
        hot_word_input = self.driver.find_element(By.XPATH, '//*[@id="app"]/section/main/section/main/div[2]/article'
                                           '/div/div[1]/div/div/div[2]/div/div[2]'
                                           '/div[1]/div[3]/div/div/input')
        hot_word_input.send_keys(hot_word)
        #删除输入的热词
        for i in range(len(hot_word)):
            hot_word_input.send_keys(Keys.BACKSPACE)






