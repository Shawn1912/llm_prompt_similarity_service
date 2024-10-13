import re

def validate_input_type(text):
    if not isinstance(text, str):
        raise ValueError("Invalid input type. Expected a string.")
    return text

def limit_length(input_text, max_length=500):
    return input_text[:max_length]

def reduce_repetitive_characters(text):
    # Replace any character repeated more than 3 times with the character repeated 3 times
    return re.sub(r'(.)\1{3,}', r'\1\1\1', text)

def sanitize_html_and_js(text):
    # Remove all <script> tags and all other HTML tags
    text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.IGNORECASE)
    # Remove all other HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove inline JavaScript event handlers (e.g., onclick, onmouseover)
    text = re.sub(r'on[a-z]+="[^"]+"', '', text, flags=re.IGNORECASE)
    return text

def filter_inappropriate_content(input_text, word_list):
    # Remove or censor words based on the provided word list
    for word in word_list:
        input_text = re.sub(rf'\b{word}\b', '', input_text, flags=re.IGNORECASE)
    return input_text