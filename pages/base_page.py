import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from seletools.actions import drag_and_drop


@allure.suite('Проверка разделов "Вопросы о важном" на главной странице в Firefox')
class BasePage:

    def __int__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def get_text_element(self, locator):
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
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    def wait_to_element_invisible(self, locator):
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator))

    def drag_and_drop(self, locator_to_drag, locator_to_drop):
        source = self.driver.find_element(*locator_to_drag)
        target = self.driver.find_element(*locator_to_drop)
        drag_and_drop(self.driver, source, target)

    def get_current_urls(self):
        return self.driver.current_url
