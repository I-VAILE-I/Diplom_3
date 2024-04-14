from selenium.webdriver.common.by import By


class OrdersListLocators:
    order = [By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']"]
    order_information = [By.XPATH, "(//p[@class='undefined text text_type_main-default mb-15'])[1]"]
    created_orders_for_all_time = [By.XPATH, "//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]/div[last()-1]"]
    created_orders_for_today = [By.XPATH, "//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]/div[last()]"]
    in_work = [By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"]
    created_order_number = [By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"]
