import time

import allure
from data import TextData, Urls
from locators.login_and_registration_pages_locators import LoginAndRegistrationPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_list_locators import OrdersListLocators
from locators.personal_cabinet_locators import PersonalCabinetPageLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем на текст "Личный кабинет"')
    def click_on_text_personal_cabinet(self):
        self.click_on_element(MainPageLocators.personal_cabinet_text)

    @allure.step('Кликаем на "Конструктор"')
    def click_on_constructor(self):
        self.click_on_element(MainPageLocators.constructor_selection)

    @allure.step('Кликаем на "Лента заказов"')
    def click_on_orders_list(self):
        self.click_on_element(MainPageLocators.orders_list)

    @allure.step('Получаем выполенные заказы за все время')
    def get_created_orders_for_all_time(self):
        return self.get_text_element(OrdersListLocators.created_orders_for_all_time)

    @allure.step('Получаем заказ который в процессе готовки')
    def get_order_in_work(self):
        return self.get_text_element(OrdersListLocators.in_work)

    @allure.step('Получаем выполенные заказы за сегодня')
    def get_created_orders_for_today(self):
        return self.get_text_element(OrdersListLocators.created_orders_for_today)

    @allure.step('Вводим Email')
    def add_email(self):
        self.input_text_in_field(locator=LoginAndRegistrationPageLocators.login_input_email, text=TextData.email)

    @allure.step('Вводим пароль')
    def add_password(self):
        self.input_text_in_field(locator=LoginAndRegistrationPageLocators.login_input_password, text=TextData.password)

    @allure.step('Кликаем на текст "Войти"')
    def click_login_button(self):
        self.click_on_element(LoginAndRegistrationPageLocators.login_button)

    @allure.step('Кликаем на "Оформить заказ"')
    def click_create_order_button(self):
        self.click_on_element(MainPageLocators.login_button_on_main_page)

    @allure.step('Кликаем на заказ')
    def click_on_order(self):
        self.click_on_element(OrdersListLocators.order)

    @allure.step('Закрываем информацию о заказе')
    def close_info_about_order(self):
        self.click_on_element(MainPageLocators.cross_to_close)

    @allure.step('Перетаскиваем булочку')
    def drag_and_drop_bun(self):
        self.drag_and_drop(MainPageLocators.first_bun, MainPageLocators.constructor)

    @allure.step('Смотрим историю заказов')
    def click_on_orders_history(self):
        self.click_on_element(LoginAndRegistrationPageLocators.orders_history)

    @allure.step('Ждем открытия страницы логина')
    def wait_to_be_open_login_page(self):
        self.wait_to_open_new_tab(title=Urls.login_url)

    @allure.step('Ждем открытия историю заказов')
    def wait_to_open_order_history(self):
        self.wait_to_click_on_element(locator=PersonalCabinetPageLocators.first_order)

    @allure.step('Ждем открытия главной страницы')
    def wait_to_be_open_main_page(self):
        self.wait_to_open_new_tab(title=Urls.main_page_url_after_login)

    @allure.step('Ждем открытия "Ленты Заказов"')
    def wait_to_be_orders_list_page(self):
        self.wait_to_open_new_tab(title=Urls.orders_list)

    @allure.step('Ждем когда можно будет закрыть окно')
    def wait_to_close_window(self):
        self.wait_to_element_invisible(locator=MainPageLocators.cross_to_close)

    @allure.step('Ждем открытия профиля')
    def wait_to_be_open_profile_page(self):
        self.wait_to_click_on_element(locator=LoginAndRegistrationPageLocators.logout_button)

    @allure.step('Получаем имя булочки в заказе')
    def get_order_information_in_order(self):
        return self.get_text_element(locator=OrdersListLocators.order_information)

    @allure.step('Получаем номер первого заказа')
    def get_last_order_numbers(self):
        return self.get_text_element(locator=PersonalCabinetPageLocators.last_order)

    @allure.step('Получаем номер созданного заказа')
    def get_created_order_numbers(self):
        return self.get_text_element(locator=OrdersListLocators.created_order_number)

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

    @allure.step('Ждем когда главная страница станет кликабельна')
    def wait_3_s(self):
        """
        Поясню почем time.sleep: неявное ожидание у меня отказывается работать
        А явное ожидание, не понял к какому элементу можно привязаться
        т.к. во время загрузки страницы они становятся активными и видимыми а
        селениум при нажатии на них падает, нашел выход только в этом.
        Причем такая проблема только с Firefox
        """
        time.sleep(3)

    @allure.step('Ждем когда главная страница станет кликабельна')
    def wait_5_s(self):
        """
        Жду появление заказа, не понял к чему привязать явное ожидание
        """
        time.sleep(5)