import re

def anonymize(text: str) -> str:
    return re.sub(r'\b[A-ZА-Я][a-zа-я]+\b', '[ИМЯ]', text)
