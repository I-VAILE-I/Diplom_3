import allure

from data import Urls
from pages.personal_cabinet_page import PersonalCabinetPage


@allure.suite('Проверка персонального кабинета в Firefox')
class TestPersonalCabinetPageFirefox:

    @allure.title('Проверяем авторизацию')
    def test_authorization(self, driver_firefox):
        authorization = PersonalCabinetPage(driver=driver_firefox)
        authorization.wait_500_ms()
        authorization.click_on_text_personal_cabinet()
        authorization.add_email()
        authorization.add_password()
        authorization.click_login_button()
        authorization.wait_to_be_open_main_page()
        assert authorization.get_current_urls() == Urls.main_page_url_after_login

    @allure.title('Проверяем заход в профиль')
    def test_go_to_personal_cabinet(self, driver_firefox):
        authorization = PersonalCabinetPage(driver=driver_firefox)
        authorization.wait_500_ms()
        authorization.click_on_text_personal_cabinet()
        authorization.add_email()
        authorization.add_password()
        authorization.click_login_button()
        authorization.wait_to_be_open_main_page()
        authorization.wait_500_ms()
        authorization.click_on_text_personal_cabinet()
        authorization.wait_to_be_open_profile_page()
        assert authorization.get_current_urls() == Urls.profile_page_url

    @allure.title('Проверяем историю заказов в профиле')
    def test_go_to_orders_history(self, driver_firefox):
        authorization = PersonalCabinetPage(driver=driver_firefox)
        authorization.wait_500_ms()
        authorization.click_on_text_personal_cabinet()
        authorization.add_email()
        authorization.add_password()
        authorization.click_login_button()
        authorization.wait_to_be_open_main_page()
        authorization.wait_500_ms()
        authorization.click_on_text_personal_cabinet()
        authorization.wait_to_be_open_profile_page()
        authorization.wait_500_ms()
        authorization.click_on_orders_history()
        assert authorization.get_current_urls() == Urls.orders_history

    @allure.title('Проверяем выход из профиля')
    def test_logout(self, driver_firefox):
        authorization = PersonalCabinetPage(driver=driver_firefox)
        authorization.wait_500_ms()
        authorization.click_on_text_personal_cabinet()
        authorization.add_email()
        authorization.add_password()
        authorization.click_login_button()
        authorization.wait_to_be_open_main_page()
        authorization.wait_500_ms()
        authorization.click_on_text_personal_cabinet()
        authorization.wait_to_be_open_profile_page()
        authorization.wait_500_ms()
        authorization.click_logout_button()
        authorization.wait_to_be_open_login_page()
        assert authorization.get_current_urls() == Urls.login_url
