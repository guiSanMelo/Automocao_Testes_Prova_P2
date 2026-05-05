import requests

class BaseTest:

    BASE_URL="https://petstore.swagger.io/v2"
    token = None
    pets_ids=[]
    pedidos_criados_ids=[]
   
    @classmethod
    def login(cls, username="test", password="abc123"):
        response = requests.post(f"{cls.BASE_URL}/auth/login", json={
            "username": username,
            "password": password
        })
        assert response.status_code==200
        cls.token = response.json()["acess_token"]

    @classmethod
    def get_headers(cls):
        return {}
    
    def get(self, path, **kwargs):
        return requests.get(
            f"{self.BASE_URL}{path}",
            headers=self.get_headers(),
            **kwargs
        )
    
    def post(self, path, **kwargs):
        return requests.post(
            f"{self.BASE_URL}{path}", 
            headers=self.get_headers(),
            **kwargs
        )
        
    def put(self, path, **kwargs):
        return requests.put(
            f"{self.BASE_URL}{path}", 
            headers=self.get_headers(),
            **kwargs
        )
    
    def delete(self, path, **kawrgs):
        return requests.delete(
            f"{self.BASE_URL}{path}",
            headers=self.get_headers(),
            **kawrgs
        )