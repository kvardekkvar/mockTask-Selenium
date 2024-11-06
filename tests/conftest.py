import pytest
from selenium import webdriver

config = {
    'browser': 'chrome',
    'headless': False,
    'debug_mode': False
}

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    if config["headless"]:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    if not config["debug_mode"]:
        driver.quit()
