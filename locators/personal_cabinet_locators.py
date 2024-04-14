from selenium.webdriver.common.by import By


class PersonalCabinetPageLocators:
    logout_button = [By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"]
    main_page_logo = [By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']"]
    first_order = [By.XPATH, "//p[@class='text text_type_digits-default']"]
    last_order = [By.XPATH, "(//ul[contains(@class, 'OrderHistory_profileList__374GU OrderHistory_list__KcLDB')]/li)[last()]"]
