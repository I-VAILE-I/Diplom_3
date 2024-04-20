import time
import allure
from data import TextData, Urls
from locators.login_and_registration_pages_locators import LoginAndRegistrationPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class LoginAndRegistrationPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(driver)
        self.driver = driver

    @allure.step('Вводим Email')
    def add_email(self):
        self.input_text_in_field(locator=LoginAndRegistrationPageLocators.login_input_email, text=TextData.email)

    @allure.step('Вводим новый пароль')
    def add_new_password(self):
        self.input_text_in_field(locator=LoginAndRegistrationPageLocators.input_new_password, text=TextData.password)

    @allure.step('Вводим пароль')
    def add_password(self):
        self.input_text_in_field(locator=LoginAndRegistrationPageLocators.login_input_password, text=TextData.password)

    @allure.step('Кликаем на текст "Войти"')
    def click_login_button(self):
        self.click_on_element(LoginAndRegistrationPageLocators.login_button)

    @allure.step('Делаем введенный новый пароль видимым')
    def make_password_visible(self):
        self.click_on_element(locator=LoginAndRegistrationPageLocators.make_new_password_visible)

    @allure.step('Кликаем на кнопку "Восстановить"')
    def click_on_recovery_password_button(self):
        self.click_on_element(LoginAndRegistrationPageLocators.login_button)

    @allure.step('Кликаем на "Восстановление пароля"')
    def click_on_recovery_password_text(self):
        self.click_on_element(LoginAndRegistrationPageLocators.forgot_password_button)

    @allure.step('Ждем открытия страницы "Замены пароля"')
    def wait_to_be_open_reset_password_page(self):
        self.wait_to_open_new_tab(title=Urls.reset_password_url)

    @allure.step('Ждем открытия страницы "Восстановление пароля"')
    def wait_to_be_open_forgot_password_page(self):
        self.wait_to_open_new_tab(title=Urls.forgot_password_url)

    @allure.step('Ждем открытия страницы "Авторизации"')
    def wait_to_be_open_login_page(self):
        self.wait_to_open_new_tab(title=Urls.login_url)

    @allure.step('Получаем статус активности поля пароля')
    def get_password_field_status(self):
        return self.get_password_field_activity(locator=LoginAndRegistrationPageLocators.input_new_password)

    @allure.step('Ждем когда главная страница станет кликабельна')
    def wait_500_ms(self):
        """
        Поясню почем time.sleep: неявное ожидание у меня отказывается работать
        А явное ожидание, не понял к какому элементу можно привязаться
        т.к. во время загрузки страницы они становятся активными и видимыми а
        селениум при нажатии на них падает, нашел выход только в этом.
        Причем такая проблема только с Firefox
        """
        time.sleep(0.5)

    @allure.step('Ждем открытия главной страницы')
    def wait_to_be_invisible_loading_screen(self):
        self.wait_to_invisibil_on_element(MainPageLocators.loading_screen)
