import unittest
from src.api.app import app

class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_similarity_endpoint(self):
        response = self.app.post('/api/similarity', json={
            "prompt1": "apple orange banana",
            "prompt2": "banana apple grape",
            "metric": "jaccard"
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("similarity_score", data)
        self.assertIn("llm_response", data)

    def test_reject_input_excessive_disallowed_words(self):
        response = self.app.post('/api/similarity', json={
            "prompt1": "This is an offensive prompt that has a lot of inappropriate words like murder and hate",
            "prompt2": "Similar offensive input",
            "metric": "cosine"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("rejected", response.json.get("message").lower())

if __name__ == '__main__':
    unittest.main()