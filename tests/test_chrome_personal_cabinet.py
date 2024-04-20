import allure

from data import Urls
from pages.login_and_registration_page import LoginAndRegistrationPage
from pages.main_page import MainPage
from pages.personal_cabinet_page import PersonalCabinetPage


@allure.suite('Проверка персонального кабинета в Chrome')
class TestPersonalCabinetPageChrome:

    @allure.title('Проверяем авторизацию')
    def test_authorization(self, driver_chrome):
        login_page = LoginAndRegistrationPage(driver=driver_chrome)
        main_page = MainPage(driver=driver_chrome)
        main_page.click_on_text_personal_cabinet()
        login_page.add_email()
        login_page.add_password()
        login_page.click_login_button()
        main_page.wait_to_be_open_main_page()
        assert main_page.get_current_urls() == Urls.main_page_url_after_login

    @allure.title('Проверяем заход в профиль')
    def test_go_to_personal_cabinet(self, driver_chrome):
        login_page = LoginAndRegistrationPage(driver=driver_chrome)
        main_page = MainPage(driver=driver_chrome)
        personal_cabinet = PersonalCabinetPage(driver=driver_chrome)
        main_page.click_on_text_personal_cabinet()
        login_page.add_email()
        login_page.add_password()
        login_page.click_login_button()
        main_page.wait_to_be_open_main_page()
        main_page.click_on_text_personal_cabinet()
        personal_cabinet.wait_to_be_open_profile_page()
        assert personal_cabinet.get_current_urls() == Urls.profile_page_url

    @allure.title('Проверяем историю заказов в профиле')
    def test_go_to_orders_history(self, driver_chrome):
        login_page = LoginAndRegistrationPage(driver=driver_chrome)
        main_page = MainPage(driver=driver_chrome)
        personal_cabinet = PersonalCabinetPage(driver=driver_chrome)
        main_page.click_on_text_personal_cabinet()
        login_page.add_email()
        login_page.add_password()
        login_page.click_login_button()
        main_page.wait_to_be_open_main_page()
        main_page.click_on_text_personal_cabinet()
        personal_cabinet.wait_to_be_open_profile_page()
        personal_cabinet.click_on_orders_history()
        assert personal_cabinet.get_current_urls() == Urls.orders_history

    @allure.title('Проверяем выход из профиля')
    def test_logout(self, driver_chrome):
        login_page = LoginAndRegistrationPage(driver=driver_chrome)
        main_page = MainPage(driver=driver_chrome)
        personal_cabinet = PersonalCabinetPage(driver=driver_chrome)
        main_page.click_on_text_personal_cabinet()
        login_page.add_email()
        login_page.add_password()
        login_page.click_login_button()
        main_page.wait_to_be_open_main_page()
        main_page.click_on_text_personal_cabinet()
        personal_cabinet.wait_to_be_open_profile_page()
        personal_cabinet.click_logout_button()
        login_page.wait_to_be_open_login_page()
        assert personal_cabinet.get_current_urls() == Urls.login_url
