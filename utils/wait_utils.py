# utils/wait_utils.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WaitUtils:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element_visible(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"❌ 元素 {locator} 超时未出现")
            return None

    def wait_for_element_clickable(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            print(f"❌ 元素 {locator} 不可点击")
            return None
