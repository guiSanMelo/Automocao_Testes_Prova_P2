import os
import subprocess
class Main:

    def __init__(self):
        pass

    def execute(self):
        subprocess.run("python -m pytest -v -s", shell=True)
       #subprocess.run("python -m pytest -v -s PetStore_Swager_Teste/tests/test_store.py", shell=True)


if __name__ == "__main__":
    main = Main()
    main.execute()