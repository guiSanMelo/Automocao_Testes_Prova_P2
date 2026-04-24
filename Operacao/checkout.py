from selenium import webdriver
from utils.messages import Messages
from utils.actions import Actions
from models.cliente import Cliente
from selenium.webdriver.common.by import By
from models.cliente import Cliente
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Checkout:

    def __init__(self):
        self.messages = Messages()
        self.actions = Actions()
        pass

    def checkout(self):
        pass

    def checkout_produtos(self):
        pass

    def checkout_informocoes(self):
        pass

    def checkout_precos(self):
        pass

    pass