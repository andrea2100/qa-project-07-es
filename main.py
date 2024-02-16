import time
import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:
    # Elementos de la página:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    ask_taxi = (By.XPATH, "//button[@type='button' and @class='button round']")
    select_comfort_tariff = (By.CSS_SELECTOR, "img[src='/static/media/kids.27f92282.svg']")
    blanket = (By.CLASS_NAME, 'r-sw-label')
    phone_number_field = (By.CLASS_NAME, 'np-text')
    input_phone = (By.ID, 'phone')
    next_button = (By.XPATH, "//button[@type='submit' and text()='Siguiente']")
    code_element = (By.ID, 'code')
    confirm_button = (By.XPATH, "//button[@type='submit' and text()='Confirmar']")
    pay_button = (By.CLASS_NAME, 'pp-text')
    add_card_button = (By.XPATH, "//img[@src='/static/media/plus.d25b8941.svg' and @class='pp-plus' and @alt='plus']")
    cancel_button = (By.XPATH, "//button[@type='button' and text()='Cancelar']")
    card_input = (By.CLASS_NAME, 'card-input')
    code_input = (By.XPATH, "//input[@type='text' and @id='code' and @name='code' and @placeholder='12' and @class='card-input']")
    card_number_label = (By.XPATH, "//div[@class='card-number-label' and text()='Número de tarjeta (no la tuya):']")
    link_button = (By.XPATH, "//button[@class='button full' and text()='Enlace']")
    checkmark = (By.CLASS_NAME, 'checkmark')
    close_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    comment = (By.ID, 'comment')
    slider_round = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    counter_plus = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]')
    ask_taxi_button = (By.CLASS_NAME, 'smart-button-main')
    timer = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[1]/div/div[2]')
    driver_icon = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/img')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        time.sleep(3)
        self.set_from(from_address)
        self.set_to(to_address)

    def wait_ask_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.ask_taxi))

    def click_ask_taxi(self):
        self.driver.find_element(*self.ask_taxi).click()

    def click_tariff_comfort(self):
        self.driver.find_element(*self.select_comfort_tariff).click()

    def look_for_blanket(self):
        return self.driver.find_element(*self.blanket)
    def click_phone_number(self):
        self.driver.find_element(*self.phone_number_field).click()

    def fill_out_phone_number(self):
        self.driver.find_element(*self.input_phone).send_keys(data.phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def look_for_code_field(self):
        return self.driver.find_element(*self.code_element)

    def enter_code(self):
        code = retrieve_phone_code(driver=self.driver)
        self.driver.find_element(*self.code_element).send_keys(code)
    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click()

    def click_pay_button(self):
        self.driver.find_element(*self.pay_button).click()

    def click_add_card(self):
        self.driver.find_element(*self.add_card_button).click()

    def input_card_number(self):
        self.driver.find_element(*self.card_input).send_keys(data.card_number)

    def input_card_code(self):
        self.driver.find_element(*self.code_input).send_keys(data.card_code)

    def click_card_number_label(self):
        self.driver.find_element(*self.card_number_label).click()

    def click_link_button(self):
        self.driver.find_element(*self.link_button).click()

    def look_new_card_checkmark(self):
        return self.driver.find_element(*self.checkmark)

    def click_close_button(self):
        time.sleep(5)
        self.driver.find_element(*self.close_button).click()

    def input_comment(self):
        self.driver.find_element(*self.comment).send_keys(data.message_for_driver)

    def look_for_comment(self):
        return self.driver.find_element(*self.comment)

    def click_slider_round(self):
        element = self.driver.find_element(*self.slider_round)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def look_for_slider_round(self):
        return self.driver.find_element(*self.slider_round)

    def ask_two_ice_creams(self):
        time.sleep(2)
        self.driver.find_element(*self.counter_plus).click()
        self.driver.find_element(*self.counter_plus).click()

    def look_for_counter_plus_disabled(self):
        return self.driver.find_element(*self.counter_plus)

    def click_ask_taxi_button(self):
        self.driver.find_element(*self.ask_taxi_button).click()

    def look_for_timer(self):
        return self.driver.find_element(*self.timer)

    def wait_driver_icon(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(self.driver_icon))

    def look_for_driver_icon(self):
        return self.driver.find_element(*self.driver_icon)

# Clase de Pruebas para Urban Routes:
class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

# 1. Prueba para configurar la dirección.
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        self.driver.maximize_window()
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

# 2. Prueba para seleccionar la tarifa Comfort.
    def test_select_comfort_tax(self):
        self.routes_page.wait_ask_taxi_button()
        self.routes_page.click_ask_taxi()
        self.routes_page.click_tariff_comfort()
        time.sleep(1)
        blanket_element = self.routes_page.look_for_blanket()
        assert blanket_element.text == 'Manta y pañuelos'

# 3. Prueba para rellenar el número de teléfono.
    def test_fill_phone_number(self):
        self.routes_page.click_phone_number()
        time.sleep(1)
        self.routes_page.fill_out_phone_number()
        self.routes_page.click_next_button()
        time.sleep(2)
        get_placeholder = self.routes_page.look_for_code_field().get_attribute('placeholder')
        assert get_placeholder == 'xxxx'

# 4. Prueba para Agregar una tarjeta de crédito.
    def test_add_credit_card(self):
        self.routes_page.enter_code()
        time.sleep(1)
        self.routes_page.click_confirm_button()
        self.routes_page.click_pay_button()
        self.routes_page.click_add_card()
        time.sleep(2)
        self.routes_page.input_card_number()
        time.sleep(2)
        self.routes_page.input_card_code()
        time.sleep(2)
        self.routes_page.click_card_number_label()
        time.sleep(2)
        self.routes_page.click_link_button()
        new_card_checkmark = self.routes_page.look_new_card_checkmark()
        assert new_card_checkmark.get_attribute('class') == 'checkmark'

# 5. Prueba para escribir un mensaje para el controlador.
    def test_input_comment(self):
        self.routes_page.click_close_button()
        time.sleep(2)
        self.routes_page.input_comment()
        comment = self.routes_page.look_for_comment()
        assert comment.get_attribute('value') == data.message_for_driver

# 6. Prueba para pedir una manta y pañuelos
    def test_ask_blanket_and_handkerchiefs(self):
        time.sleep(2)
        self.routes_page.click_slider_round()
        slider_element = self.routes_page.look_for_slider_round()
        assert slider_element.get_attribute('class') == 'slider round'

# 7. Prueba para pedir 2 helados
    def test_ask_two_ice_creams(self):
        self.routes_page.ask_two_ice_creams()
        time.sleep(2)
        counter_plus_disabled_element = self.routes_page.look_for_counter_plus_disabled()
        assert counter_plus_disabled_element.get_attribute('class') == 'counter-plus disabled'

# 8. Prueba para que aparezca el modal para pedir un taxi
    def test_appears_modal(self):
        self.routes_page.click_ask_taxi_button()
        timer = self.routes_page.look_for_timer()
        assert timer.get_attribute('class') == 'order-header-time'

# 9. Prueba para esperar a que aparezca la información del conductor en el modal (opcional)
    def test_wait_driver_information(self):
        self.routes_page.wait_driver_icon()
        time.sleep(2)
        driver_name_icon = self.routes_page.look_for_driver_icon()
        assert driver_name_icon.get_attribute('alt') == 'close'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()





