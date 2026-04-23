from compras_automacao import *
import os
from dotenv import load_dotenv

def main():
    load_dotenv()

    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)

    Operacao.abrir_site(driver=driver)
    Operacao.login()
    pass

if __name__ == "__main__":
    main()