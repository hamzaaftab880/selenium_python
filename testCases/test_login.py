import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_001_Login:

    base_url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homepage_title(self):
        self.driver = webdriver.Chrome(executable_path= "D:\selenium_python\webdrivers/chromedriver.exe")
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Your store. Login"
            assert True
        else:
            assert False
    def test_login(self):

        self.driver = webdriver.Chrome(executable_path="D:\selenium_python\webdrivers/chromedriver.exe")
        self.driver.get(self.base_url)
