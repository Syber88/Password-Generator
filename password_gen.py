import string
import random 

def generate(min_length, numbers=True, special_characters=True) -> str:
    password = ""
    characters = string.ascii_letters
    numbers = string.digits
    special_chars = string.punctuation

    for letter in range(min_length):
        for 