from selenium import webdriver
from selenium.webdriver.common.by import By  
class Utils:

    def __init__(self):
        pass

    def correct_message(self, campo:str):
        print(f"{campo} deu certo!")
        pass

    def error_message(self, campo:str, e:Exception):
        print(f"Erro em {campo}:")
        print(f"Detalhe do erro: {e}")  
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
            self.correct_message(f"Apertar {nome_botao}")
        except Exception as e:
            if botao_id is not None:
                nome_botao=botao_id
            elif botao_class is not None:
                nome_botao=botao_class
            self.error_message(f"Botão-{nome_botao}", e)
            pass