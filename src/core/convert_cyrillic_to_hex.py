import re

def is_cyrillic(cyrillic_query:str):
    return bool(re.fullmatch('[а-яА-ЯёЁ]+', cyrillic_query))

def convert_cyrillic_to_hex(cyrillic_query:str):
    if is_cyrillic(cyrillic_query):
        return '%' + '%'.join([f'{byte:02X}' for byte in cyrillic_query.encode('utf-8')])

