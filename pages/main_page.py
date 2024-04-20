import time

import allure
from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(driver)
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

    @allure.step('Получаем дополнительную информацию об ингридиенте')
    def open_info_about_bun(self):
        self.click_on_element(MainPageLocators.first_bun)

    @allure.step('Закрываем информацию об ингридиенте')
    def click_on_close_cross(self):
        self.click_on_element(MainPageLocators.cross_to_close)

    @allure.step('Кликаем на "Оформить заказ"')
    def click_create_order_button(self):
        self.click_on_element(MainPageLocators.login_button_on_main_page)

    @allure.step('Перетаскиваем булочку')
    def drag_and_drop_bun(self):
        self.drag_and_drop(MainPageLocators.first_bun, MainPageLocators.constructor)

    @allure.step('Ждем открытия главной страницы')
    def wait_to_be_open_main_page(self):
        self.wait_to_open_new_tab(title=Urls.main_page_url_after_login)

    @allure.step('Ждем когда можно будет кликнуть на личный кабинет')
    def wait_to_click_personal_cabinet(self):
        self.wait_to_click_on_element(MainPageLocators.personal_cabinet_text)

    @allure.step('Ждем когда можно будет кликнуть на конструктор')
    def wait_to_click_constructor(self):
        self.wait_to_click_on_element(MainPageLocators.constructor_selection)

    @allure.step('Ждем открытия главной страницы')
    def wait_to_be_invisible_loading_screen(self):
        self.wait_to_invisibil_on_element(MainPageLocators.loading_screen)

    @allure.step('Получаем имя булочки')
    def get_bun_name(self):
        return self.get_text_element(locator=MainPageLocators.bun_name)

    @allure.step('Получаем статус заказа')
    def get_order_status(self):
        return self.get_text_element(locator=MainPageLocators.order_created)

    @allure.step('Смотрим счетчик на булочке')
    def get_bun_counter(self):
        return self.get_text_element(locator=MainPageLocators.bun_count)

    @allure.step('Ждем когда можно будет закрыть окно')
    def wait_to_close_window(self):
        self.wait_to_element_invisible(locator=MainPageLocators.cross_to_close)

    @allure.step('Кликаем на кнопку "Войти"')
    def click_on_login_button(self):
        self.click_on_element(MainPageLocators.login_button_on_main_page)

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
