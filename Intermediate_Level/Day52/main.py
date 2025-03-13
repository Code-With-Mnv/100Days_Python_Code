import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class AutoMate:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

        self.url = "https://www.instagram.com/"
        self.driver.get(self.url)

    def login_to_insta(self):

        # Enter username and password
        username_input = self.driver.find_element(
            by=By.CSS_SELECTOR, value="input[name='username']"
        )
        password_input = self.driver.find_element(
            by=By.CSS_SELECTOR, value="input[name='password']"
        )
        login_button = self.driver.find_element(
            by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button'
        )

        username_input.send_keys("manavfun0@gmail.com")
        password_input.send_keys("Fun@Insta")
        login_button.click()


automater = AutoMate()
time.sleep(2)
automater.login_to_insta()
