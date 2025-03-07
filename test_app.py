import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_home_route(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    def test_status_route(self):
        tester = app.test_client(self)
        response = tester.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "running"})

if __name__ == "__main__":
    unittest.main()
