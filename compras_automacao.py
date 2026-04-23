from utils import Utils
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

    def __init__(self, username, password, nome, sobrenome, cep, orcamento:float=75):
        self.username=username
        self.password=password
        self.nome=nome
        self.sobrenome=sobrenome
        self.cep=cep
        self.orcamento = orcamento
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
            driver.implicitly_wait(20)
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

            driver.implicitly_wait(20)
            self.util.correct_message("Fazer login")
        except Exception as e:
            self.util.error_message("Fazer login", e)
        pass

    def apertar_botao(self, driver:webdriver.Chrome, botao_id:str|None=None, botao_class:str|None=None):
        try:
            if botao_id is not None:
                botao=driver.find_element(By.ID, f'{botao_id}')
                nome_botao=botao_id
                pass
            elif botao_class is not None:
                botao=driver.find_element(By.CLASS_NAME, f'{botao_class}')
                nome_botao=botao_class
                pass
            botao.click()
            driver.implicitly_wait(20)
            self.util.correct_message(f"Apertar {nome_botao}")
        except Exception as e:
            if botao_id is not None:
                nome_botao=botao_id
            elif botao_class is not None:
                nome_botao=botao_class
            self.util.error_message(f"Botão-{nome_botao}", e)
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


