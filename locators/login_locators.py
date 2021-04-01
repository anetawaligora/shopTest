from selenium.webdriver.common.by import By


class LoginLocators:
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_click = (By.ID, "login-button")

