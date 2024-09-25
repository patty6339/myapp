import unittest
from app import app, db
from app.models import Customer, Order

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_customer_creation(self):
        response = self.app.post('/customers', json={'name': 'John Doe', 'code': 'JD123'})
        self.assertEqual(response.status_code, 201)

    def test_order_creation(self):
        self.app.post('/customers', json={'name': 'John Doe', 'code': 'JD123'})
        response = self.app.post('/orders', json={'item': 'Product', 'amount': 100.0, 'time': '2024-01-01', 'customer_id': 1})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
