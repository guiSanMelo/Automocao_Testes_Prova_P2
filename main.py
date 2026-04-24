import os
from utils import Utils
from dotenv import load_dotenv
from selenium import webdriver
from Operacao import Cliente, Tela_Login
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main:

    def __init__(self):
        pass

    def programa(self):
        load_dotenv()
        _util = Utils()
        _login = Tela_Login()
        _cliente = Cliente(
            username=os.getenv("SAUCE_USERNAME"),
            password=os.getenv("SAUCE_PASSWORD"),
            nome=os.getenv("NOME"),
            sobrenome=os.getenv("SOBRENOME"),
            cep=os.getenv("CEP")
        )
        service=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service)

        try:
            _login.abrir_site(driver)
            _login.credenciais_login(_cliente, driver)

            _util.apertar_botao(driver, botao_id="login-button")
        except Exception as e:
            _util.error_message("Main-programa", e)
        finally:
            print("programa fechado")
            driver.quit()

if __name__ == "__main__":
    main = Main() 
    main.programa()
        