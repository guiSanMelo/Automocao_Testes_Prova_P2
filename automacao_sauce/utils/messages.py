from selenium import webdriver
from selenium.webdriver.common.by import By  
class Messages:

    def __init__(self):
        pass

    def correct_message(self, campo:str):
        print(f"{campo} deu certo!")
        pass

    def error_message(self, campo:str, e:Exception):
        print(f"Erro em {campo}:")
        print(f"Detalhe do erro: {e}")  
        pass

    