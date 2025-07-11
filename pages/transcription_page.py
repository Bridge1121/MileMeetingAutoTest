import time

from selenium.webdriver import Keys, ActionChains

from utils.wait_utils import WaitUtils
from selenium.webdriver.common.by import By


class TranscriptionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver, 10)


    #点击允许使用麦克风权限
    def allow_mic_permission(self):
        time.sleep(1)
        ActionChains(self.driver).move_by_offset(636, 380).click().perform()

    #开始中文转写
    def start_transcription(self):
        # 开始实时转写
        self.driver.find_element(By.XPATH,
                                 '/html/body/section/section/main/section/main/div[2]'
                                 '/div/div/div[1]/div[2]/div[1]/div/div/div[1]').click()
        #修改麦克风
        self.driver.find_element(By.XPATH,'/html/body/section/div[12]/div/div[2]/div/div[2]/div[3]/div/div/div/div/div[1]/input').click()
        # 点击开始会议
        self.driver.find_element(By.XPATH, '/html/body/section/div[12]/div/div[2]/div/div[3]/button').click()
        time.sleep(5)
        # 点击允许使用麦克风
        # ActionChains(self.driver).move_by_offset(636, 380).click().perform()


    #开始英文转写
    def start_transcription_english(self):
        # 启动英文转写
        self.driver.find_element(By.XPATH,
                                 '/html/body/section/section/main/section/main'
                                 '/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[1]').click()
        #语言修改成英文
        self.driver.find_element(By.XPATH,'/html/body/section/div[12]/div/div[2]'
                                          '/div/div[2]/div[2]/div/div[1]/div'
                                          '/div[1]/span/span/i').click()
        #选择中英混合
        self.driver.find_element(By.XPATH,'/html/body/section/div[12]/div/div[2]/div'
                                          '/div[2]/div[2]/div/div[1]/div/div[2]/div[1]'
                                          '/div[1]/ul/li[2]/span').click()
        # 点击开始会议
        self.driver.find_element(By.XPATH, '/html/body/section/div[12]/div/div[2]/div/div[3]/button').click()
        time.sleep(5)


    #修改会议设置
    def modify_meeting_setting(self):
        #实时转写时点击设置
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/header/div[2]/span[2]/img').click()
        #点击选择麦克风
        # self.driver.find_element(By.XPATH,'/html/body/section/div[12]/div/div[2]/div/div[2]/div/div[1]/input').click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li').click()
        time.sleep(2)
        #确认修改
        self.driver.find_element(By.XPATH,'/html/body/section/div[12]/div/div[2]/div/div[3]/button').click()


    #暂停会议
    def pause_meeting(self,pause_interval=10):
        #点击暂停
        self.driver.find_element(By.CLASS_NAME,'button-pause').click()
        time.sleep(pause_interval)

    #继续会议
    def resume_meeting(self):
        self.driver.find_element(By.CLASS_NAME,'button-resume').click()


    #结束会议
    def end_meeting(self):
        time.sleep(2)
        #点击结束
        self.driver.find_element(By.CLASS_NAME,'stop-button').click()
        time.sleep(2)
        #点击弹窗结束
        self.driver.find_element(By.XPATH,'/html/body/div/div/div[3]/button[2]').click()
        time.sleep(5)


    #语气词过滤默认勾选状态
    def close_modal_particles(self):
        #关闭语气词过滤
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/label/span/span').click()

    #打开手动区分发言人
    def open_manual_speaker_distinguish(self):
        #点击下拉框
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/div[1]/div[1]/div[1]/span[1]/div/div[1]/span/span/i').click()
        time.sleep(4)
        #选择手动区分发言人
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        time.sleep(2)

    #不区分发言人
    def close_speaker_distinguish(self):
        #点击下拉框
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/div[1]/div[1]/div[1]/span[1]/div/div/span/span/i').click()
        time.sleep(4)
        #选择不区分发言人
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()

    #打开声纹区分发言人
    def open_voice_print_speaker_distinguish(self):
        # 点击下拉框
        self.driver.find_element(By.XPATH,
                                 '/html/body/section/section/main/section/main/div[2]/div/div/div/div[1]/div[1]/div[1]/span[1]/div/div/span/span/i').click()
        time.sleep(4)
        # 选择声纹区分发言人
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[3]').click()


    #修改手动区分发言人名称
    def modify_manual_speaker_name(self,new_name="测试修改"):
        #点击发言人
        speaker_name = self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[1]/div/section/div/ul/li[1]/span[2]')
        speaker_name.click()
        #删除
        for i in range(len(speaker_name.text)):
            speaker_name.send_keys(Keys.BACKSPACE)
        #输入新的说话人名称
        speaker_name.send_keys(new_name)

        speaker_name.send_keys(Keys.ENTER)

    # 修改手动区分发言人名称
    def modify_manual_speaker_name_ch_en_num(self, new_name="测试twx123"):
        # 点击发言人
        speaker_name = self.driver.find_element(By.XPATH,
                                                '/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[1]/div/section/div/ul/li[2]/span[2]')
        speaker_name.click()
        # 删除
        for i in range(len(speaker_name.text)):
            speaker_name.send_keys(Keys.BACKSPACE)
        # 输入新的说话人名称
        speaker_name.send_keys(new_name)
        speaker_name.send_keys(Keys.ENTER)

    # 修改手动区分发言人名称为特殊符号
    def modify_manual_speaker_name_special_symbols(self, new_name="#*(^!"):
        # 点击发言人
        speaker_name = self.driver.find_element(By.XPATH,
                                                '/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[1]/div/section/div/ul/li[3]/span[2]')
        speaker_name.click()
        # 删除
        for i in range(len(speaker_name.text)):
            speaker_name.send_keys(Keys.BACKSPACE)
        # 输入新的说话人名称
        speaker_name.send_keys(new_name)
        speaker_name.send_keys(Keys.ENTER)


    #添加已有声纹的发言人
    def add_voice_print_speaker(self,voice_print_name="twx"):
        #点击去添加
        self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[1]/div/section/div/button/span').click()
        #搜索框输入发言人名称
        self.driver.find_element(By.CLASS_NAME,'el-select el-select--small').send_keys(voice_print_name)
        #选择搜索到的内容
        self.driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li').click()


    #修改会议标题为空失败，继续输入新标题
    def modify_meeting_title_null(self,new_title="测试修改会议标题"):
        #点击会议标题修改图标
        edit_icon = self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/header/div[1]/div/div/div/i')
        edit_icon.click()
        #会议标题文本框
        input = self.driver.find_element(By.XPATH,
                                         '/html/body/section/section/main/section/main/div[2]/div/div/div/header/div[1]/div/div/div/form/div/div/div/input')
        time.sleep(2)

        #未修改直接保存
        input.send_keys(Keys.ENTER)
        self.wait.wait_for_element_clickable((By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/header/div[1]/div/div/div/i'))
        #再次点击修改
        edit_icon.click()
        for i in range(len(input.get_attribute("value"))):
            input.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        input.send_keys(Keys.ENTER)
        #输入新标题
        input.send_keys(new_title)
        time.sleep(2)
        input.send_keys(Keys.ENTER)

    #修改会议标题
    def modify_title(self, new_title="测试重复标题"):
        # 点击会议标题修改图标
        edit_icon = self.driver.find_element(By.XPATH,
                                             '/html/body/section/section/main/section/main/div[2]/div/div/div/header/div[1]/div/div/div/i')
        edit_icon.click()
        input = self.driver.find_element(By.XPATH,
                                         '/html/body/section/section/main/section/main/div[2]/div/div/div/header/div[1]/div/div/div/form/div/div/div/input')
        # 会议标题文本框
        for i in range(len(input.get_attribute("value"))):
            input.send_keys(Keys.BACKSPACE)
        # 输入新标题
        input.send_keys(new_title)
        input.send_keys(Keys.ENTER)


    #修改会议标题不保存
    def modify_title_not_save(self, new_title="测试重复标题"):
        # 点击会议标题修改图标
        edit_icon = self.driver.find_element(By.XPATH,
                                             '/html/body/section/section/main/section/main/div[2]/div/div/div/header/div[1]/div/div/div/i')
        edit_icon.click()
        # 会议标题文本框
        input = self.driver.find_element(By.XPATH,
                                         '/html/body/section/section/main/section/main/div[2]/div/div/div/header/div[1]/div/div/div/form/div/div/div/input')
        for i in range(len(input.get_attribute("value"))):
            input.send_keys(Keys.BACKSPACE)
        # 输入新标题
        input.send_keys(new_title)
        #不保存
        cancel_button = self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/header/div[1]/div/div/div/svg[2]/use')
        cancel_button.click()


    #修改会议标题为中英、数字、特殊字符
    def modify_meeting_title_ch_en_special_symbols(self,new_title="测Aa1@&试"):
        #点击会议标题修改图标
        edit_icon = self.driver.find_element(By.XPATH,'/html/body/section/section/main/section/main/div[2]/div/div/div/header/div[1]/div/div/div/i')
        edit_icon.click()
        #会议标题文本框
        input = self.driver.find_element(By.XPATH,
                                         '/html/body/section/section/main/section/main/div[2]/div/div/div/header/div[1]/div/div/div/form/div/div/div/input')
        for i in range(len(input.get_attribute("value"))):
            input.send_keys(Keys.BACKSPACE)
        #输入新标题
        input.send_keys(new_title)
        input.send_keys(Keys.ENTER)


    #修改会议标题，输入1个和15个字符
    def modify_meeting_title_fifteen_characters(self,new_title="abc12345bewis测试"):
        # 点击会议标题修改图标
        edit_icon = self.driver.find_element(By.XPATH,
                                             '//*[@id="app"]/section/main/section/main/div[2]/div/div/div/header/div[1]/div/div/div/i')
        edit_icon.click()
        # 会议标题文本框
        input = self.driver.find_element(By.XPATH,
                                         '/html/body/section/section/main/section/main/div[2]/div/div/div/header/div[1]/div/div/div/form/div/div/div/input')
        time.sleep(2)
        for i in range(len(input.get_attribute("value"))):
            input.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        # 输入1个字符，保存
        # input.send_keys('一')
        # input.send_keys(Keys.ENTER)
        # time.sleep(5)
        # #再次点击修改
        # edit_icon.click()
        # time.sleep(2)
        # input.send_keys(Keys.BACKSPACE)
        # time.sleep(2)
        #输入15个字符，点击保存
        input.send_keys("中文123new_title")
        time.sleep(2)
        input.send_keys(Keys.ENTER)
        time.sleep(2)


    #修改转写内容
    def modify_transcription_content(self, new_content="一二三"):
        text = self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/p[2]/span[1]/span[1]')
        text.send_keys(new_content)
        time.sleep(5)


    #下载转写记录
    def download_transcription_record(self):
        download_btn = self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/div[2]/div/div/div[1]/div[3]/span/span/span/span')
        download_btn.click()
        #下载转写记录
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]').click()


    #编辑会议纪要
    def edit_meeting_summary(self):
        if self.driver.find_element(By.XPATH, '//*[@id="tinymce"]/p[2]/strong'):
            text_input = self.driver.find_element(By.XPATH, '//*[@id="tinymce"]/p[1]')
            text_input.click()
            time.sleep(2)
            text_input.send_keys('测试修改会议纪要')
            time.sleep(2)

    #下载会议纪要
    def download_meeting_summary(self):
        download_btn = self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main/div[2]/div/div/div[1]/div[3]/span/span/span/span')
        download_btn.click()
        #点击更多
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]').click()
        #点击会议纪要
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[3]').click()


    #添加热词
    def add_hot_word(self,word):
        time.sleep(2)
        #点击专有词汇
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/main/section/main/div[2]/div/div'
                                           '/div/div[1]/div[1]/div[1]/div[2]/div[2]').click()
        #判断是否有添加热词按钮
        # if self.wait.wait_for_element_clickable((By.XPATH, '/html/body/section/section/main/section/main/div[2]'
        #                                                    '/div/div/div/div[1]/div[3]/div[1]/div/div[2]'
        #                                                    '/div/div/div/div/div[2]/div/button/span')):
        #     self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main'
        #                                        '/div[2]/div/div/div/div[1]/div[3]/div[1]/div/div[2]'
        #                                        '/div/div/div/div/div[2]/div/button/span').click()
        # else:
        #点击管理热词
        self.driver.find_element(By.XPATH, '/html/body/section/section/main'
                                           '/section/main/div[2]/div/div/div/div[1]/div[3]/div[1]'
                                           '/div/div[2]/div/div/div/div/div[1]/button/span').click()
        #输入热词
        hot_word_text = self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main'
                                           '/div[2]/div/div/div/div[1]/div[3]/div[1]/div'
                                           '/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]'
                                           '/div[1]/div/div[1]/textarea')
        hot_word_text.send_keys(word)
        #点击保存
        self.driver.find_element(By.XPATH, '/html/body/section/section'
                                           '/main/section/main/div[2]/div/div/div'
                                           '/div[1]/div[3]/div[1]/div/div[2]/div/div/div'
                                           '/div/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div/button[2]').click()
        time.sleep(2)
        #弹窗点击确定
        confirm_btn = self.driver.find_element(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small')
        self.wait.wait_for_element_visible((By.CSS_SELECTOR, 'body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small'))
        # self.wait.wait_for_element_visible((By.XPATH, '/html/body/div[3]/div/div/div/div[3]/button[2]'))
        # confirm_btn = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/span/button[2]')
        ActionChains(self.driver).move_to_element(confirm_btn).click().perform()
        time.sleep(4)
        #关闭对话框
        self.driver.find_element(By.XPATH, '/html/body/section/section/main/section/main'
                                           '/div[2]/div/div/div/div[1]/div[3]/div[1]/div/div[1]/button/i').click()




