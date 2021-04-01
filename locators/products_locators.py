from selenium.webdriver.common.by import By


class ProductsLocators:
    active_option = (By.CLASS_NAME, "active_option")
    add_to_cart_button = (By.CLASS_NAME, "btn_inventory")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    inventory_item_price = (By.CLASS_NAME, "inventory_item_price")
    inventory_item_name = (By.CLASS_NAME, "inventory_item_name")
    product_sort_container = (By.CLASS_NAME, "product_sort_container")
    remove_from_cart_button = (By.CLASS_NAME, "btn_inventory")
    select_container = (By.CLASS_NAME, "select_container")
