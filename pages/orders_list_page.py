import time
import allure
from data import Urls, default_order_value
from locators.main_page_locators import MainPageLocators
from locators.order_list_locators import OrdersListLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получаем выполенные заказы за все время')
    def get_created_orders_for_all_time(self):
        return self.get_text_element(OrdersListLocators.created_orders_for_all_time)

    @allure.step('Получаем заказ который в процессе готовки')
    def get_order_in_work(self, expected_value):
        return self.get_orders_in_work(locator=OrdersListLocators.in_work, expected_value=expected_value)

    @allure.step('Получаем выполенные заказы за сегодня')
    def get_created_orders_for_today(self):
        return self.get_text_element(OrdersListLocators.created_orders_for_today)

    @allure.step('Кликаем на заказ')
    def click_on_order(self):
        self.click_on_element(OrdersListLocators.order)

    @allure.step('Ждем когда можно будет кликнуть на заказ')
    def wait_to_click_on_order(self):
        self.wait_to_click_on_element(OrdersListLocators.order)

    @allure.step('Ждем открытия "Ленты Заказов"')
    def wait_to_be_orders_list_page(self):
        self.wait_to_open_new_tab(title=Urls.orders_list)

    @allure.step('Получаем имя булочки в заказе')
    def get_order_information_in_order(self):
        return self.get_text_element(locator=OrdersListLocators.order_information)

    @allure.step('Получаем номер созданного заказа')
    def wait_to_get_actual_order_number(self):
        return self.get_order_numbers(
            locator=OrdersListLocators.created_order_number,
            default_value=default_order_value
        )

    @allure.step('Ждем открытия информации о заказе')
    def wait_to_be_open_created_order(self):
        self.wait_to_visible_on_element(OrdersListLocators.order_window)
        self.wait_to_click_on_element(MainPageLocators.cross_to_close)
        self.wait_to_visible_on_element(OrdersListLocators.order_animation)
