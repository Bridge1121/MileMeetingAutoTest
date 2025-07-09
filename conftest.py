import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    time.sleep(3)
    # driver.quit()
    driver.minimize_window()

@pytest.fixture(autouse=True)
def ensure_login(driver):
    if driver:
        if driver.current_url != "https://10.12.7.166:9443/#/login/account":
            # 已登录页面，直接返回
            return
        # 未登录，自动执行登录逻辑
        driver.get("https://10.12.7.166:9443/#/login/account")
        driver.find_element(By.XPATH,
                                 '//*[@id="app"]/section/main/div[1]/div/div[2]/div/div/div/form/div[1]/div/div/input').send_keys(
            "admin")
        driver.find_element(By.XPATH,
                                 '//*[@id="app"]/section/main/div[1]/div/div[2]/div/div/div/form/div[2]/div/div/input').send_keys(
            "admin123")
        driver.find_element(By.XPATH,
                                 '//*[@id="app"]/section/main/div[1]/div/div[2]/div/div/div/form/div[4]/div/button').click()
