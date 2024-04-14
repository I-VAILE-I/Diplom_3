import allure
from data import Urls, ExpectedResults
from pages.orders_list_page import OrderListPage


@allure.suite('Проверка раздела "Лента Заказов" в Chrome')
class TestOrderListPageChrome:

    @allure.title('Показывается подробная информация кликая на заказ')
    def test_click_on_order_to_get_information(self, driver_chrome):
        order_list_page = OrderListPage(driver=driver_chrome)
        order_list_page.click_on_text_personal_cabinet()
        order_list_page.wait_to_be_open_login_page()
        order_list_page.add_email()
        order_list_page.add_password()
        order_list_page.click_login_button()
        order_list_page.wait_to_be_open_main_page()
        order_list_page.drag_and_drop_bun()
        order_list_page.click_create_order_button()
        order_list_page.wait_500_ms()
        order_list_page.close_info_about_order()
        order_list_page.click_on_orders_list()
        order_list_page.wait_500_ms()
        order_list_page.click_on_order()
        assert order_list_page.get_order_information_in_order() == ExpectedResults.order_status_in_list

    @allure.title('Заказы пользователя отображаются на странице «Лента заказов»')
    def test_user_order_from_history_in_orders_list(self, driver_chrome):
        order_list_page = OrderListPage(driver=driver_chrome)
        order_list_page.click_on_text_personal_cabinet()
        order_list_page.wait_to_be_open_login_page()
        order_list_page.add_email()
        order_list_page.add_password()
        order_list_page.click_login_button()
        order_list_page.wait_to_be_open_main_page()
        order_list_page.click_on_text_personal_cabinet()
        order_list_page.wait_to_be_open_profile_page()
        order_list_page.click_on_orders_history()
        order_list_page.wait_to_open_order_history()
        order_numbers = order_list_page.get_last_order_numbers().split('\n')[0]
        order_list_page.click_on_orders_list()
        order_list_page.wait_500_ms()
        assert order_numbers in order_list_page.text_on_page()

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_created_orders_on_all_time_change(self, driver_chrome):
        order_list_page = OrderListPage(driver=driver_chrome)
        order_list_page.click_on_text_personal_cabinet()
        order_list_page.wait_to_be_open_login_page()
        order_list_page.add_email()
        order_list_page.add_password()
        order_list_page.click_login_button()
        order_list_page.wait_to_be_open_main_page()
        order_list_page.click_on_orders_list()
        order_list_page.wait_500_ms()
        created_orders_all_time = order_list_page.get_created_orders_for_all_time().split('\n')[1]
        order_list_page.click_on_constructor()
        order_list_page.wait_to_be_open_main_page()
        order_list_page.drag_and_drop_bun()
        order_list_page.click_create_order_button()
        order_list_page.wait_500_ms()
        order_list_page.close_info_about_order()
        order_list_page.click_on_orders_list()
        order_list_page.wait_500_ms()
        changed_orders_all_time = order_list_page.get_created_orders_for_all_time().split('\n')[1]
        assert int(changed_orders_all_time) > int(created_orders_all_time)

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_created_orders_on_today_change(self, driver_chrome):
        order_list_page = OrderListPage(driver=driver_chrome)
        order_list_page.click_on_text_personal_cabinet()
        order_list_page.wait_to_be_open_login_page()
        order_list_page.add_email()
        order_list_page.add_password()
        order_list_page.click_login_button()
        order_list_page.wait_to_be_open_main_page()
        order_list_page.click_on_orders_list()
        order_list_page.wait_500_ms()
        created_orders_all_time = order_list_page.get_created_orders_for_today().split('\n')[1]
        order_list_page.click_on_constructor()
        order_list_page.wait_to_be_open_main_page()
        order_list_page.drag_and_drop_bun()
        order_list_page.click_create_order_button()
        order_list_page.wait_500_ms()
        order_list_page.close_info_about_order()
        order_list_page.click_on_orders_list()
        order_list_page.wait_500_ms()
        changed_orders_all_time = order_list_page.get_created_orders_for_today().split('\n')[1]
        assert int(changed_orders_all_time) > int(created_orders_all_time)

    @allure.title('Созданный заказ в процессе')
    def test_get_created_order_with_status_in_work(self, driver_chrome):
        order_list_page = OrderListPage(driver=driver_chrome)
        order_list_page.click_on_text_personal_cabinet()
        order_list_page.wait_to_be_open_login_page()
        order_list_page.add_email()
        order_list_page.add_password()
        order_list_page.click_login_button()
        order_list_page.wait_to_be_open_main_page()
        order_list_page.drag_and_drop_bun()
        order_list_page.click_create_order_button()
        order_list_page.wait_500_ms()
        order_list_page.wait_500_ms() # не понял к чему привязаться, что бы заглушка в 99999 пропала
        created_order_num = order_list_page.get_created_order_numbers()
        order_list_page.close_info_about_order()
        order_list_page.click_on_orders_list()
        order_list_page.wait_5_s()
        in_work_order = order_list_page.get_order_in_work()
        assert in_work_order == f'0{created_order_num}'
