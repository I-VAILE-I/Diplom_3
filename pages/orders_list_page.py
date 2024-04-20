import time
import allure
from data import Urls
from locators.main_page_locators import MainPageLocators
from locators.order_list_locators import OrdersListLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(driver)
        self.driver = driver

    @allure.step('Получаем выполенные заказы за все время')
    def get_created_orders_for_all_time(self):
        return self.get_text_element(OrdersListLocators.created_orders_for_all_time)

    @allure.step('Получаем заказ который в процессе готовки')
    def get_order_in_work(self):
        return self.get_text_element(OrdersListLocators.in_work)

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
    def get_created_order_numbers(self):
        return self.get_text_element(locator=OrdersListLocators.created_order_number)

    @allure.step('Ждем открытия информации о заказе')
    def wait_to_be_open_created_order(self):
        self.wait_to_visible_on_element(OrdersListLocators.order_animation)
        self.wait_to_click_on_element(MainPageLocators.cross_to_close)

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

    @allure.step('Ждем открытия главной страницы')
    def wait_to_be_invisible_loading_screen(self):
        self.wait_to_invisibil_on_element(MainPageLocators.loading_screen)