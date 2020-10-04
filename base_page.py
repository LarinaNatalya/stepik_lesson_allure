from selenium.common.exceptions import NoSuchElementException
from locators import MainPageLocators
from locators import BasePageLocators

class BasePage():#класс внутри которого методы
    def __init__(self, browser, url, timeout=10):#конструктор, неявное ожидание
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):#метод
        self.browser.get(self.url)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        except NoSuchElementException: return False
        return True
        
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
    
    def put_to_register_email(self)
        key=self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        key.send_keys(email)
        
    def put_to_register_password(self)
        password_1=self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_1.send_keys(password_text)

    def put_to_register_password_repeat(self)
        password_2=self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT)
        password_2.send_keys(password_text)

    def click_to_register_button(self) 
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)   
        button.click()
    
    def answer_to_register(self)
        answer=browser.find_element (*BasePageLocators.LOGIN_TEXT)
        assert "Thanks" in answer.text




        
