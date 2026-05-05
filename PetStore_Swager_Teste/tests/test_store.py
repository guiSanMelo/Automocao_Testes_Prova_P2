import requests
from base_test import BaseTest
import datetime
class TestStore(BaseTest):

    def test_get_store_inventory_200(self):
        response = self.get("/store/inventory")
        assert response.status_code==200
        
    def test_post_store_order_200(self):
        order = {
            "id": 0,
            "petId": 0,
            "quantity": 0,
            "shipDate": "2026-05-05T01:47:04.087Z",
            "status": "placed",
            "complete": True
        }
        response = self.post("/store/order", json=order)
        assert response.status_code==200
        
      
    def test_get_store_order_by_id_200(self):
        for orderId in self.pedidos_criados_ids:
            response = self.get(f"/store/order/{orderId}")
            assert response.status_code==200
            
    def test_delete_order_by_id(self):
        for orderId in self.pedidos_criados_ids:
            response = self.delete(f"/store/order/{orderId}")
            assert response.status_code==200

