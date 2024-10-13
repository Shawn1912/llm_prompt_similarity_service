import re

MAX_PROMPT_LENGTH = 1000

def sanitize_input(prompt):
    prompt = strip_html_tags(prompt)
    prompt = limit_prompt_length(prompt)
    return prompt

def strip_html_tags(prompt):
    return re.sub(r'<.*?>', '', prompt)

def limit_prompt_length(prompt):
    return prompt[:MAX_PROMPT_LENGTH]