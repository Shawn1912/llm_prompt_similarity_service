import re


def limit_length(input_text, max_length=500):
    return input_text[:max_length]

def reduce_repetitive_characters(input_text):
    # Replace any character repeated more than 3 times with the character repeated 3 times
    return re.sub(r'(.)\1{3,}', r'\1\1\1', input_text)

def sanitize_html_and_js(input_text):
    # Remove all <script> tags and all other HTML tags
    input_text = re.sub(r'<script.*?>.*?</script>', '', input_text, flags=re.IGNORECASE)
    # Remove all other HTML tags
    input_text = re.sub(r'<.*?>', '', input_text)
    return input_text