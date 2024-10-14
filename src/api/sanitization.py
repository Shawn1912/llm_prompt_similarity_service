from .sanitization_utils import (
    validate_input_type,
    is_excessively_disallowed,
    limit_length,
    reduce_repetitive_characters,
    filter_disallowed_words,
    sanitize_html_and_js,
)

DISALLOWED_WORDS = ["badword", "offensive", "inappropriate", "kill", "hate", "murder"]
MAX_PROMPT_LENGTH = 500
MAX_RESPONSE_LENGTH = 1000

def sanitize_input(input_text):
    input_text = validate_input_type(input_text)
    if is_excessively_disallowed(input_text, DISALLOWED_WORDS, 3):
        raise ValueError("Input rejected due to excessive toxicity.")
    input_text = sanitize_html_and_js(input_text)
    input_text = limit_length(input_text, max_length=MAX_PROMPT_LENGTH)
    input_text = reduce_repetitive_characters(input_text)
    input_text = filter_disallowed_words(input_text, DISALLOWED_WORDS)
    return input_text

def sanitize_output(output_text):
    output_text = validate_input_type(output_text)
    output_text = limit_length(output_text, max_length=MAX_RESPONSE_LENGTH)
    output_text = filter_disallowed_words(output_text, DISALLOWED_WORDS)
    return output_text