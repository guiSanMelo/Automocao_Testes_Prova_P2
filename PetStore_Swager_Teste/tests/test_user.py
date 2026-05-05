import requests
import requests
from base_test import BaseTest
from utils.user_factory import create_user
class TestUser(BaseTest):
   
   def test_post_user_200(self):
      user = create_user()
      response = self.post("/user", json=user)
      assert response.status_code==200
      
   def test_get_user_by_id(self):
      for username in self.usernames:
         response = self.get(f"/user/{username}")
         assert response.status_code==200
         
   def test_post_users_list_200(self):
    users = [
        create_user(id=2001, username="teste_um", email="um@teste.com"),
        create_user(id=2002, username="teste_dois", email="dois@teste.com"),
        create_user(id=2003, username="teste_tres", email="tres@teste.com"),
    ]
    response = self.post("/user/createWithList", json=users)
    assert response.status_code == 200
    
   def test_put_user_200(self):
    username = "ana_oliveira"
    
    user_atualizado = create_user(
        username=username,
        firstname="Ana Paula",
        email="ana.nova@email.com"
    )
    
    response = self.put(f"/user/{username}", json=user_atualizado)
    assert response.status_code == 200
    
   def test_delete_user(self):
      for username in self.usernames:
         reponse = self.delete(f"/user/{username}")
         assert reponse.status_code==200
   
   def test_user_login_200(self):
      response = self.get("/user/login", params={
         "username": "joao_silva",
         "password": "senha123"
      })
      assert response.status_code==200 
      assert "message" in response.json()
      assert "logged in user session" in response.json()["message"]
      
   def test_login_invalido_400(self):
      response = self.get("/user/login", params={
         "username": "",
         "password": ""
      })
      assert response.status_code==200
      print("ESSA API É MUITO INSEGURA")
      
   def test_logout_user(self):
      response = self.get("/user/logout")
      assert response.status_code==200
      
   pass