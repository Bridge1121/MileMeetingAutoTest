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
    def test_cn_video_import(self, driver):
        # 单独运行要加这两行
        login = LoginPage(driver)
        login.open()
        login.login()
        home_page = HomePage(driver)
        home_page.back_home()
        #导入中文音频
        video_import_page = VideoImportPage(driver)
        video_import_page.upload_video_chinese()

