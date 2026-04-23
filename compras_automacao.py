import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

class Cliente:

    def __init__(self, username, password, nome, sobrenome, cep):
        self.username=username
        self.password=password
        self.nome=nome
        self.sobrenome=sobrenome
        self.cep=cep
        pass


class Operacao(Cliente):

    user-name = 0
    password = 0

    def abrir_site(driver:webdriver.Chrome):
        try:
            driver.get("https://www.saucedemo.com/")
            print("site aberto")
            pass
        except:
            print("não foi possível abrir o site!")
            pass
        pass

    def login(cliente:Cliente):

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


    abrir_site()

