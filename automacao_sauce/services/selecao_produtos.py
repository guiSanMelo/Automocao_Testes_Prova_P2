from selenium import webdriver
from utils.messages import Messages
from utils.actions import Actions
from models.cliente import Cliente
from selenium.webdriver.common.by import By
from models.cliente import Cliente
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
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
        try:
            
            wait = WebDriverWait(driver, 5)
            button = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory")))
            produto = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))

            for button, produto in zip(button, produto):
                nome = produto.text
                button.click()
                print(F"--Poduto adicionado ao carrinho: ", nome)
                driver.implicitly_wait(2)
                pass

            self.messages.correct_message("Produtos selecionados")
            driver.implicitly_wait(10)
            
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

    def ir_checkout(self, driver:webdriver.Chrome, cliente:Cliente):
        try:
            self.verificar_produtos(driver, cliente)

            wait = WebDriverWait(driver, 15)
            button = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
            button.click()
            sleep(10)
            self.messages.correct_message("ir para o checkout")
            pass
        except Exception as e:
            self.messages.error_message("verificação dos produtos", e)


    def verificar_produtos(self, driver:webdriver.Chrome, cliente:Cliente):
        try:
            produtos = self.listar_produtos(driver)
            if not produtos:
                return
            preco_total = sum(p["preco"] for p in produtos)

            while preco_total > cliente.orcamento and len(produtos)>1:
                produtos = self.remover_produto(driver, produtos)
                if produtos:
                    preco_total = sum(p["preco"] for p in produtos)
                else:
                    break
            pass
            sleep(10)
        except Exception as e:
            self.messages.error_message("verificação dos produtos", e)
    pass

    def listar_produtos(self, driver: webdriver.Chrome):
        try:
            wait = WebDriverWait(driver, 15)
            itens = wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
            )
            produtos = []

            for item in itens:
                nome = item.find_element(By.CLASS_NAME, "inventory_item_name").text
                preco = float(
                    item.find_element(By.CLASS_NAME, "inventory_item_price")
                    .text.replace("$", "")
                )
                botao = item.find_element(By.CLASS_NAME, "cart_button")

                produtos.append({
                    "nome": nome,
                    "preco": preco,
                    "botao": botao
                })
            return produtos
        except Exception as e:
            self.messages.error_message("listar os produtos", e)
            return []

    def remover_produto(self, driver:webdriver.Chrome, lista_produtos:list[dict]):
        try: 
            item_mais_caro = max(lista_produtos, key=lambda x: x["preco"])
            item_mais_caro["botao"].click()
            lista_produtos.remove(item_mais_caro)
            self.messages.correct_message(f"remover produto {item_mais_caro['nome']}")
            return lista_produtos
        except Exception as e:
            self.messages.error_message(f"remover produto", e)
        

