import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.constant_parameters import URL


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """钩子函数：在每个测试用例执行时打印用例名称"""
    outcome = yield  # 获取用例执行结果
    report = outcome.get_result()
    # 只在测试用例执行阶段打印（setup/teardown 阶段不打印）
    if report.when == "call":
        # 测试函数的完整路径（模块名::函数名）
        test_name = f"{item.module.__name__}::{item.name}"
        print(f"\n===== 正在执行测试函数：{test_name} =====")


@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    time.sleep(3)
    driver.quit()
    # driver.minimize_window()

@pytest.fixture(autouse=True)
def ensure_login(driver):
    if driver:
        if driver.current_url != URL+"#/login/account":
            # 已登录页面，直接返回
            return
        # 未登录，自动执行登录逻辑
        driver.get(URL+"#/login/account")
        driver.find_element(By.XPATH,
                                 '//*[@id="app"]/section/main/div[1]/div/div[2]/div/div/div/form/div[1]/div/div/input').send_keys(
            "admin")
        driver.find_element(By.XPATH,
                                 '//*[@id="app"]/section/main/div[1]/div/div[2]/div/div/div/form/div[2]/div/div/input').send_keys(
            "admin123")
        driver.find_element(By.XPATH,
                                 '//*[@id="app"]/section/main/div[1]/div/div[2]/div/div/div/form/div[4]/div/button').click()
