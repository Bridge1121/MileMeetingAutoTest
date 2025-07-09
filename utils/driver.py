import tempfile

from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    # 设置自动允许麦克风权限（以“允许”代替弹窗）
    prefs = {
        "profile.default_content_setting_values.media_stream_mic": 1,  # 1: 允许, 2: 阻止
        "profile.default_content_setting_values.media_stream_camera": 1,
    }
    options.add_argument("--start-maximized")
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    # driver.get("https://10.12.7.166:9443/")
    driver.implicitly_wait(10)
    return driver
