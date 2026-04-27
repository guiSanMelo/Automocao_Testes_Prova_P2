from selenium import webdriver
from utils.messages import Messages
from utils.actions import Actions
from models.cliente import Cliente
from selenium.webdriver.common.by import By
from models.cliente import Cliente
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Selecao_Produtos:
    
    def __init__(self):
        self.messages = Messages()
        self.actions = Actions()
        pass

    def entrar_inventário(self, driver:webdriver.Chrome):
        try:
            driver.get("https://www.saucedemo.com/inventory.html")
            self.messages.correct_message("Abrir inventário")
        except Exception as e:
            self.messages.error_message("Abrir inventário", e)
        pass

    def selecionar_produtos(self, driver:webdriver.Chrome, cliente:Cliente):
        #inventory_list -> Class
        #inventory_item -> Class
        #inventory_item_price -> Class
        #btn btn_primary btn_small btn_inventory -> Class
        #https://www.saucedemo.com/inventory.html
        try:
            wait = WebDriverWait(driver, 5)
            button = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory")))
            produto = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))

            for button, produto in zip(button, produto):
                if self.posso_gastar(preco_total=0, orcamento_cliente=cliente.orcamento) is False:
                    print("Você não tem mais dinheiro")
                    break 
                nome = produto.text
                button.click()
                print(F"--Poduto adicionado ao carrinho: ", nome)
                pass

            self.messages.correct_message("Produtos selecionados")
            driver.implicitly_wait(20)
            pass
        except Exception as e:
            self.messages.error_message("Seleção de Produtos", e)
        pass

    def ir_carrinho(self, driver:webdriver.Chrome):
        try:
            self.actions.apertar_botao(driver=driver, botao_class="shopping_cart_link")
            driver.implicitly_wait(10)
            self.messages.correct_message("ir para o carrinho")
            pass
        except Exception as e:
            self.messages.error_message("ir pro carrinho", e)
        pass

    def posso_gastar(self, preco_total:int, orcamento_cliente:int):
        if preco_total<=orcamento_cliente:
            return True
        else:
            return False
    pass