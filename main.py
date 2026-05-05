import subprocess
import os

class Main:

    def __init__(self):
        self.raiz = os.path.dirname(os.path.abspath(__file__))

    def rodar_petstore(self):
        print("======= Iniciando testes da API PetStore =======\n")
        subprocess.run(
            "python -m pytest PetStore_Swager_Teste/ -v -s",
            shell=True,
            cwd=self.raiz
        )
        print("======= Testes PetStore finalizados =======\n")

    def rodar_sauce(self):
        print("======= Iniciando automação Sauce =======\n")
        subprocess.run(
            ["python", os.path.join(self.raiz, "automacao_sauce", "main.py")],
            cwd=self.raiz
        )
        print("======= Automação Sauce finalizada =======\n")

    def execute(self):
        self.rodar_petstore()
        self.rodar_sauce()


if __name__ == "__main__":
    main = Main()
    main.execute()