import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
