import re

def sanitize_input(prompt):
    # Strip HTML tags
    prompt = re.sub(r'<.*?>', '', prompt)
    # Limit prompt length
    return prompt[:500]