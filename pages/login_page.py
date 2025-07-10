import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://10.12.7.166:9443/")
        time.sleep(2)
        #点击高级
        self.driver.find_element("xpath",'//*[@id="details-button"]').click()
        #点击继续前往
        self.driver.find_element("xpath",'//*[@id="proceed-link"]').click()
        self.driver.implicitly_wait(5)


    def login(self, username="admin", password="admin123"):
        self.driver.find_element("xpath", '//*[@id="app"]/section/main/div[1]/div/div[2]/div/div/div/form/div[1]/div/div/input').send_keys(username)
        self.driver.find_element("xpath", '//*[@id="app"]/section/main/div[1]/div/div[2]/div/div/div/form/div[2]/div/div/input').send_keys(password)
        self.driver.find_element("xpath", '//*[@id="app"]/section/main/div[1]/div/div[2]/div/div/div/form/div[4]/div/button').click()
