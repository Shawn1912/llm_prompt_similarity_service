import unittest
from src.api.llm import query_llm

class TestLLM(unittest.TestCase):
    def test_query_llm(self):
        prompt = "What is the meaning of life?"
        response = query_llm(prompt)
        self.assertTrue(isinstance(response, str))
        self.assertGreater(len(response), 0)

if __name__ == '__main__':
    unittest.main()