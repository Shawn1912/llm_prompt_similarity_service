import re


def validate_input_type(text):
    if not isinstance(input_text, str):
        raise ValueError("Invalid input type. Expected a string.")
    return input_text

def sanitize_html_and_js(input_text):
    # Remove all <script> tags and all other HTML tags
    input_text = re.sub(r'<script.*?>.*?</script>', '', input_text, flags=re.IGNORECASE)
    input_text = re.sub(r'<.*?>', '', input_text)
    return input_text