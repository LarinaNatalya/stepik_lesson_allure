from base_page import BasePage

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url_text=driver.current_url
        past_link="login"
        assert past_link in url_text,\
        "Seach page title '\s' should contain search text '\s'" %(url_text, past_link)

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_PAGE), "Login page is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_PAGE), "Register page is not presented"
        
    def should_be_register_email(self):
        #проверка, есть ли поле ввода email
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Register email is not presented"
    
    def should_be_register_password(self):
        #проверка, есть ли поле ввода пароля
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Register password is not presented"
        
    def should_be_register_password_repeat(self):
        #проверка, есть ли поле повторного ввода пароля
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_REPEAT), "Register password repeat is not presented"
        
    def should_be_register_button(self):
        #проверка, есть ли кнопка регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register register button is not presented"    
        
        
        
  