from selenium import webdriver
from utils.messages import Messages
from utils.actions import Actions
from models.cliente import Cliente
from selenium.webdriver.common.by import By
from models.cliente import Cliente
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class Checkout:

    def __init__(self):
        self.messages = Messages()
        self.actions = Actions()
        pass

    def checkout_info(self, driver:webdriver.Chrome, cliente:Cliente):
        try:
            wait = WebDriverWait(driver, 15)
            first_name_campo = wait.until(
                EC.presence_of_element_located((By.ID, "first-name"))
            )

            first_name_campo.send_keys(cliente.nome)
            driver.find_element(By.ID, "last-name").send_keys(cliente.sobrenome) # -> Sobrenome
            sleep(2)
            driver.find_element(By.ID, "postal-code").send_keys(cliente.cep) # -> CEP
            sleep(2)
            self.messages.correct_message("checkout de informações")
            sleep(2)
            self.actions.apertar_botao(driver, botao_id="continue")
        except Exception as e:
            self.messages.error_message("Checkout das informações", e)

    def finalizar_compra(self, driver:webdriver.Chrome):
        try:
            sleep(5)
            self.actions.apertar_botao(driver, "finish")
            sleep(30)
        except Exception as e:
            self.messages.error_message("finalizar comprar", e)
    
    pass