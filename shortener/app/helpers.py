import re
from random import choice
from string import ascii_letters, digits

ALPHABET = ascii_letters + digits

url_regex = re.compile(
    r'^(?:http|ftp)s?://'
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r'(?::\d+)?'
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def rand_str(length: int) -> str:
    return ''.join(choice(ALPHABET) for _ in range(length))


def validate_url(url: str) -> bool:
    return url_regex.fullmatch(url) is not None
