import string
import random 

def get_minimum_length() -> int:
    length = int(input("what is the length of the password"))
    return length


def numbers_inpassword() -> bool:
    nums = input("should the password include numbers. yes/no\n").lower() == "yes"
    return nums


def numbers_inpassword() -> bool:
    special = input("should the password include special characters. yes/no\n").lower() == "yes"
    return special


def generate(min_length=5, numbers=True, special_characters=True) -> str:
    str = ""
    str += string.ascii_letters
    str += string.digits
    str += string.punctuation
    password = ""

    while len(password) < min_length:
        password += random.choice(str)
    return password




        