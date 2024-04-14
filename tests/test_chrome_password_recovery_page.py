import allure

from data import Urls, ExpectedResults
from pages.recovery_password_page import RecoveryPasswordPage


@allure.suite('Проверка страницы восставновления пароля в Chrome')
class TestForgotPasswordPagesChrome:

    @allure.title('Проверяем заход на страницу "Восстановление пароля"')
    def test_open_forgot_password_page_click_on_personal_cabinet(self, driver_chrome):
        recovery_password_page = RecoveryPasswordPage(driver=driver_chrome)
        recovery_password_page.click_on_text_personal_cabinet()
        recovery_password_page.click_on_recovery_password_text()
        assert recovery_password_page.get_current_urls() == Urls.forgot_password_url

    @allure.title('Проверяем заход на страницу "Восстановление пароля"')
    def test_open_forgot_password_page_click_on_login_button(self, driver_chrome):
        recovery_password_page = RecoveryPasswordPage(driver=driver_chrome)
        recovery_password_page.click_on_login_button()
        recovery_password_page.click_on_recovery_password_text()
        assert recovery_password_page.get_current_urls() == Urls.forgot_password_url

    @allure.title('Проверяем заход на страницу "Замена пароля"')
    def test_open_reset_password_page(self, driver_chrome):
        recovery_password_page = RecoveryPasswordPage(driver=driver_chrome)
        recovery_password_page.click_on_login_button()
        recovery_password_page.click_on_recovery_password_text()
        recovery_password_page.add_email()
        recovery_password_page.click_on_recovery_pawword_button()
        recovery_password_page.wait_to_be_open_reset_password_page()
        assert recovery_password_page.get_current_urls() == Urls.reset_password_url

    @allure.title('Проверяем веведнный пароль скрыт')
    def test_input_new_password_and_check_is_not_visible(self, driver_chrome):
        recovery_password_page = RecoveryPasswordPage(driver=driver_chrome)
        recovery_password_page.click_on_login_button()
        recovery_password_page.click_on_recovery_password_text()
        recovery_password_page.add_email()
        recovery_password_page.click_on_recovery_pawword_button()
        recovery_password_page.wait_to_be_open_reset_password_page()
        recovery_password_page.add_new_password()
        assert recovery_password_page.get_password_field_status() == ExpectedResults.not_visible_password

    @allure.title('Проверяем веведнный пароль не скрыт')
    def test_input_new_password_and_check_is_visible(self, driver_chrome):
        recovery_password_page = RecoveryPasswordPage(driver=driver_chrome)
        recovery_password_page.click_on_login_button()
        recovery_password_page.click_on_recovery_password_text()
        recovery_password_page.add_email()
        recovery_password_page.click_on_recovery_pawword_button()
        recovery_password_page.wait_to_be_open_reset_password_page()
        recovery_password_page.add_new_password()
        recovery_password_page.make_password_visible()
        assert recovery_password_page.get_password_field_status() == ExpectedResults.visible_password
