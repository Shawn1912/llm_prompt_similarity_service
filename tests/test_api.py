import unittest
from src.api.app import app

class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_similarity_endpoint(self):
        response = self.app.post('/api/similarity', json={"prompt1": "Hello", "prompt2": "World"})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()