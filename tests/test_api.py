import unittest
from src.api.app import app
from src.api.sanitization import sanitize_input, sanitize_output
from src.api.similarity import jaccard_similarity, cosine_similarity
from src.api.llm import query_llm

class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_jaccard_similarity(self):
        prompt1 = "apple orange banana"
        prompt2 = "banana apple grape"
        score = jaccard_similarity(prompt1, prompt2)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 1)
        self.assertAlmostEqual(score, 0.5, delta=0.1)  # Expecting around 0.5 similarity
    
    def test_cosine_similarity(self):
        prompt1 = "machine learning"
        prompt2 = "deep learning"
        score = cosine_similarity(prompt1, prompt2)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 1)

    def test_filter_disallowed_words_input(self):
        response = self.app.post('/api/similarity', json={
            "prompt1": "This is an offensive prompt that has a lot of inappropriate words like murder and hate",
            "prompt2": "Another text"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("rejected", response.json.get("error").lower())

    def test_sanitize_html(self):
        response = self.app.post('/api/similarity', json={
            "prompt1": "<script>alert('bad')</script>",
            "prompt2": "Normal text"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("rejected", response.json.get("error").lower())

if __name__ == '__main__':
    unittest.main()