import re

DISALLOWED_WORDS = ["badword", "offensive", "inappropriate"]

def sanitize_output(output):
    # Remove any disallowed words
    for word in DISALLOWED_WORDS:
        output = re.sub(rf'\b{word}\b', '***', output, flags=re.IGNORECASE)

    # Example: Strip potential script tags if HTML content exists
    output = re.sub(r'<script.*?>.*?</script>', '', output, flags=re.IGNORECASE)

    return output