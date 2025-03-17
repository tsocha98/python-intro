import re
from datetime import datetime

def is_valid_email(email):
    """Sprawdza, czy adres e-mail jest poprawny"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def calculate_area(shape, *args):
    """Oblicza pole figury: kwadrat, prostokąt, koło"""
    if shape == "square":
        return args[0] ** 2
    elif shape == "rectangle":
        return args[0] * args[1]
    elif shape == "circle":
        return 3.14159 * args[0] ** 2
    else:
        raise ValueError("Nieznana figura")

def filter_even_numbers(numbers):
    """Filtruje liczby parzyste z listy"""
    return [num for num in numbers if num % 2 == 0]

def format_date(date_str, input_format="%Y-%m-%d", output_format="%d/%m/%Y"):
    """Konwertuje format daty"""
    return datetime.strptime(date_str, input_format).strftime(output_format)

def is_palindrome(text):
    """Sprawdza, czy podany tekst jest palindromem"""
    cleaned_text = ''.join(filter(str.isalnum, text)).lower()
    return cleaned_text == cleaned_text[::-1]
