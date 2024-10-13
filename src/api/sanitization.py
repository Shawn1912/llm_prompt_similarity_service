from .sanitization_utils import (
    validate_input_type,
    limit_length,
    reduce_repetitive_characters,
    filter_inappropriate_content,
    sanitize_html_and_js,
)

DISALLOWED_WORDS = ["badword", "offensive", "inappropriate"]
TOXIC_WORDS = ["hate", "kill", "stupid", "idiot", "dumb"]
MAX_PROMPT_LENGTH = 500
MAX_RESPONSE_LENGTH = 1000

def sanitize_input(input_text):
    input_text = validate_input_type(input_text)  # Validate input is a string
    input_text = sanitize_html_and_js(input_text)  # Remove any HTML or script tags
    input_text = limit_length(input_text, max_length=MAX_PROMPT_LENGTH)  # Limit the length
    input_text = reduce_repetitive_characters(input_text)  # Reduce character repetition
    input_text = filter_inappropriate_content(input_text, DISALLOWED_WORDS)  # Filter profanity
    input_text = filter_inappropriate_content(input_text, TOXIC_WORDS)  # Check for toxic content
    print(f"Filtered text ${input_text}")
    return input_text

def sanitize_output(output_text):
    output_text = validate_input_type(output_text)  # Validate output is a string
    output_text = limit_length(output_text, max_length=MAX_RESPONSE_LENGTH)  # Limit the length
    output_text = filter_inappropriate_content(output_text, DISALLOWED_WORDS)  # Filter profanity
    output_text = filter_inappropriate_content(output_text, TOXIC_WORDS)  # Check for toxic content
    return output_text