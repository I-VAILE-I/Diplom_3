from selenium.webdriver.common.by import By


class LoginAndRegistrationPageLocators:
    registration_input_name = [By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']"]
    registration_input_email = [By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"]
    registration_input_password = [By.XPATH, "//input[@name='Пароль']"]
    login_input_email = [By.XPATH, "//input[@name='name']"]
    login_input_password = [By.XPATH, "//input[@name='Пароль']"]
    login_button = [By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]
    login_button_on_registration_page = [By.XPATH, "//a[@class='Auth_link__1fOlj']"]
    login_button_on_recovery_password_page = [By.XPATH, "//a[@class='Auth_link__1fOlj']"]
    error_input = [By.XPATH, "//p[@class='input__error text_type_main-default']"]
    open_registration_on_login_page = [By.XPATH, "//a[@class='Auth_link__1fOlj']"]
    click_on_registration_button = [By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]
    forgot_password_button = [By.XPATH, "//a[@href='/forgot-password']"]
    input_new_password = [By.XPATH, "//input[@name='Введите новый пароль']"]
    make_new_password_visible = [By.XPATH, "//div[@class='input__icon input__icon-action']"]
    logout_button = [By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"]
    orders_history = [By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']"]
