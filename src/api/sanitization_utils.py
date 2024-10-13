def validate_input_type(input_text):
    if not isinstance(input_text, str):
        raise ValueError("Invalid input type. Expected a string.")
    return input_text
