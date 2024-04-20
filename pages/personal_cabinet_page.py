import time

import allure
from locators.login_and_registration_pages_locators import LoginAndRegistrationPageLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_cabinet_locators import PersonalCabinetPageLocators
from pages.base_page import BasePage


class PersonalCabinetPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(driver)
        self.driver = driver

    @allure.step('Смотрим историю заказов')
    def click_on_orders_history(self):
        self.click_on_element(LoginAndRegistrationPageLocators.orders_history)

    @allure.step('Ждем открытия историю заказов')
    def wait_to_open_order_history(self):
        self.wait_to_click_on_element(locator=PersonalCabinetPageLocators.first_order)

    @allure.step('Ждем открытия профиля')
    def wait_to_be_open_profile_page(self):
        self.wait_to_click_on_element(locator=LoginAndRegistrationPageLocators.logout_button)

    @allure.step('Получаем номер первого заказа')
    def get_last_order_numbers(self):
        return self.get_text_element(locator=PersonalCabinetPageLocators.last_order)

    @allure.step('Ждем открытия профиля')
    def wait_to_be_open_profile_page(self):
        self.wait_to_click_on_element(locator=LoginAndRegistrationPageLocators.logout_button)

    @allure.step('Кликаем на текст "Войти"')
    def click_logout_button(self):
        self.click_on_element(LoginAndRegistrationPageLocators.logout_button)

    @allure.step('Смотрим историю заказов')
    def click_on_orders_history(self):
        self.click_on_element(LoginAndRegistrationPageLocators.orders_history)

    @allure.step('Ждем открытия главной страницы')
    def wait_to_be_invisible_loading_screen(self):
        self.wait_to_invisibil_on_element(MainPageLocators.loading_screen)

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
