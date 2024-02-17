import data
from selenium import webdriver
from urban_routes_page import UrbanRoutesPage

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
        blanket_element = self.routes_page.look_for_blanket()
        assert blanket_element.text == 'Manta y pañuelos'

# 3. Prueba para rellenar el número de teléfono.
    def test_fill_phone_number(self):
        self.routes_page.click_phone_number()
        self.routes_page.fill_out_phone_number()
        self.routes_page.click_next_button()
        get_placeholder = self.routes_page.look_for_code_field().get_attribute('placeholder')
        assert get_placeholder == 'xxxx'

# 4. Prueba para Agregar una tarjeta de crédito.
    def test_add_credit_card(self):
        self.routes_page.enter_code()
        self.routes_page.click_confirm_button()
        self.routes_page.click_pay_button()
        self.routes_page.click_add_card()
        self.routes_page.input_card_number()
        self.routes_page.input_card_code()
        self.routes_page.click_card_number_label()
        self.routes_page.click_link_button()
        new_card_checkmark = self.routes_page.look_new_card_checkmark()
        assert new_card_checkmark.get_attribute('class') == 'checkmark'

# 5. Prueba para escribir un mensaje para el controlador.
    def test_input_comment(self):
        self.routes_page.click_close_button()
        self.routes_page.wait_comment_button()
        self.routes_page.input_comment()
        comment = self.routes_page.look_for_comment()
        assert comment.get_attribute('value') == data.message_for_driver

# 6. Prueba para pedir una manta y pañuelos
    def test_ask_blanket_and_handkerchiefs(self):
        self.routes_page.click_slider_round()
        slider_element = self.routes_page.look_for_slider_round()
        assert slider_element.get_attribute('class') == 'slider round'

# 7. Prueba para pedir 2 helados
    def test_ask_two_ice_creams(self):
        self.routes_page.ask_two_ice_creams()
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
        driver_name_icon = self.routes_page.look_for_driver_icon()
        assert driver_name_icon.get_attribute('alt') == 'close'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
