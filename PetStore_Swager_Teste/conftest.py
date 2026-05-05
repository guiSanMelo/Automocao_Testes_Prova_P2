import pytest
from PetStore_Swager_Teste.base_test import BaseTest
from utils.pet_factory import PETS_PRE_DEFINIDOS
from utils.order_factory import ORDER_PRE_DEFINIDAS
@pytest.fixture(scope="session", autouse=True)
def auth():
   pass

@pytest.fixture(scope="session")
def api():
    return BaseTest()

@pytest.fixture(scope="session", autouse=False)
def criar_pets_iniciais():
    """Cria os 5 pets pré-definidos uma vez antes de todos os testes."""
    api = BaseTest()
    ids_criados = []

    for pet in PETS_PRE_DEFINIDOS:
        response = api.post("/pet", json=pet)
        assert response.status_code == 200, f"Falha ao criar pet {pet['name']}"
        ids_criados.append(response.json()["id"])
       # print(f"Pet criado: {pet['name']} — ID: {response.json()['id']}")

    return ids_criados

@pytest.fixture(scope="session", autouse=True)
def criar_orders_iniciais():
    """Cria os 5 pedidos pré-definidos uma vez antes de todos os testes."""
    
    api = BaseTest()
    pedidos_criados_ids= []
    
    for pedido in ORDER_PRE_DEFINIDAS:
        response = api.post("/store/order", json=pedido)
        assert response.status_code==200, f"Falha ao criar pedido{pedido['id']}"
        pedidos_criados_ids.append(response.json()["id"])
    return pedidos_criados_ids