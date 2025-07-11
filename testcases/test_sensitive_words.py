import allure
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.sensitive_words_page import SensitiveWordsPage


@allure.feature("敏感词管理")
@pytest.mark.usefixtures("driver")
class TestSensitiveWords:
    @allure.story("添加敏感词")
    @allure.title("输入2个汉字、10个汉字")
    @allure.feature("输入2个汉字、10个汉字")
    @pytest.mark.order(1)
    def test_add_sensitive_words_chinese(self, driver):
        # 单独运行时添加
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        home = HomePage(driver)
        home.back_home()
        sensitive_words_page = SensitiveWordsPage(driver)
        #添加2个汉字
        sensitive_words_page.open_sensitive_words_page()
        sensitive_words_page.add_sensitive_words("小狗")
        #输入10个汉字
        sensitive_words_page.add_sensitive_words(sensitive_words="小黑小黑小黑小黑小黑")

    @allure.story("删除敏感词")
    @allure.title("删除敏感词")
    @allure.feature("删除敏感词")
    @pytest.mark.order(3)
    def test_add_sensitive_words_chinese_and_english(self, driver):
        home = HomePage(driver)
        home.back_home()
        sensitive_words_page = SensitiveWordsPage(driver)
        sensitive_words_page.open_sensitive_words_page()
        sensitive_words_page.delete_sensitive_words()

    @allure.story("搜索敏感词")
    @allure.title("搜索敏感词")
    @allure.feature("搜索敏感词")
    @pytest.mark.order(2)
    def test_search_sensitive_words(self, driver):
        home = HomePage(driver)
        home.back_home()
        sensitive_words_page = SensitiveWordsPage(driver)
        sensitive_words_page.open_sensitive_words_page()
        sensitive_words_page.search_sensitive_words("小")