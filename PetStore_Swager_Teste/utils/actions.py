import requests
from PetStore_Swager_Teste.utils.pet_factory import ApiClient
class Actions:

    def __init__(self):
        self._Api = Api()

    def task_payload(self):
        return {
            "content": "Tarefa de teste",
            "user_id": "test_user_123",
            "task_id": "",      
            "is_done": False
        }
        
    def create_task(self, payload):
        return requests.put(self._Api.ENDPOINT + "/create-task", json=payload)
    
    def get_task(self, task_id):
        return requests.get(f"{self._Api.ENDPOINT}/get-task/{task_id}")
    
    def update_task(self, payload):
        return requests.put(f"{self._Api.ENDPOINT}/update-task", json=payload)