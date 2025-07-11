import time

import allure
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.transcription_page import TranscriptionPage
from utils.wait_utils import WaitUtils

@allure.feature("实时转写功能")
@pytest.mark.usefixtures("driver")
class TestATranscription:


    @allure.story("点击开始会议记录")
    @allure.feature("点击开始会议记录后进入实时转写页面,音频录音中，点击【暂停】按钮，录音暂停,点击【结束】显示结束录音提示弹窗")
    @allure.title("点击开始会议记录后进入实时转写页面,音频录音中，点击【暂停】按钮，录音暂停,点击【结束】显示结束录音提示弹窗")
    @pytest.mark.order(1)
    def test_transcription_start_pause_end(self,driver):
        # 单独运行要加这两行
        login = LoginPage(driver)
        login.open()
        login.login()
        #返回到首页
        home = HomePage(driver)
        home.back_home()
        trans = TranscriptionPage(driver)
        #开始转写
        trans.start_transcription_english()
        trans.allow_mic_permission()
        #暂停转写
        trans.pause_meeting()
        time.sleep(5)
        #继续转写
        trans.resume_meeting()
        #录音1分钟后暂停转写
        time.sleep(5)
        #点击暂停
        trans.pause_meeting()
        time.sleep(5)
        #结束会议
        trans.end_meeting()

    @allure.story("实时转写中添加热词")
    @allure.feature("实时转写中添加热词")
    @allure.title("实时转写中添加热词")
    # @pytest.mark.skip(reason="保存按钮不可点击")
    def test_transcription_add_hot_word(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        #返回到首页
        home = HomePage(driver)
        home.back_home()
        trans = TranscriptionPage(driver)
        #开始转写
        trans.start_transcription()
        time.sleep(10)
        #添加热词
        trans.add_hot_word("好困")
        trans.add_hot_word("都是分开的是解放军的")
        trans.add_hot_word("cssdf")
        trans.add_hot_word("SFDFSD")
        trans.add_hot_word("SFDdf华国")
        #结束会议
        trans.end_meeting()


    @allure.story("切换麦克风")
    @allure.feature(
        "实时转写页面点击麦克风图标，弹窗显示当前正在拾音的麦克风和扬声器。点击默认的音源设备名称可下拉选择其他的音源设备")
    @allure.title(
        "实时转写页面点击麦克风图标，弹窗显示当前正在拾音的麦克风和扬声器。点击默认的音源设备名称可下拉选择其他的音源设备")
    def test_transcription_switch_microphone(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        #返回到首页
        home = HomePage(driver)
        home.back_home()
        trans = TranscriptionPage(driver)
        #开始转写
        trans.start_transcription()
        time.sleep(5)
        #点击设置
        trans.modify_meeting_setting()
        #结束会议
        trans.end_meeting()

    @allure.story("实时转写语气词过滤")
    @allure.feature(
        "语气词过滤默认勾选状态，转写过程中，关闭语气词过滤，语气词过滤开关仅对本条记录生效")
    @allure.title(
        "语气词过滤默认勾选状态，转写过程中，关闭语气词过滤，语气词过滤开关仅对本条记录生效")
    def test_transcription_filter_noise(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        #返回到首页
        home = HomePage(driver)
        home.back_home()
        trans = TranscriptionPage(driver)
        trans.start_transcription()
        #关闭语气词过滤开关
        trans.close_modal_particles()
        time.sleep(2)
        #结束会议
        trans.end_meeting()

    @allure.story("手动区分发言人")
    @allure.feature(
        "转写过程关闭区分发言人开关之后，再开启的新转写区分发言人开关默认是关闭状态，发言人区分后，点击发言人姓名时，切换为可编辑状态，可以编辑后保存")
    @allure.title(
        "转写过程关闭区分发言人开关之后，再开启的新转写区分发言人开关默认是关闭状态，发言人区分后，点击发言人姓名时，切换为可编辑状态，可以编辑后保存")
    @pytest.mark.skip(reason="")
    def test_mannual_speaker_distinguish_and_edit(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        #首先返回到首页
        home = HomePage(driver)
        home.back_home()
        trans = TranscriptionPage(driver)
        #开始转写
        trans.start_transcription()
        trans.open_manual_speaker_distinguish()
        trans.close_speaker_distinguish()
        #打开手动区分发言人
        trans.open_manual_speaker_distinguish()
        time.sleep(2)
        #修改发言人名称
        trans.modify_manual_speaker_name("测试发言人修改")
        time.sleep(2)
        #修改发言人长度校验
        #中英文数字组合
        trans.modify_manual_speaker_name_ch_en_num()
        time.sleep(2)
        #特殊符号
        trans.modify_manual_speaker_name_special_symbols()
        #结束会议
        trans.end_meeting()

    @allure.story("声纹区分发言人")
    @allure.feature(
        "打开声纹区分发言人，添加已有声纹的发言人，关闭声纹区分发言人，结束会议")
    @allure.title(
        "打开声纹区分发言人，添加已有声纹的发言人，关闭声纹区分发言人，结束会议")
    @pytest.mark.skip(reason="声纹区分发言人功能已删除")
    def test_voice_print_speaker_distinguish(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        #首先返回到首页
        home = HomePage(driver)
        home.back_home()
        trans = TranscriptionPage(driver)
        #开始转写
        trans.start_transcription()
        trans.open_voice_print_speaker_distinguish()
        #添加已有声纹的发言人
        # trans.add_voice_print_speaker()
        # time.sleep(2)
        # trans.close_speaker_distinguish()
        # #关闭声纹区分发言人
        # trans.close_voice_print_speaker_distinguish()
        #结束会议
        trans.end_meeting()

    @allure.story("会议标题编辑，格式校验")
    @allure.feature(
        "实时转写页左上角显示文件名，点击重命名图标，可进入重命名编辑状态，未修改文件名，保存文件名，文件名长度校验")
    @allure.title(
        "实时转写页左上角显示文件名，点击重命名图标，可进入重命名编辑状态，未修改文件名，保存文件名，文件名长度校验")
    def test_transcription_title_edit(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        home = HomePage(driver)
        home.back_home()
        trans = TranscriptionPage(driver)
        trans.start_transcription()
        #修改会议标题
        #长度校验
        trans.modify_meeting_title_fifteen_characters()
        time.sleep(2)
        # trans.modify_meeting_title_null()
        #结束会议
        trans.end_meeting()

    @allure.story("会议标题编辑为已存在的会议标题，修改后取消保存")
    @allure.feature(
        "修改为已存在的记录文件名，修改文件名后取消保存")
    @allure.title(
        "修改为已存在的记录文件名，修改文件名后取消保存")
    def test_transcription_meeting_title_edit_cancel(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        home = HomePage(driver)
        home.back_home()
        trans = TranscriptionPage(driver)
        trans.start_transcription()
        #修改会议标题
        trans.modify_title()
        #结束会议
        trans.end_meeting()
        #回到首页
        home.back_home()
        #重新开会
        trans.start_transcription()
        # 修改名称不保存
        # trans.modify_title_not_save()
        #修改为已存在的名称
        trans.modify_title()
        time.sleep(2)
        #结束会议
        trans.end_meeting()

    @allure.story("实时转写过程中编辑转写内容，结束会议并下载")
    @allure.feature(
        "新增内容后，结束会议后显示修改后的内容（退出编辑5秒后才能保存成功）,转写内容做了增加，结束会议后，下载下来的文稿显示新增的内容")
    @allure.title(
        "新增内容后，结束会议后显示修改后的内容（退出编辑5秒后才能保存成功）,转写内容做了增加，结束会议后，下载下来的文稿显示新增的内容")
    def test_add_content_and_end_meeting_and_show_new_content(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        #首页
        home = HomePage(driver)
        home.back_home()
        trans = TranscriptionPage(driver)
        trans.start_transcription()
        time.sleep(5)
        #修改转写内容
        trans.modify_transcription_content()
        #结束会议
        trans.end_meeting()
        #下载转写记录
        trans.download_transcription_record()

    @allure.story("会议纪要编辑")
    @allure.feature(
        "实时转写中，点击【纪要】图标展开编辑栏，实时转写暂停时，点击【纪要】展开编辑栏，转写中，写入纪要，自动保存成功，本次纪要内容不保存至下一条实时转写记录内")
    @allure.title(
        "实时转写中，点击【纪要】图标展开编辑栏，实时转写暂停时，点击【纪要】展开编辑栏，转写中，写入纪要，自动保存成功，本次纪要内容不保存至下一条实时转写记录内")
    def test_transcription_write_summary_save_success_and_not_save_to_next_transcription_record(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        #回到首页
        home_page = HomePage(driver)
        home_page.back_home()
        #开始转写
        trans = TranscriptionPage(driver)
        trans.start_transcription()
        time.sleep(3)
        #编辑会议纪要
        # trans.edit_meeting_summary()
        #结束会议
        trans.end_meeting()
        #下载会议纪要
        trans.download_meeting_summary()


