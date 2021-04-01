from enum import Enum
from locators import LoginLocators, ProductsLocators
from selenium.webdriver.support.select import Select


class ProductsSorting(Enum):
    az = 'Name (A to Z)'
    za = 'Name (Z to A)'
    lohi = 'Price (low to high)'
    hilo = 'Price (high to low)'


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://www.saucedemo.com")

    def log_in(self):
        self.driver.find_element(*LoginLocators.username_input).send_keys("standard_user")
        self.driver.find_element(*LoginLocators.password_input).send_keys("secret_sauce")
        self.driver.find_element(*LoginLocators.login_click).click()

    def add_to_cart(self, index):
        self.driver.find_elements(*ProductsLocators.add_to_cart_button)[index].click()

    def remove_from_cart(self, index):
        self.driver.find_elements(*ProductsLocators.remove_from_cart_button)[index].click()

    def is_cart_badge_displayed(self):
        cart_badge_elements = self.driver.find_elements(*ProductsLocators.cart_badge)
        return cart_badge_elements[0].is_displayed() if len(cart_badge_elements) > 0 else False

    def get_cart_badge_count(self):
        return self.driver.find_element(*ProductsLocators.cart_badge).text

    def get_active_sort_option(self):
        return self.driver.find_element(*ProductsLocators.select_container).find_element(
            *ProductsLocators.active_option).text

    def get_products_prices_in_display_order(self):
        price_elements = self.driver.find_elements(*ProductsLocators.inventory_item_price)
        price_values = map(lambda element: element.text, price_elements)
        prices_as_numbers = map(lambda price: float(price[1:]), price_values)
        return list(prices_as_numbers)

    def get_products_names_in_display_order(self):
        name_elements = self.driver.find_elements(*ProductsLocators.inventory_item_name)
        name_values = map(lambda element: element.text, name_elements)
        return list(name_values)

    def change_sorting_type(self, value: ProductsSorting):
        select = Select(self.driver.find_element(*ProductsLocators.product_sort_container))
        select.select_by_value(value.name)
