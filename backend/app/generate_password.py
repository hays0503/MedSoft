import random

def generate_ascii_password(length: int) -> str:
    password = ''.join(chr(random.randint(33, 126)) for _ in range(length))
    return password
