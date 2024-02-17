import data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from retrieve_phone_code import retrieve_phone_code
import importlib

class UrbanRoutesPage:
    selector = importlib.import_module('selector')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.selector.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.selector.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.selector.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.selector.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(self.selector.map))
        self.set_from(from_address)
        self.set_to(to_address)

    def wait_ask_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.selector.ask_taxi))

    def click_ask_taxi(self):
        self.driver.find_element(*self.selector.ask_taxi).click()

    def click_tariff_comfort(self):
        self.driver.find_element(*self.selector.select_comfort_tariff).click()

    def look_for_blanket(self):
        return self.driver.find_element(*self.selector.blanket)

    def click_phone_number(self):
        self.driver.find_element(*self.selector.phone_number_field).click()

    def fill_out_phone_number(self):
        self.driver.find_element(*self.selector.input_phone).send_keys(data.phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.selector.next_button).click()

    def look_for_code_field(self):
        return self.driver.find_element(*self.selector.code_element)

    def enter_code(self):
        code = retrieve_phone_code(driver=self.driver)
        self.driver.find_element(*self.selector.code_element).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.selector.confirm_button).click()

    def click_pay_button(self):
        self.driver.find_element(*self.selector.pay_button).click()

    def click_add_card(self):
        self.driver.find_element(*self.selector.add_card_button).click()

    def input_card_number(self):
        self.driver.find_element(*self.selector.card_input).send_keys(data.card_number)

    def input_card_code(self):
        self.driver.find_element(*self.selector.code_input).send_keys(data.card_code)

    def click_card_number_label(self):
        self.driver.find_element(*self.selector.card_number_label).click()

    def click_link_button(self):
        self.driver.find_element(*self.selector.link_button).click()

    def look_new_card_checkmark(self):
        return self.driver.find_element(*self.selector.checkmark)

    def click_close_button(self):
        self.driver.find_element(*self.selector.close_button).click()

    def wait_comment_button(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(self.selector.comment))

    def input_comment(self):
        self.driver.find_element(*self.selector.comment).send_keys(data.message_for_driver)

    def look_for_comment(self):
        return self.driver.find_element(*self.selector.comment)

    def click_slider_round(self):
        element = self.driver.find_element(*self.selector.slider_round)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def look_for_slider_round(self):
        return self.driver.find_element(*self.selector.slider_round)

    def ask_two_ice_creams(self):
        self.driver.find_element(*self.selector.counter_plus).click()
        self.driver.find_element(*self.selector.counter_plus).click()

    def look_for_counter_plus_disabled(self):
        return self.driver.find_element(*self.selector.counter_plus)

    def click_ask_taxi_button(self):
        self.driver.find_element(*self.selector.ask_taxi_button).click()

    def look_for_timer(self):
        return self.driver.find_element(*self.selector.timer)

    def wait_driver_icon(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(self.selector.driver_icon))

    def look_for_driver_icon(self):
        return self.driver.find_element(*self.selector.driver_icon)
