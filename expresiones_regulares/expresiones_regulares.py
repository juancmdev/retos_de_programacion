import re

# """
# Ejercicio
# """
# regex = r"[0-9]+"

# def find_numbers(text: str) -> list:
#     return re.findall(regex, text)

# print(find_numbers("Este es el ejercicio 16 publicado 15/04/2024."))

"""
Extra
"""

def validate_email(email: str) -> bool:
    return bool(re.match(r"[\w.+-]+@[\w]+\.[a-zA-Z]+", email))

print(validate_email("juancmorenoj@gmail.com"))

def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))

print(validate_phone("+00320 1234"))

