import string
import random 


def get_minimum_length() -> int:
    while True:
        length = input("what is the length of the password:\n")
        if not length.isdigit():
            print("Please enter a digit to proceed")
            continue
        return int(length)  


def numbers_inpassword() -> bool:
    nums = input("should the password include numbers. yes/no\n").lower() == "yes"
    return nums


def special_inpassword() -> bool:
    special = input("should the password include special characters. yes/no\n").lower() == "yes"
    return special


def generate(min_length=8, numbers=True, special_characters=True) -> str:
    str = ""
    str += string.ascii_letters
    if numbers:
        str += string.digits
    if special_characters:
        str += string.punctuation
    password = ""

    while len(password) < min_length:
        password += random.choice(str)
    print("==============")
    print(password)
    print("==============")
    return password


if __name__ == "__main__":
    pass_length = get_minimum_length()
    include_numbers = numbers_inpassword()
    include_special = special_inpassword()
    generate(pass_length, include_numbers, include_special)




        