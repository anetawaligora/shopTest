
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# Zdefiniowanie metody (logowania) wewnątrz tej metody powstanie test

def test_log_in():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    # obiekt Wait
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com")
    # driver.find_element_by_name("user-name").click()
    driver.find_element_by_id("user-name").send_keys("standard_user")
    driver.find_element_by_id("password").send_keys("secret_sauce")
    driver.find_element_by_id("login-button").click()

    assert driver.find_element_by_class_name("product_label").is_displayed()
    print("Login test passed")
