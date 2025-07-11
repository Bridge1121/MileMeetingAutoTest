import allure
import pytest
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


@allure.feature("退出功能")
@pytest.mark.usefixtures("driver")
class TestLogout:


    @allure.story("退出登录")
    @allure.title("登录成功，点击菜单栏头像>退出账号，可退出账号")
    @allure.feature("登录成功，点击菜单栏头像>退出账号，可退出账号")
    @pytest.mark.order(index=-1)#最后执行
    def test_logout_success(self,driver):
        # 单独运行要加这两行
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        #先登录再退出
        login = LoginPage(driver)
        login.login("admin", "admin123")
        logout = LogoutPage(driver)
        logout.logout()

    @allure.story("实时转写时退出登录")
    @allure.title("正在实时转写过程中，点击退出账号，弹窗提示需先结束实时转写，然后再退出系统，点击确定后再退出账号")
    @allure.feature("正在实时转写过程中，点击退出账号，弹窗提示需先结束实时转写，然后再退出系统，点击确定后再退出账号")
    def test_logout_while_transcription(self,driver):
        #单独运行时添加
        # login = LoginPage(driver)
        # login.open()
        # login.login()
        logout = LogoutPage(driver)
        logout.logout_transcription()




