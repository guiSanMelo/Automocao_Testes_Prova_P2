from selenium import webdriver
from utils.messages import Messages
from utils.actions import Actions
from models.cliente import Cliente
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class Tela_Login():

    def __init__(self):
        self.messages = Messages()
        self.actions = Actions()
        pass

    def abrir_site(self, driver:webdriver.Chrome):
        try:
            driver.get("https://www.saucedemo.com/")
            self.messages.correct_message("Abrir o site")
            #driver.implicitly_wait(5)
           
            pass
        except Exception as e:
            self.messages.error_message("Abrir o site", e)
            pass
        pass

    def credenciais_login(self, cliente:Cliente, driver:webdriver.Chrome):
        try:
            wait = WebDriverWait(driver, 5)

            campo_username = wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
            campo_username.send_keys(cliente.username)

            driver.find_element(By.ID, 'password').send_keys(cliente.password)

            driver.implicitly_wait(5)
            self.actions.apertar_botao(driver, botao_id="login-button")
            driver.forward()
            self.messages.correct_message("Fazer login")
        except Exception as e:
            self.messages.error_message("Fazer login", e)
        pass