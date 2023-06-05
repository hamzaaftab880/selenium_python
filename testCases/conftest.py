import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome(executable_path="D:\selenium_python\webdrivers/chromedriver.exe")
    return driver