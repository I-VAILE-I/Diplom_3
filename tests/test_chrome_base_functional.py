import allure
from data import Urls, ExpectedResults
from pages.login_and_registration_page import LoginAndRegistrationPage
from pages.main_page import MainPage
from pages.orders_list_page import OrderListPage
from pages.personal_cabinet_page import PersonalCabinetPage


@allure.suite('Проверка базовой функциональности Chrome')
class TestBaseFunctionalPagesChrome:

    @allure.title('Проверяем переход в "Конструктор"')
    def test_open_constructor_from_personal_cabinet(self, driver_chrome):
        main_page_base = MainPage(driver=driver_chrome)
        main_page_base.click_on_text_personal_cabinet()
        login_base_functional = LoginAndRegistrationPage(driver=driver_chrome)
        login_base_functional.wait_to_be_open_login_page()
        login_base_functional.add_email()
        login_base_functional.add_password()
        login_base_functional.click_login_button()
        main_page_base.wait_to_click_personal_cabinet()
        main_page_base.click_on_text_personal_cabinet()
        personal_cabinet_page = PersonalCabinetPage(driver=driver_chrome)
        personal_cabinet_page.wait_to_be_open_profile_page()
        main_page_base.click_on_constructor()
        assert main_page_base.get_current_urls() == Urls.main_page_url_after_login

    @allure.title('Проверяем переход в "Лента заказов"')
    def test_open_orders_list_from_main_page(self, driver_chrome):
        main_page_base = MainPage(driver=driver_chrome)
        main_page_base.click_on_orders_list()
        assert main_page_base.get_current_urls() == Urls.orders_list

    @allure.title('Проверяем информацию о булочке')
    def test_open_bun_info_and_close(self, driver_chrome):
        main_page_base = MainPage(driver=driver_chrome)
        main_page_base.open_info_about_bun()
        bun_name = main_page_base.get_bun_name()
        main_page_base.click_on_close_cross()
        assert bun_name == ExpectedResults.bun_name

    @allure.title('Перетаскиваем булочку в конструктор')
    def test_drag_and_drop_bun_to_constructor(self, driver_chrome):
        main_page_base = MainPage(driver=driver_chrome)
        main_page_base.drag_and_drop_bun()
        assert main_page_base.get_bun_counter() == ExpectedResults.bun_count

    @allure.title('Проверяем, залогиненный пользователь оформляет заказ')
    def test_make_order_for_authorized_user(self, driver_chrome):
        main_page_base = MainPage(driver=driver_chrome)
        main_page_base.click_on_text_personal_cabinet()
        login_base_functional = LoginAndRegistrationPage(driver=driver_chrome)
        login_base_functional.wait_to_be_open_login_page()
        login_base_functional.add_email()
        login_base_functional.add_password()
        login_base_functional.click_login_button()
        main_page_base.wait_to_be_open_main_page()
        main_page_base.drag_and_drop_bun()
        main_page_base.click_create_order_button()
        order_list_page = OrderListPage(driver=driver_chrome)
        order_list_page.wait_to_be_open_created_order()
        assert main_page_base.get_order_status() == ExpectedResults.order_status

    @allure.title('Проверяем, не залогиненный пользователь не может оформить заказ')
    def test_cant_make_order_for_not_authorized_user(self, driver_chrome):
        main_page_base = MainPage(driver=driver_chrome)
        main_page_base.drag_and_drop_bun()
        main_page_base.click_create_order_button()
        login_base_functional = LoginAndRegistrationPage(driver=driver_chrome)
        login_base_functional.wait_to_be_open_login_page()
        assert login_base_functional.get_current_urls() == Urls.login_url
