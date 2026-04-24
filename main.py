import os
from utils.messages import Messages
from utils.actions import Actions
from Operacao.tela_login import Tela_Login
from models.cliente import Cliente
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Main:

    def __init__(self):
        self._messages = Messages()
        self._actions = Actions()
        self._login = Tela_Login()
        pass

    def programa(self):
        load_dotenv()
        
        cliente = Cliente(
            username=os.getenv("SAUCE_USERNAME"),
            password=os.getenv("SAUCE_PASSWORD"),
            nome=os.getenv("NOME"),
            sobrenome=os.getenv("SOBRENOME"),
            cep=os.getenv("CEP")
        )
        service=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service)

        try:
            self._login.abrir_site(driver)
            self._login.credenciais_login(cliente, driver)

        except Exception as e:
            self._messages.error_message("Main-programa", e)
        finally:
            print("programa fechado")
            driver.quit()

if __name__ == "__main__":
    main = Main() 
    main.programa()
        