from selenium.webdriver.common.by import By


class MainPageLocators:
    login_button_on_main_page = [By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"]
    constructor_selection = [By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2']"]
    personal_cabinet_text = [By.LINK_TEXT, "Личный Кабинет"]
    orders_list = [By.LINK_TEXT, "Лента Заказов"]
    first_bun = [By.CSS_SELECTOR, ".BurgerIngredient_ingredient__1TVf6"]
    cross_to_close = [By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
    order_animation_gif = [By.XPATH, "//img[@alt='tick animation']"]
    order_window = [By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']"]
    bun_name = [By.XPATH, "//p[@class='text text_type_main-medium mb-8']"]
    bun_count = [By.XPATH, "//p[@class='counter_counter__num__3nue1']"]
    main_page_loader = [By.XPATH, "//div[@class='Modal_modal__P3_V5']"]
    order_created = [By.XPATH, "//p[@class='undefined text text_type_main-small mb-2']"]
    constructor = [By.CSS_SELECTOR, ".BurgerConstructor_basket__29Cd7"]
    loading_screen_one = [By.XPATH, "(//div[@class='Modal_modal_overlay__x2ZCr'])[1]"]
    loading_screen_two = [By.XPATH, "(//div[@class='Modal_modal_overlay__x2ZCr'])[2]"]
    xpath_personal_cabinet = [By.XPATH, "(//a[@class='AppHeader_header__link__3D_hX'])[2]"]
    xpath_orders_list = [By.XPATH, "(//a[@class='AppHeader_header__link__3D_hX'])[1]"]
