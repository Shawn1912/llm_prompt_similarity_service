import unittest
from src.api.sanitization import sanitize_output

class TestOutputSanitization(unittest.TestCase):
    def test_sanitize_output_removes_disallowed_words(self):
        input_text = "This is a badword and some offensive content."
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