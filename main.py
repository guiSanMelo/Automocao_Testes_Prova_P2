import os
import subprocess

class Main:

    def __init__(self):
        pass

    def execute(self):
        print("======= Automatização do teste da API PetStore =======\n")
        
        subprocess.run("python -m pytest -v -s", shell=True)
        
        print("======= Automatização do teste da API PetStore =======\n")
        
        subprocess.run(["python", "automacao_sauce/main.py"])


if __name__ == "__main__":
    main = Main()
    main.execute()