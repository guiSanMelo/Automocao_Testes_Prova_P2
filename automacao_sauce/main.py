import os
from utils.messages import Messages
from utils.actions import Actions
from services.tela_login import Tela_Login
from services.selecao_produtos import Selecao_Produtos
from services.checkout import Checkout
from models.cliente import Cliente
from dotenv import load_dotenv

class Main:

    def __init__(self):
        load_dotenv()
        self._messages = Messages()
        self._actions = Actions()
        self._login = Tela_Login()
        self._inventario = Selecao_Produtos()
        self._checkout = Checkout()
        pass

    def programa(self):
        cliente = Cliente(
            username=os.getenv("SAUCE_USERNAME"),
            password=os.getenv("SAUCE_PASSWORD"),
            nome=os.getenv("SAUCE_NOME"),
            sobrenome=os.getenv("SAUCE_SOBRENOME"),
            cep=os.getenv("SAUCE_CEP"),
            orcamento=float(os.getenv("SAUCE_ORCAMENTO"))
        )

        driver = self._actions.setUp()
        try:
            self._login.abrir_site(driver)
            self._login.credenciais_login(cliente, driver)
            self._inventario.selecionar_produtos(driver, cliente)
            self._inventario.ir_carrinho(driver)
            self._inventario.ir_checkout(driver, cliente)
            self._checkout.checkout_info(driver, cliente)
            self._checkout.finalizar_compra(driver)
        except Exception as e:
            self._messages.error_message("Main-programa", e)
        finally:
            print("programa fechado")
            driver.quit()

if __name__ == "__main__":
    main = Main() 
    main.programa()
        