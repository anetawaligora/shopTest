from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_add_to_cart():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    # obiekt Wait
    # wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com")
    driver.find_element_by_id("user-name").send_keys("standard_user")
    driver.find_element_by_id("password").send_keys("secret_sauce")
    driver.find_element_by_id("login-button").click()

    # driver.execute_script("arguments[o].scrollIntoViev(true);", driver.find_element_by_id("btn_primary btn_inventory"))

    # driver.find_element_by_class_name("inventory_item_name").click()

    driver.find_elements_by_class_name("btn_inventory")[0].click()

    assert driver.find_element_by_class_name("shopping_cart_badge").is_displayed()
    print("Add to cart test passed")


def test_go_to_cart():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    # obiekt Wait
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com")
    driver.find_element_by_id("user-name").send_keys("standard_user")
    driver.find_element_by_id("password").send_keys("secret_sauce")
    driver.find_element_by_id("login-button").click()

    # driver.execute_script("arguments[o].scrollIntoViev(true);", driver.find_element_by_id("btn_primary btn_inventory"))

    # driver.find_element_by_class_name("inventory_item_name").click()

    driver.find_elements_by_class_name("svg-inline--fa")

    assert driver.find_element_by_class_name("inventory_item_name").is_displayed()
    print("Go to cart test passed")
