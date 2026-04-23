import os
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

cliente={
    "username":os.getenv("USERNAME"),
    "password":os.getenv("PASSWORD"),
    "nome":os.getenv("NOME"),
    "sobrenome":os.getenv("SOBRENOME"),
    "CEP":os.getenv("CEP")
}

def main(cliente=cliente, service=service, driver=driver):
    pass
if __name__ == "__main__":
    main()