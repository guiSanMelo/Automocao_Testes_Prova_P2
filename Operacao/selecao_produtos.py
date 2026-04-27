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
            wait = WebDriverWait(driver, 20)
            button = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory")))
            for button in button:
                button.click()
                produto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
                print(F"--Poduto adicionado ao carrinho: ", produto)
            
            self.messages.correct_message("Produtos selecionados")
            driver.implicitly_wait(30)
            pass
        except Exception as e:
            self.messages.error_message("Seleção de Produtos", e)
        pass

    def ir_carrinho(self):
        pass

    def posso_gastar(self, preco_total:int, orcamento_cliente:int):
        if preco_total<=orcamento_cliente:
            return True
        else:
            return False
    pass