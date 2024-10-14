import unittest
from src.api.sanitization import sanitize_input, sanitize_output

class TestInputSanitization(unittest.TestCase):
    def test_sanitize_input(self):
        input_prompt = "<b>Test</b> with some extra text."
        sanitized = sanitize_input(input_prompt)
        self.assertEqual(sanitized, "Test with some extra text.")

    def test_length_limit(self):
        input_prompt = "a" * 600
        sanitized = sanitize_input(input_prompt)
        self.assertEqual(len(sanitized), 500)

class TestOutputSanitization(unittest.TestCase):
    def test_sanitize_output_removes_disallowed_words(self):
        input_text = "This result contains words like murder and kill."
        sanitized = sanitize_output(input_text)
        self.assertNotIn("badword", sanitized)
        self.assertNotIn("offensive", sanitized)
        self.assertIn("***", sanitized)

    def test_sanitize_output_removes_script_tags(self):
        input_text = "<script>alert('This is malicious');</script>Some text."
        sanitized = sanitize_output(input_text)
        self.assertNotIn("<script>", sanitized)
        self.assertNotIn("alert", sanitized)
        self.assertEqual(sanitized, "Some text.")

if __name__ == '__main__':
    unittest.main()