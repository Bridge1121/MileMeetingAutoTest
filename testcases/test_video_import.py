import allure
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.video_import_page import VideoImportPage


@allure.feature("测试导入音视频")
@pytest.mark.usefixtures("driver")
class TestVideoImport:

    @allure.story("导入中文音频，AI工具全选")
    @allure.title("导入中文音频，AI工具全选")
    @allure.feature("导入中文音频，AI工具全选")
    @pytest.mark.order(1)
    def test_cn_video_upload(self, driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        home_page = HomePage(driver)
        home_page.back_home()
        #导入中文音频
        video_import_page = VideoImportPage(driver)
        video_import_page.upload_video_chinese()

    @allure.story("导入英文音频，AI工具全选")
    @allure.title("导入英文音频，AI工具全选")
    @allure.feature("导入英文音频，AI工具全选")
    def test_en_video_upload(self, driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        home_page = HomePage(driver)
        home_page.back_home()
        # 导入英文音频
        video_import_page = VideoImportPage(driver)
        video_import_page.upload_video_english()

    @allure.story("导入粤语音频，AI工具全选")
    @allure.title("导入粤语音频，AI工具全选")
    @allure.feature("导入粤语音频，AI工具全选")
    def test_yy_video_upload(self, driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        home_page = HomePage(driver)
        home_page.back_home()
        # 导入粤语音频
        video_import_page = VideoImportPage(driver)
        video_import_page.upload_video_yuewen()

    @allure.story("导入四川话音频，AI工具全选")
    @allure.title("导入四川话音频，AI工具全选")
    @allure.feature("导入四川话音频，AI工具全选")
    def test_sc_video_upload(self, driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        home_page = HomePage(driver)
        home_page.back_home()
        # 导入粤语音频
        video_import_page = VideoImportPage(driver)
        video_import_page.upload_video_sichuan()

    @allure.story("批量导入各种格式的音频")
    @allure.title("批量导入各种格式的音频，清空导入的音频，点击删除")
    @allure.feature("批量导入各种格式的音频，清空导入的音频，点击删除")
    def test_batch_video_upload(self, driver):
        home_page = HomePage(driver)
        home_page.back_home()
        video_import_page = VideoImportPage(driver)
        #批量导入视频文件
        video_import_page.upload_all_video_files_and_clear()
        #批量导入音频文件
        video_import_page.upload_all_audio_files_and_clear()

    @allure.story("文件上传页输入专有词汇格式")
    @allure.title("专有词汇格式不正确时，在文本框下方红色字体提示“专有词汇格式不正确，"
                  "输入含特殊字符的内容、含数字的内容、含特殊字符的内容")
    @allure.feature("专有词汇格式不正确时，在文本框下方红色字体提示“专有词汇格式不正确，"
                  "输入含特殊字符的内容、含数字的内容、含特殊字符的内容")
    def test_input_hot_word_while_upload(self, driver):
        home_page = HomePage(driver)
        home_page.back_home()
        video_import_page = VideoImportPage(driver)
        # 输入专有词汇
        video_import_page.input_hot_word_while_upload("测试&")
        video_import_page.input_hot_word_while_upload("123456")
        video_import_page.input_hot_word_while_upload("测试@")




