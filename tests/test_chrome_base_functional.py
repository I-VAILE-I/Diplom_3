import allure
from data import Urls, ExpectedResults
from pages.base_functional_pages import BaseFunctionalPages


@allure.suite('Проверка базовой функциональности Chrome')
class TestBaseFunctionalPagesChrome:

    @allure.title('Проверяем переход в "Конструктор"')
    def test_open_constructor_from_personal_cabinet(self, driver_chrome):
        base_functional = BaseFunctionalPages(driver=driver_chrome)
        base_functional.click_on_text_personal_cabinet()
        base_functional.wait_to_be_open_login_page()
        base_functional.add_email()
        base_functional.add_password()
        base_functional.click_login_button()
        base_functional.click_on_text_personal_cabinet()
        base_functional.wait_to_be_open_profile_page()
        base_functional.click_on_constructor()
        assert base_functional.get_current_urls() == Urls.main_page_url_after_login

    @allure.title('Проверяем переход в "Лента заказов"')
    def test_open_orders_list_from_main_page(self, driver_chrome):
        base_functional = BaseFunctionalPages(driver=driver_chrome)
        base_functional.click_on_orders_list()
        assert base_functional.get_current_urls() == Urls.orders_list

    @allure.title('Проверяем информацию о булочке')
    def test_open_bun_info_and_close(self, driver_chrome):
        base_functional = BaseFunctionalPages(driver=driver_chrome)
        base_functional.open_info_about_bun()
        bun_name = base_functional.get_bun_name()
        base_functional.close_info_about_bun()
        assert bun_name == ExpectedResults.bun_name

    @allure.title('Перетаскиваем булочку в конструктор')
    def test_drag_and_drop_bun_to_constructor(self, driver_chrome):
        base_functional = BaseFunctionalPages(driver=driver_chrome)
        base_functional.drag_and_drop_bun()
        assert base_functional.get_bun_counter() == ExpectedResults.bun_count

    @allure.title('Проверяем, залогиненный пользователь оформляет заказ')
    def test_make_order_for_authorized_user(self, driver_chrome):
        base_functional = BaseFunctionalPages(driver=driver_chrome)
        base_functional.click_on_text_personal_cabinet()
        base_functional.wait_to_be_open_login_page()
        base_functional.add_email()
        base_functional.add_password()
        base_functional.click_login_button()
        base_functional.wait_to_be_open_main_page()
        base_functional.drag_and_drop_bun()
        base_functional.click_create_order_button()
        assert base_functional.get_order_status() == ExpectedResults.order_status

    @allure.title('Проверяем, не залогиненный пользователь не может оформить заказ')
    def test_make_order_for_not_authorized_user(self, driver_chrome):
        base_functional = BaseFunctionalPages(driver=driver_chrome)
        base_functional.drag_and_drop_bun()
        base_functional.click_create_order_button()
        assert base_functional.get_current_urls() == Urls.login_url
