import requests
from base_test import BaseTest
from utils.order_factory import create_order
class TestStore(BaseTest):

    def test_get_store_inventory_200(self):
        response = self.get("/store/inventory")
        assert response.status_code==200
        
    def test_post_store_order_200(self):
        order = create_order()
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

