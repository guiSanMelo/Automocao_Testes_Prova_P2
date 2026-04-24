from selenium import webdriver
from .messages import *
from selenium.webdriver.common.by import By
from models.cliente import Cliente
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Actions:

    def __init__(self):
        self.messages = Messages()
        pass

    def achar_elemento(self, driver:webdriver.Chrome, elemento_id:str|None = None, elemento_class:str|None=None):
        try:
            if elemento_id is not None:
                elemento = driver.find_element(By.ID, f'{elemento_id}')
                elemento_nome = elemento_id
                pass
            elif elemento_class is not None:
                elemento = driver.find_element(By.CLASS_NAME, f'{elemento_class}')
                elemento_nome = elemento_class
                pass
            else:
                raise ValueError("É necessário fornecer botao_id ou botao_class")
            self.messages.correct_message(f'Achar {elemento_nome}')
            return elemento
        except Exception as e:
            if elemento_id is not None:
                nome_elemento = elemento_id
            elif elemento_class is not None:
                nome_elemento= elemento_class
            self.messages.error_message(f"{nome_elemento}", e)
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
            else:
                raise ValueError("É necessário fornecer botao_id ou botao_class")
            botao.click()
            driver.implicitly_wait(20)
            self.messages.correct_message(f"Apertar {nome_botao}")
        except Exception as e:
            if botao_id is not None:
                nome_botao=botao_id
            elif botao_class is not None:
                nome_botao=botao_class
            self.messages.error_message(f"Botão-{nome_botao}", e)
            pass
    pass