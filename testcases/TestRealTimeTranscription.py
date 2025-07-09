import subprocess
import time

import allure
import pytest
from pywinauto import Application
import pygetwindow as gw
from pywinauto import Desktop

pytestmark = [allure.feature("实时转写模块用例"), allure.epic("麦耳会记客户端")]


class TestRealTimeTranscription:
    def setup_class(cls):
        # 启动程序
        # subprocess.Popen(r"C:\Program Files (x86)\AISPEECH\MileMeeting\MileMeeting.exe")
        # time.sleep(5)
        # # 获取窗口并置顶 & 最大化
        # windows = gw.getWindowsWithTitle("麦耳会记")  # 你可以替换为程序窗口标题关键字
        # gw_window = windows[0]
        # hwnd = gw_window._hWnd  # 窗口句柄
        # cls.window = Desktop(backend="uia").window(handle=hwnd)
        # cls.window.wait('visible', timeout=10)
        # cls.window.set_focus()
        # cls.window.maximize()
        # cls.app = Application(backend="uia").start(r'"C:\Program Files (x86)\AISPEECH\MileMeeting\MileMeeting.exe"')
        cls.app = Application(backend="uia").connect(title="麦耳会记")
        time.sleep(5)
        # cls.window = cls.app.window(title="麦耳会记")
        cls.window = cls.app.top_window()
        cls.window.maximize()  # 顶层窗口最大化
        cls.window.set_focus()


    def teardown_class(cls):
        time.sleep(2)
        cls.window.minimize()

    @pytest.mark.testcase
    @allure.description("点击开始会议记录，弹出转写前设置弹窗,音频录音时，点击【结束】显示结束录音提示弹窗")
    @allure.title("点击开始会议记录，弹出转写前设置弹窗,音频录音时，点击【结束】显示结束录音提示弹窗")
    def test_real_time_transcription_and_finish(self):
        #点击开始会议记录
        self.window.child_window(title="开始实时记录", control_type="Text").click_input()
        time.sleep(2)
        #点击开始会议
        self.window.child_window(title="开始会议", control_type="Button").click_input()
        time.sleep(4)
        #点击结束会议
        self.window.child_window(title="结束", control_type="Text").click_input()
        time.sleep(2)
        #点击结束
        self.window.child_window(title="结束", control_type="Button").click()
        time.sleep(2)
        #点击首页
        self.window.child_window(title="首页", control_type="Text").click_input()


