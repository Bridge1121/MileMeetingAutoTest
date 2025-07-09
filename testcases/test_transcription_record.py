import allure
import pytest

from pages.home_page import HomePage
from pages.transcription_record_page import TranscriptionRecordPage


@allure.feature("转写记录")
@pytest.mark.usefixtures("driver")
class TestTranscriptionRecord:

    @allure.story("转写记录页面布局样式正常，文案内容正确")
    @allure.title("转写记录页面布局样式正常，文案内容正确")
    @allure.feature("转写记录页面布局样式正常，文案内容正确")
    def test_transcription_record_layout(self, driver):
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
    def test_transcription_record_page_switch_page_size(self):
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        trans_record = TranscriptionRecordPage(driver)
        #点击会议记录
        trans_record.open_transcription_record()
        #修改分页设置
        trans_record.modify_page_setting()




