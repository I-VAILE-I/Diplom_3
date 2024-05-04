from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    def standard_click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text

    def get_orders_in_work(self, locator, expected_value):
        WebDriverWait(self.driver, 25).until(
            lambda driver: driver.find_element(*locator).text == f'0{expected_value}'
        )
        return self.driver.find_element(*locator).text

    def get_order_numbers(self, locator, default_value):
        WebDriverWait(self.driver, 25).until(
            lambda driver: driver.find_element(*locator).text != default_value
        )
        return self.driver.find_element(*locator).text

    def text_on_page(self):
        return self.driver.page_source

    def input_text_in_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_password_field_activity(self, locator):
        return self.driver.find_element(*locator).get_attribute('type')

    def wait_to_open_new_tab(self, title):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(title))

    def wait_to_click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def wait_to_visible_on_element(self, locator):
        WebDriverWait(self.driver, 35).until(EC.visibility_of_element_located(locator))

    def wait_to_invisibil_on_element(self, locator):
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element(locator))

    def wait_to_element_invisible(self, locator):
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator))

    def drag_and_drop(self, locator_to_drag, locator_to_drop):
        source = self.driver.find_element(*locator_to_drag)
        target = self.driver.find_element(*locator_to_drop)
        drag_and_drop(self.driver, source, target)

    def script_to_click(self, locator_to_drag, locator_to_drop):
        source = self.driver.find_element(*locator_to_drag)
        target = self.driver.find_element(*locator_to_drop)
        drag_and_drop(self.driver, source, target)

    def get_current_urls(self):
        return self.driver.current_url
