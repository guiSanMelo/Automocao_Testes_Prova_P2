import pytest
from PetStore_Swager_Teste.base_test import BaseTest
from utils.pet_factory import PETS_PRE_DEFINIDOS
from utils.order_factory import ORDER_PRE_DEFINIDAS
from utils.user_factory import USERS_PRE_DEFINIDOS
@pytest.fixture(scope="session", autouse=True)
def auth():
   pass

@pytest.fixture(scope="session")
def api():
    return BaseTest()

@pytest.fixture(scope="session", autouse=False)
def criar_pets_iniciais():
    api = BaseTest()

    for pet in PETS_PRE_DEFINIDOS:
        response = api.post("/pet", json=pet)
        assert response.status_code == 200, f"Falha ao criar pet {pet['name']}"
        BaseTest.pets_ids.append(response.json()["id"]) 
    return BaseTest.pets_ids  

@pytest.fixture(scope="session", autouse=False)
def criar_orders_iniciais():
    api = BaseTest()

    for pedido in ORDER_PRE_DEFINIDAS:
        response = api.post("/store/order", json=pedido)
        assert response.status_code == 200, f"Falha ao criar pedido {pedido['id']}"
        BaseTest.pedidos_id.append(response.json()["id"])
        print(f"Pedido criado: {pedido['id']}")

    return BaseTest.pedidos_id

@pytest.fixture(scope="session", autouse=True)
def criar_user_iniciais():
    api = BaseTest()
    usernames = []

    for users in USERS_PRE_DEFINIDOS:
        response = api.post("/user", json=users)
        assert response.status_code == 200, f"Falha ao criar o usuário: {users['username']}"
        BaseTest.usernames.append(users["username"])
        print(f"Usuário criado: {users['username']}")

    return BaseTest.usernames