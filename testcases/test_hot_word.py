import allure
import pytest

from pages.home_page import HomePage
from pages.hot_word_page import HotWordPage


@allure.feature("测试热词管理")
@pytest.mark.usefixtures("driver")
class TestHotWord:
    @allure.story("热词为空")
    @allure.title("光标定位到文本输入框的任意位置可进入编辑状态，取消热词编辑，恢复空态显示，保存热词编辑，恢复空态显示")
    @allure.feature("光标定位到文本输入框的任意位置可进入编辑状态，取消热词编辑，恢复空态显示，保存热词编辑，恢复空态显示")
    @pytest.mark.order(-1)#最后运行
    def test_hot_word_empty(self, driver):
        #返回首页
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        #打开热词页面
        hot_word_page = HotWordPage(driver)
        hot_word_page.click_more_app_and_open_hot_word_page()
        #清空所有热词
        hot_word_page.delete_hot_word()
        #输入热词
        hot_word_page.add_hot_word("没有热词")
        #点击取消
        hot_word_page.hot_word_cancel()
        hot_word_page.add_hot_word("测试添加")
        #点击保存
        hot_word_page.hot_word_save()


    @allure.story("热词编辑")
    @allure.title("热词输入2个汉字，10个汉字")
    @allure.feature("热词输入2个汉字，10个汉字")
    def test_hot_word_input_chinese(self, driver):
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        # 打开热词页面
        hot_word_page = HotWordPage(driver)
        hot_word_page.click_more_app_and_open_hot_word_page()
        #输入热词
        hot_word_page.add_hot_word("汉字")
        hot_word_page.hot_word_save()
        hot_word_page.add_hot_word("我要输入十个汉字是吧")
        hot_word_page.hot_word_save()

    @allure.story("热词编辑")
    @allure.title("热词输入2个字母,10个字母，大写字母，大小写混合")
    @allure.feature("热词输入2个字母,10个字母，大写字母，大小写混合")
    def test_hot_word_input_letter(self, driver):
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        hot_word_page = HotWordPage(driver)
        hot_word_page.click_more_app_and_open_hot_word_page()
        hot_word_page.add_hot_word("ab")
        hot_word_page.hot_word_save()
        hot_word_page.add_hot_word("adkfnshend")
        hot_word_page.hot_word_save()
        hot_word_page.add_hot_word("ABD")
        hot_word_page.hot_word_save()
        hot_word_page.add_hot_word("ABDfdgnfd")
        hot_word_page.hot_word_save()

    @allure.story("热词编辑")
    @allure.title("热词文本框支持输入中文、英文、中英文逗号/顿号")
    @allure.feature("热词文本框支持输入中文、英文、中英文逗号/顿号")
    def test_hot_word_input_letter_and_chinese(self, driver):
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        hot_word_page = HotWordPage(driver)
        hot_word_page.click_more_app_and_open_hot_word_page()
        hot_word_page.add_hot_word("中文、end、顿号")
        hot_word_page.hot_word_save()

    @allure.story("热词编辑")
    @allure.title("同一槽位下输入重复的热词，保存时弹出toast提示")
    @allure.feature("同一槽位下输入重复的热词，保存时弹出toast提示")
    def test_hot_word_input_same_slot(self, driver):
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        hot_word_page = HotWordPage(driver)
        hot_word_page.click_more_app_and_open_hot_word_page()
        hot_word_page.add_hot_word("重复、重复")
        hot_word_page.hot_word_save()

    @allure.story("热词编辑")
    @allure.title("编辑状态下，点击tab标签可切换不同分页，输入不同的热词，保存提交")
    @allure.feature("编辑状态下，点击tab标签可切换不同分页，输入不同的热词，保存提交")
    def test_hot_word_input_different_tab(self, driver):
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        hot_word_page = HotWordPage(driver)
        hot_word_page.click_more_app_and_open_hot_word_page()
        hot_word_page.switch_hot_word_page_tab("人名")
        hot_word_page.add_hot_word("张三")
        hot_word_page.switch_hot_word_page_tab("地名")
        hot_word_page.add_hot_word("上海")
        hot_word_page.switch_hot_word_page_tab("其他热词")
        hot_word_page.add_hot_word("其他")
        #保存
        hot_word_page.hot_word_save()

    @allure.story("热词编辑")
    @allure.title("三个槽位页下输入同一个热词，保存提交")
    @allure.feature("三个槽位页下输入同一个热词，保存提交")
    def test_hot_word_input_different_tab(self, driver):
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        hot_word_page = HotWordPage(driver)
        hot_word_page.click_more_app_and_open_hot_word_page()
        hot_word = "李四"
        hot_word_page.switch_hot_word_page_tab("人名")
        hot_word_page.add_hot_word(hot_word)
        hot_word_page.switch_hot_word_page_tab("地名")
        hot_word_page.add_hot_word(hot_word)
        hot_word_page.switch_hot_word_page_tab("其他热词")
        hot_word_page.add_hot_word(hot_word)
        # 保存
        hot_word_page.hot_word_save()
        #点击搜索
        hot_word_page.search_hot_word(hot_word)
        #有多个搜索结果时点击下一个
        hot_word_page.click_next()


    @allure.story("热词编辑")
    @allure.title("确定取消热词编辑后，再次进入热词编辑")
    @allure.feature("确定取消热词编辑后，再次进入热词编辑")
    def test_hot_word_cancel(self, driver):
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        hot_word_page = HotWordPage(driver)
        hot_word_page.click_more_app_and_open_hot_word_page()
        hot_word_page.add_hot_word("取消")
        hot_word_page.hot_word_cancel()
        #回到首页
        home.back_home()
        #再次进入热词编辑
        hot_word_page.click_more_app_and_open_hot_word_page()

    @allure.story("热词编辑")
    @allure.title("编辑热词时，点击左侧侧边栏跳转页面")
    @allure.feature("编辑热词时，点击左侧侧边栏跳转页面")
    def test_hot_word_side_bar(self, driver):
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        hot_word_page = HotWordPage(driver)
        hot_word_page.click_more_app_and_open_hot_word_page()
        hot_word_page.add_hot_word("跳转")
        #点击导航栏跳转
        home.back_home()
        #弹窗点击确定离开
        hot_word_page.click_confirm_leave()

    @allure.story("热词编辑")
    @allure.title("保存后热词统一用中文顿号隔开,输入多个分隔符，保存过滤多余分隔符")
    @allure.feature("保存后热词统一用中文顿号隔开,输入多个分隔符，保存过滤多余分隔符")
    def test_hot_word_filter_separator(self, driver):
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        hot_word_page = HotWordPage(driver)
        hot_word_page.click_more_app_and_open_hot_word_page()
        hot_word_page.add_hot_word("一二，ABC,一一一一一一一一一一、aaaaaaaaaa")
        hot_word_page.hot_word_save()
        hot_word_page.add_hot_word("一二三四、、、、、一二三四五")
        hot_word_page.hot_word_save()

    @allure.story("热词编辑")
    @allure.title("选中多个热词删除,清空所有热词后保存，恢复空态显示")
    @allure.feature("选中多个热词删除,清空所有热词后保存，恢复空态显示")
    def test_hot_word_delete_all(self, driver):
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        hot_word_page = HotWordPage(driver)
        hot_word_page.click_more_app_and_open_hot_word_page()
        hot_word_page.delete_hot_word()

    @allure.story("搜索热词")
    @allure.title("精确搜索非当前tab中存在的热词,搜索不存在的热词，弹出toast提示")
    @allure.feature("精确搜索非当前tab中存在的热词,搜索不存在的热词，弹出toast提示")
    def test_hot_word_search(self, driver):
        # 返回到首页
        home = HomePage(driver)
        home.back_home()
        hot_word_page = HotWordPage(driver)
        hot_word_page.click_more_app_and_open_hot_word_page()
        #添加热词
        hot_word = "测试搜索"
        hot_word_page.add_hot_word(hot_word)
        #切换tab页
        hot_word_page.switch_hot_word_page_tab("其他热词")
        #搜索刚才添加的热词
        hot_word_page.search_hot_word(hot_word)
        #搜索不存在的热词
        hot_word_page.search_hot_word("不存在的")
