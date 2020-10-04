from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_form")
    REGISTER_PAGE = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTER_PASSWORD_REPEAT = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON=(By.CSS_SELECTOR, "[name='registration_submit']")
  
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_TEXT = (By.CSS_SELECTOR, "div.alertinner.wicon")

 
