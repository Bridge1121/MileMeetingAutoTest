import allure
import pytest
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


@allure.feature("登录功能")
@pytest.mark.usefixtures("driver")
class TestLogin:

    @allure.story("正确用户名密码登录")
    @allure.title("输入默认账号：admin，密码：admin123，点击【登录】按钮可登录成功进入首页,密码是密文显示")
    @allure.feature("输入默认账号：admin，密码：admin123，点击【登录】按钮可登录成功进入首页,密码是密文显示")
    @pytest.mark.order(1)
    @pytest.mark.skip
    def test_login_success(self,driver):
        login = LoginPage(driver)
        login.open()
        login.login("admin", "admin123")



