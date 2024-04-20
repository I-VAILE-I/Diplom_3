import allure

from data import Urls, ExpectedResults
from pages.login_and_registration_page import LoginAndRegistrationPage
from pages.main_page import MainPage


@allure.suite('Проверка страницы восставновления пароля в Firefox')
class TestForgotPasswordPagesFirefox:

    @allure.title('Проверяем заход на страницу "Восстановление пароля"')
    def test_open_forgot_password_page_click_on_personal_cabinet(self, driver_firefox):
        login_page = LoginAndRegistrationPage(driver=driver_firefox)
        main_page = MainPage(driver=driver_firefox)
        main_page.wait_to_be_invisible_loading_screen()
        main_page.click_on_text_personal_cabinet()
        login_page.click_on_recovery_password_text()
        assert login_page.get_current_urls() == Urls.forgot_password_url

    @allure.title('Проверяем заход на страницу "Восстановление пароля"')
    def test_open_forgot_password_page_click_on_login_button(self, driver_firefox):
        login_page = LoginAndRegistrationPage(driver=driver_firefox)
        main_page = MainPage(driver=driver_firefox)
        main_page.wait_to_be_invisible_loading_screen()
        main_page.wait_to_click_personal_cabinet()
        main_page.wait_500_ms()
        main_page.click_on_login_button()
        login_page.click_on_recovery_password_text()
        assert login_page.get_current_urls() == Urls.forgot_password_url

    @allure.title('Проверяем заход на страницу "Замена пароля"')
    def test_open_reset_password_page(self, driver_firefox):
        login_page = LoginAndRegistrationPage(driver=driver_firefox)
        main_page = MainPage(driver=driver_firefox)
        main_page.wait_to_be_invisible_loading_screen()
        main_page.click_on_login_button()
        login_page.click_on_recovery_password_text()
        login_page.add_email()
        login_page.click_on_recovery_password_button()
        login_page.wait_to_be_open_reset_password_page()
        assert login_page.get_current_urls() == Urls.reset_password_url

    @allure.title('Проверяем веведнный пароль скрыт')
    def test_input_new_password_and_check_is_not_visible(self, driver_firefox):
        login_page = LoginAndRegistrationPage(driver=driver_firefox)
        main_page = MainPage(driver=driver_firefox)
        main_page.wait_to_be_invisible_loading_screen()
        main_page.wait_to_click_personal_cabinet()
        main_page.click_on_login_button()
        login_page.click_on_recovery_password_text()
        login_page.add_email()
        login_page.click_on_recovery_password_button()
        login_page.wait_to_be_open_reset_password_page()
        login_page.add_new_password()
        assert login_page.get_password_field_status() == ExpectedResults.not_visible_password

    @allure.title('Проверяем веведнный пароль не скрыт')
    def test_input_new_password_and_check_is_visible(self, driver_firefox):
        login_page = LoginAndRegistrationPage(driver=driver_firefox)
        main_page = MainPage(driver=driver_firefox)
        main_page.wait_to_be_invisible_loading_screen()
        main_page.wait_to_click_personal_cabinet()
        main_page.wait_500_ms()
        main_page.click_on_login_button()
        login_page.click_on_recovery_password_text()
        login_page.add_email()
        login_page.click_on_recovery_password_button()
        login_page.wait_to_be_open_reset_password_page()
        login_page.add_new_password()
        login_page.wait_500_ms()
        login_page.make_password_visible()
        assert login_page.get_password_field_status() == ExpectedResults.visible_password
