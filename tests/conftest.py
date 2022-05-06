import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture         # fct that run before the test functions
def browser():
    # initializing Chrome driver instance, chrome tab opens
    driver = selenium.webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    #return the webdriver instance  -  cleanup after fixture code execution
    yield driver
    #close the driver
    driver.quit()