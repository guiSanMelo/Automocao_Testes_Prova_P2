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

    def selecionar_produtos(self):
        #inventory_list -> Class
        #inventory_item -> Class
        #inventory_item_price -> Class
        #btn btn_primary btn_small btn_inventory -> Class
        try:
            
            pass
        except Exception as e:
            self.messages.error_message("Seleção de Produtos", e)
        pass

    def ir_carrinho(self, ):
        pass

    def posso_gastar(self, preco_total:int, orcamento_cliente:int):
        if preco_total<=orcamento_cliente:
            return True
        else:
            return False
    pass