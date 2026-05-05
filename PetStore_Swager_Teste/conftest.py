import pytest
from PetStore_Swager_Teste.base_test import BaseTest
from utils.pet_factory import PETS_PRE_DEFINIDOS, criar_pet

@pytest.fixture(scope="session", autouse=True)
def auth():
   pass

@pytest.fixture(scope="session")
def api():
    return BaseTest()

@pytest.fixture(scope="session", autouse=True)
def criar_pets_iniciais():
    """Cria os 5 pets pré-definidos uma vez antes de todos os testes."""
    api = BaseTest()
    ids_criados = []

    for pet in PETS_PRE_DEFINIDOS:
        response = api.post("/pet", json=pet)
        assert response.status_code == 200, f"Falha ao criar pet {pet['name']}"
        ids_criados.append(response.json()["id"])
        print(f"Pet criado: {pet['name']} — ID: {response.json()['id']}")

    return ids_criados