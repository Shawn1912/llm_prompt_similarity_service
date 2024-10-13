import re

def validate_input_type(text):
    if not isinstance(text, str):
        raise ValueError("Invalid input type. Expected a string.")
    return text

def is_excessively_disallowed(input_text, word_list, threshold=5):
    disallowed_word_count = 0

    for word in word_list:
        disallowed_word_count += len(re.findall(rf'\b{word}\b', input_text, flags=re.IGNORECASE))

    if disallowed_word_count > threshold:
        return True
    return False

def limit_length(input_text, max_length=500):
    return input_text[:max_length]

def reduce_repetitive_characters(text):
    # Replace any character repeated more than 3 times with the character repeated 3 times
    return re.sub(r'(.)\1{3,}', r'\1\1\1', text)

def sanitize_html_and_js(text):
    if not isinstance(text, str):
        raise ValueError("sanitize_html_and_js() expected a string input, but got a non-string value.")

    # Remove all <script> tags and all other HTML tags
    text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.IGNORECASE)
    # Remove all other HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove inline JavaScript event handlers (e.g., onclick, onmouseover)
    text = re.sub(r'on[a-z]+="[^"]+"', '', text, flags=re.IGNORECASE)
    return text

def filter_disallowed_words(input_text, word_list):
    # Remove words based on the provided word list
    for word in word_list:
        input_text = re.sub(rf'\b{word}\b', '', input_text, flags=re.IGNORECASE)
    return input_text