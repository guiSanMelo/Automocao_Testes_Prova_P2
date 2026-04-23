from utils import *
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cliente:

    def __init__(self, username, password, nome, sobrenome, cep):
        self.username=username
        self.password=password
        self.nome=nome
        self.sobrenome=sobrenome
        self.cep=cep
        pass


class Operacao():
    util = Utils()
    #user-name = 0
    #password = 0
    def __init__(self):
        pass

    def abrir_site(self, driver:webdriver.Chrome):
        try:
            driver.get("https://www.saucedemo.com/")
            self.util.correct_message("Abrir o site")
            pass
        except Exception as e:
            self.util.error_message("Abrir o site", e)
            pass
        pass

    def login(self, cliente:Cliente, driver:webdriver.Chrome):
        try:
            wait =  WebDriverWait(driver, 10)

            campo_username = wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
            campo_username.send_keys(cliente.username)

            driver.find_element(By.ID, 'password').send_keys(cliente.password)

            driver.find_element(By.ID, 'login-button').click()

            self.util.correct_message("Fazer login")

        except Exception as e:
            self.util.error_message("Fazer login", e)
        pass

    def selecionar_produtos():
        pass

    def ir_carrinho():
        pass

    def checkout():
        pass

    def checkout_produtos():
        pass

    def checkout_informocoes():
        pass

    def checkout_precos():
        pass

    def posso_gastar(preco_produto):
        pass


