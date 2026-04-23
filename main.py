from compras_automacao import Cliente, Operacao
from utils import Utils
import os
from dotenv import load_dotenv
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


class Main:

    def __init__(self):
        pass

    util = Utils()

    def programa(self):
        try:
            load_dotenv()
            _operacao = Operacao()

            _cliente = Cliente(
                username=os.getenv("SAUCE_USERNAME"),
                password=os.getenv("SAUCE_PASSWORD"),
                nome=os.getenv("NOME"),
                sobrenome=os.getenv("SOBRENOME"),
                cep=os.getenv("CEP")
            )

            service=Service(ChromeDriverManager().install())
            driver=webdriver.Chrome(service=service)

            _operacao.abrir_site(driver)
            _operacao.login(_cliente, driver)

            _operacao.apertar_botao(driver, botao_id="login-button")

            
        except Exception as e:
            self.util.error_message("Main-programa", e)
        finally:
            print("programa fechado")
            driver.quit()

if __name__ == "__main__":
    main = Main() 
    main.programa()
        