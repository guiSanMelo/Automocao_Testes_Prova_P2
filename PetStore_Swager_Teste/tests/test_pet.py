from PetStore_Swager_Teste.base_test import BaseTest
from utils.pet_factory import criar_pet

class TestPet(BaseTest):

    def test_get_pet_by_status_200(self):
        response = self.get("/pet/findByStatus")
        assert response.status_code==200   
        
    def test_get_pet_by_id_200(self):
        for petId in self.pets_ids:
            response = self.get(f"/pet/{petId}")
            assert response.status_code == 200

    def test_adicionar_pet_200(self):
        novo_pet = criar_pet()
        
        reponse = self.post("/pet", json=novo_pet)

        assert reponse.status_code==200
        assert reponse.json()["name"] == 'doggie'
        assert reponse.json()["status"] == "available"
        
    def test_update_pet_200(self):
        
        pet = criar_pet()
        response = self.post("/pet", json=pet)
        assert response.status_code==200
        
        pet_alterado = {
            "id": 0,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "Alok",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                "id": 0,
                "name": "string"
                }
            ],
            "status": "available"
        }
        
        update = self.put("/pet", json=pet_alterado)
        
        assert update.status_code==200
        assert update.json()["name"] == 'Alok'
        assert update.json()["status"] == "available"
        
    def test_adicionar_foto_200(self):
        for petId in self.pets_ids:
            with open(".media\\imgs\\pikachu.png", "rb") as pikachu:
                response = self.post(
                    f"/pet/{petId}/uploadImage",
                    files={"files": pikachu},
                    data={"additionalMetadata": "foto do pikachu"}
                )
                assert response.status_code==200
                
    def test_deletar_pet_200(self):
        for petId in self.pets_ids:
            response = self.delete(f"/pet/{petId}")
            assert response.status_code==200
 
    
   
    
       