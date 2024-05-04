import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture(scope="function")
def driver_firefox():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1280,720')
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(Urls.main_page_url)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1280,720')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Urls.main_page_url)
    yield driver
    driver.quit()
