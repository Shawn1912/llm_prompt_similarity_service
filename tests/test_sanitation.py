import unittest
from src.api.sanitization import sanitize_input

class TestSanitization(unittest.TestCase):
    def test_sanitize_input(self):
        input_prompt = "<b>Test</b> with some extra text."
        sanitized = sanitize_input(input_prompt)
        self.assertEqual(sanitized, "Test with some extra text.")

    def test_length_limit(self):
        input_prompt = "a" * 600
        sanitized = sanitize_input(input_prompt)
        self.assertEqual(len(sanitized), 500)

if __name__ == '__main__':
    unittest.main()