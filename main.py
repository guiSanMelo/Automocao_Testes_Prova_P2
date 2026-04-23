from compras_automacao import *
from utils import *
import os
from dotenv import load_dotenv

class Main:

    def __init__(self):
        pass

    util = Utils()

    def programa(self):
        try:
            load_dotenv()
            _operacao = Operacao()

            _cliente = Cliente(
                username=os.getenv("USERNAME"),
                password=os.getenv("PASSWORD"),
                nome=os.getenv("NOME"),
                sobrenome=os.getenv("SOBRENOME"),
                cep=os.getenv("CEP")
                )

            service=Service(ChromeDriverManager().install())
            driver=webdriver.Chrome(service=service)

            _operacao.abrir_site(driver)
            _operacao.login(_cliente, driver)
        except Exception as e:
            self.util.error_message("Main-programa", e)
        finally:
            print("programa fechado")
            driver.quit()

if __name__ == "__main__":
    main = Main() 
    main.programa()
        