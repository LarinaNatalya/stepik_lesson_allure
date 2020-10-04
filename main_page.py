from base_page import BasePage
from locators import MainPageLocators
from selenium.webdriver.common.by import By
from login_page import LoginPage

'''class MainPage(BasePage):#MainPage. Его нужно сделать наследником класса BasePage- доступ ко всем атрибутам и методам своего класса-предка

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
   #     return LoginPage(browser=self.browser, url=self.browser.current_url
'''   
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
 