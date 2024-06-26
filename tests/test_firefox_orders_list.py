import allure
from data import ExpectedResults
from pages.login_and_registration_page import LoginAndRegistrationPage
from pages.main_page import MainPage
from pages.orders_list_page import OrderListPage
from pages.personal_cabinet_page import PersonalCabinetPage


@allure.suite('Проверка раздела "Лента Заказов" в firefox')
class TestOrderListPageChrome:

    @allure.title('Показывается подробная информация кликая на заказ')
    def test_click_on_order_to_get_information(self, driver_firefox):
        main_page = MainPage(driver=driver_firefox)
        personal_cabinet = LoginAndRegistrationPage(driver=driver_firefox)
        order_list_page = OrderListPage(driver=driver_firefox)
        main_page.click_on_element_text_personal_cabinet()
        personal_cabinet.wait_to_be_open_login_page()
        personal_cabinet.add_email()
        personal_cabinet.add_password()
        personal_cabinet.click_login_button()
        main_page.wait_to_be_open_main_page()
        main_page.drag_and_drop_bun()
        main_page.click_create_order_button()
        main_page.wait_to_be_invisible_loading_screen()
        order_list_page.wait_to_be_open_created_order()
        order_list_page.wait_to_get_actual_order_number()
        main_page.wait_to_click_close_cross()
        main_page.click_on_close_cross()
        main_page.click_on_orders_list()
        order_list_page.click_on_order()
        assert order_list_page.get_order_information_in_order() == ExpectedResults.order_status_in_list

    @allure.title('Заказы пользователя отображаются на странице «Лента заказов»')
    def test_user_order_from_history_in_orders_list(self, driver_firefox):
        main_page = MainPage(driver=driver_firefox)
        login_page = LoginAndRegistrationPage(driver=driver_firefox)
        order_list_page = OrderListPage(driver=driver_firefox)
        personal_cabinet_page = PersonalCabinetPage(driver=driver_firefox)
        main_page.click_on_element_text_personal_cabinet()
        login_page.wait_to_be_open_login_page()
        login_page.add_email()
        login_page.add_password()
        login_page.click_login_button()
        main_page.wait_to_be_open_main_page()
        main_page.click_on_element_text_personal_cabinet()
        personal_cabinet_page.wait_to_be_open_profile_page()
        personal_cabinet_page.click_on_orders_history()
        personal_cabinet_page.wait_to_open_order_history()
        order_numbers = personal_cabinet_page.get_last_order_numbers().split('\n')[0]
        main_page.click_on_orders_list()
        order_list_page.wait_to_click_on_order()
        assert order_numbers in order_list_page.text_on_page()

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_created_orders_on_all_time_change(self, driver_firefox):
        main_page = MainPage(driver=driver_firefox)
        login_page = LoginAndRegistrationPage(driver=driver_firefox)
        order_list_page = OrderListPage(driver=driver_firefox)
        main_page.click_on_element_text_personal_cabinet()
        login_page.wait_to_be_open_login_page()
        login_page.add_email()
        login_page.add_password()
        login_page.click_login_button()
        main_page.wait_to_be_open_main_page()
        main_page.click_on_orders_list()
        order_list_page.wait_to_click_on_order()
        created_orders_all_time = order_list_page.get_created_orders_for_all_time().split('\n')[1]
        main_page.click_on_constructor()
        main_page.wait_to_be_open_main_page()
        main_page.drag_and_drop_bun()
        main_page.click_create_order_button()
        order_list_page.wait_to_be_open_created_order()
        order_list_page.wait_to_get_actual_order_number()
        main_page.wait_to_click_close_cross()
        main_page.click_on_close_cross()
        main_page.click_on_orders_list()
        order_list_page.wait_to_click_on_order()
        changed_orders_all_time = order_list_page.get_created_orders_for_all_time().split('\n')[1]
        assert int(changed_orders_all_time) > int(created_orders_all_time)

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_created_orders_on_today_change(self, driver_firefox):
        main_page = MainPage(driver=driver_firefox)
        login_page = LoginAndRegistrationPage(driver=driver_firefox)
        order_list_page = OrderListPage(driver=driver_firefox)
        main_page.click_on_element_text_personal_cabinet()
        login_page.wait_to_be_open_login_page()
        login_page.add_email()
        login_page.add_password()
        login_page.click_login_button()
        main_page.wait_to_be_open_main_page()
        main_page.click_on_orders_list()
        order_list_page.wait_to_click_on_order()
        created_orders_all_time = order_list_page.get_created_orders_for_today().split('\n')[1]
        main_page.click_on_constructor()
        main_page.wait_to_be_open_main_page()
        main_page.drag_and_drop_bun()
        main_page.click_create_order_button()
        order_list_page.wait_to_be_open_created_order()
        order_list_page.wait_to_get_actual_order_number()
        main_page.wait_to_click_close_cross()
        main_page.click_on_close_cross()
        main_page.click_on_orders_list()
        order_list_page.wait_to_click_on_order()
        changed_orders_all_time = order_list_page.get_created_orders_for_today().split('\n')[1]
        assert int(changed_orders_all_time) > int(created_orders_all_time)

    @allure.title('Созданный заказ в процессе')
    def test_get_created_order_with_status_in_work(self, driver_firefox):
        main_page = MainPage(driver=driver_firefox)
        login_page = LoginAndRegistrationPage(driver=driver_firefox)
        order_list_page = OrderListPage(driver=driver_firefox)
        main_page.click_on_element_text_personal_cabinet()
        login_page.wait_to_be_open_login_page()
        login_page.add_email()
        login_page.add_password()
        login_page.click_login_button()
        main_page.wait_to_be_open_main_page()
        main_page.drag_and_drop_bun()
        main_page.click_create_order_button()
        order_list_page.wait_to_be_open_created_order()
        created_order_num = order_list_page.wait_to_get_actual_order_number()
        main_page.wait_to_click_close_cross()
        main_page.click_on_close_cross()
        main_page.click_on_orders_list()
        order_list_page.wait_to_click_on_order()
        in_work_order = order_list_page.get_order_in_work(expected_value=created_order_num)
        assert in_work_order == f'0{created_order_num}'
