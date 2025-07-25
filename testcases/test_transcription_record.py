import time

import allure
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.transcription_page import TranscriptionPage
from pages.transcription_record_page import TranscriptionRecordPage


@allure.feature("转写记录列表")
@pytest.mark.usefixtures("driver")
class TestTranscriptionRecord:

    @allure.story("转写记录页面布局样式正常，文案内容正确")
    @allure.title("转写记录页面布局样式正常，文案内容正确")
    @allure.feature("转写记录页面布局样式正常，文案内容正确")
    @pytest.mark.order(1)
    def test_transcription_record_layout_and_search(self, driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        trans_record = TranscriptionRecordPage(driver)
        #点击会议记录
        trans_record.open_transcription_record()

        #搜索记录
        trans_record.search_transcription_record_click_and_back()


    @allure.story("转写记录分页设置")
    @allure.title("切换每页显示的条数，列表同步刷新当前页显示正确的条数，切换具体的页码数，会跳转到对应的页数，"
                  "展示当前页的记录，点击左右切换箭头>和<，可翻到上一页，下一页，翻页后，从详情页回到列表页，列表记录回到上次浏览停留的位置")
    @allure.feature("切换每页显示的条数，列表同步刷新当前页显示正确的条数，切换具体的页码数，会跳转到对应的页数，"
                  "展示当前页的记录，点击左右切换箭头>和<，可翻到上一页，下一页，翻页后，从详情页回到列表页，列表记录回到上次浏览停留的位置")
    @pytest.mark.order(2)
    def test_transcription_record_page_switch_page_size(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        trans_record = TranscriptionRecordPage(driver)
        #点击会议记录
        trans_record.open_transcription_record()
        #修改分页设置
        trans_record.modify_page_setting()

    @allure.story("会议记录分享")
    @allure.title("在历史记录列表中选中会议记录点击分享按钮，会弹出分享弹框，复制分享链接")
    @allure.feature("在历史记录列表中选中会议记录点击分享按钮，会弹出分享弹框，复制分享链接")
    @pytest.mark.order(3)
    def test_transcription_record_share(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        trans_record = TranscriptionRecordPage(driver)
        #点击会议记录
        trans_record.open_transcription_record()
        #分享会议记录
        trans_record.share_transcription_record()

    @allure.story("会议记录下载")
    @allure.title("点击下载按钮，弹出下载弹窗，下载音频，下载会议纪要、翻译、ai摘要")
    @allure.feature("点击下载按钮，弹出下载弹窗，下载音频，下载会议纪要、翻译、ai摘要")
    @pytest.mark.order(4)
    def test_transcription_record_download(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        trans_record = TranscriptionRecordPage(driver)
        #点击会议记录
        trans_record.open_transcription_record()
        #下载会议记录
        trans_record.download_transcription_record_files()

    @allure.story("会议记录删除")
    @allure.title("单个记录删除取消再确认，批量删除取消再确认")
    @allure.feature("单个记录删除取消再确认，批量删除取消再确认")
    @pytest.mark.order(5)
    def test_transcription_record_delete(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        trans_record = TranscriptionRecordPage(driver)
        #点击会议记录
        trans_record.open_transcription_record()
        #删除会议记录
        trans_record.delete_transcription_record()
        time.sleep(2)
        # trans_record.delete_transcription_record_batch()

    @allure.story("会议记录语篇规整")
    @allure.title("不满一分钟的记录，提示无法进行语篇规整")
    @allure.feature("不满一分钟的记录，提示无法进行语篇规整")
    @pytest.mark.order(6)
    def test_transcription_record_less_one_minute_speech_regulation(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        #开始实时转写
        transcription = TranscriptionPage(driver)
        transcription.start_transcription()
        time.sleep(10)
        #点击结束
        transcription.end_meeting()
        time.sleep(20)
        trans_record = TranscriptionRecordPage(driver)
        #点击语篇规整
        trans_record.click_speech_regulation()

    @allure.story("会议记录语篇规整")
    @allure.title("一分钟以上的记录，进行语篇规整")
    @allure.feature("一分钟以上的记录，进行语篇规整")
    @pytest.mark.order(7)
    def test_transcription_record_speech_regulation(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        # 开始实时转写
        # transcription = TranscriptionPage(driver)
        # transcription.start_transcription()
        # time.sleep(65)
        # # 点击结束
        # transcription.end_meeting()
        # time.sleep(10)
        #点开第一条会议记录
        trans_record = TranscriptionRecordPage(driver)
        trans_record.open_transcription_record()
        trans_record.open_transcription_record_click()
        # 点击查找
        # trans_record.find_transcription_content("你")
        # time.sleep(2)
        #区分发言人
        # trans_record.click_distinguish_speaker()
        #生成会议纪要
        # trans_record.click_one_key_summary()
        # trans_record.click_translation()
        # 点击语篇规整
        trans_record.click_speech_regulation()

    @allure.story("会议记录翻译")
    @allure.title("会议记录翻译")
    @allure.feature("会议记录翻译")
    @pytest.mark.order(8)
    def test_transcription_record_translation(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        time.sleep(2)
        trans_record = TranscriptionRecordPage(driver)
        trans_record.open_transcription_record()
        trans_record.open_transcription_record_click()
        trans_record.click_translation()



    @allure.story("会议记录区分发言人")
    @allure.title("区分发言人")
    @allure.feature("区分发言人")
    @pytest.mark.order(9)
    def test_transcription_record_distinguish_speaker(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        time.sleep(10)
        trans_record = TranscriptionRecordPage(driver)
        trans_record.open_transcription_record()
        trans_record.open_transcription_record_click()
        trans_record.click_distinguish_speaker()


    





