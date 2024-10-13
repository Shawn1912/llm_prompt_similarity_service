import unittest
from src.api.similarity import jaccard_similarity, cosine_similarity

class TestSimilarity(unittest.TestCase):
    def test_jaccard_similarity(self):
        str1 = "apple orange banana"
        str2 = "banana apple grape"
        self.assertAlmostEqual(jaccard_similarity(str1, str2), 0.5)

    def test_cosine_similarity(self):
        str1 = "apple orange banana"
        str2 = "banana apple grape"
        score = cosine_similarity(str1, str2)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 1)

if __name__ == '__main__':
    unittest.main()