import string
import random 


def get_minimum_length() -> int:
    """Prompt the user to input the minimum length of a password.
    Continuously prompts the user until a valid integer value is provided
    as the minimum length of the password.
    Returns:
        int: The minimum length of the password as provided by the user."""
    
    while True:
        try:
            length = abs(int(input("what is the length of the password: ")))
            return length
        except ValueError:
            print("Please enter a digit to proceed")

def numbers_inpassword() -> bool:
    """Prompt the user to specify whether the password should include numbers.
    Returns:
        bool: True if the user wants numbers to be included in the password,
              False otherwise."""
    
    nums = input("should the password include numbers. yes/no ").lower()
    
    return nums == "yes" or nums == "y"


def special_inpassword() -> bool:
    """Prompt the user to specify whether the password should include special 
    characters.
    Returns:
        bool: True if the user wants special characters to be included in the 
        password, False otherwise."""
    
    special = input("should the password include special characters.yes/no").lower() 
    return special == "yes" or special == "y"


def string_selection(numbers: bool=True, special_characters: bool=True) -> str:
    str_ = ""
    str_ += string.ascii_letters
    if numbers:
        str_ += string.digits
    if special_characters:
        str_ += string.punctuation
    return str_

def check_valid(numbers, special_characters, password) -> bool:
    # string_select = string_selection(numbers, special_characters)
    valid = False
    # candidate = random.choice(string_select)
    if numbers and any(digit.isdigit for digit in password):
        valid = True
    if special_characters and any(digit in string.punctuation for digit in password):
        valid = True


def generate(min_length: int, numbers: bool, special_characters: bool) -> str:
    string_select = string_selection(numbers, special_characters)
    password = ""
    valid = False
    while len(password) < min_length:


        password += candidate

    if valid:
        return password


if __name__ == "__main__":
    pass_length = get_minimum_length()
    include_numbers = numbers_inpassword()
    include_special = special_inpassword()
    print(generate(pass_length, include_numbers, include_special))




        
