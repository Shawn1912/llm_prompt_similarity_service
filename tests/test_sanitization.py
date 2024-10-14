import unittest
from src.api.sanitization_utils import limit_length
from src.api.sanitization import sanitize_input, sanitize_output

class TestInputSanitization(unittest.TestCase):
    def test_sanitize_input(self):
        input_prompt = "<b>Test</b> with some extra text."
        sanitized = sanitize_input(input_prompt)
        self.assertEqual(sanitized, "Test with some extra text.")

    def test_sanitize_input_limits_length(self):
        input_prompt = "It's time to write a prompt!" * 600
        sanitized = sanitize_input(input_prompt)
        self.assertEqual(len(sanitized), 500)
    
    def test_sanitize_input_removes_html_js(self):
        input_text = "<script>alert('This is malicious');</script>Some text."
        sanitized = sanitize_input(input_text)
        self.assertNotIn("<script>", sanitized)
        self.assertNotIn("alert", sanitized)
        self.assertEqual(sanitized, "Some text.")

class TestOutputSanitization(unittest.TestCase):
    def test_sanitize_output_limits_length(self):
        text = "Prompt returned!" * 600
        sanitized = sanitize_output(text)
        self.assertEqual(len(sanitized), 1000)

    def test_sanitize_output_removes_disallowed_words(self):
        input_text = "This result contains words like murder and kill."
        sanitized = sanitize_output(input_text)
        self.assertNotIn("murder", sanitized)
        self.assertNotIn("kill", sanitized)

if __name__ == '__main__':
    unittest.main()