
class Urls:
    main_page_url = "https://stellarburgers.nomoreparties.site"
    main_page_url_after_login = "https://stellarburgers.nomoreparties.site/"
    profile_page_url = "https://stellarburgers.nomoreparties.site/account/profile"
    forgot_password_url = "https://stellarburgers.nomoreparties.site/forgot-password"
    reset_password_url = "https://stellarburgers.nomoreparties.site/reset-password"
    login_url = "https://stellarburgers.nomoreparties.site/login"
    orders_history = "https://stellarburgers.nomoreparties.site/account/order-history"
    orders_list = "https://stellarburgers.nomoreparties.site/feed"


class TextData:
    email = 'andrew_5_000@ya.ru'
    password = '123456'


class ExpectedResults:
    not_visible_password = 'password'
    visible_password = 'text'
    bun_name = 'Флюоресцентная булка R2-D3'
    bun_count = '2'
    order_status = 'Ваш заказ начали готовить'
    order_status_in_list = 'Выполнен'
    order_status_in_list_in_work = 'В обработке'
    order_status_in_list_created = 'Создан'

default_order_value = '9999'
