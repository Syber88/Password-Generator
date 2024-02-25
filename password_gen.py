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
    """
    Generate a string based on specified options.

    Args:
        numbers (bool, optional): Include digits in the generated string.
        Defaults to True.
        special_characters (bool, optional): Include special characters in the 
        generated string. Defaults to True.

    Returns:
        str: The generated string containing letters, and optionally digits and 
        special characters.
    """

    str_ = ""
    str_ += string.ascii_letters
    if numbers:
        str_ += string.digits
    if special_characters:
        str_ += string.punctuation
    return str_


def check_valid(numbers, special_characters, password) -> bool:
    """
    Generate a string based on specified options.

    Args:
        numbers (bool, optional): Include digits in the generated string. 
        Defaults to True.
        special_characters (bool, optional): Include special characters in the 
        generated string. Defaults to True.

    Returns:
        str: The generated string containing letters, and optionally digits and 
        special characters.
    """

    numbers_check = False
    special_chars_check = False

    if any(digit.isdigit() for digit in password):
        numbers_check = True
    if any(digit in string.punctuation for digit in password):
        special_chars_check = True
    if numbers_check == numbers and special_chars_check == special_characters:
        return True


def generate(min_length: int, numbers: bool, special_characters: bool) -> str:
    """
    Generate a random password based on specified criteria.

    Args:
        min_length (int): The minimum length of the password.
        numbers (bool): Whether the password must contain numbers.
        special_characters (bool): Whether the password must contain special characters.

    Returns:
        str: A randomly generated password meeting the specified criteria.
    """

    string_select = string_selection(numbers, special_characters)
    password = ""

    while len(password) < min_length:
        candidate = random.choice(string_select)
        password += candidate

    valid = check_valid(numbers, special_characters, password)
    if valid:
        return password
    else:
        return generate(min_length, numbers, special_characters)


if __name__ == "__main__":
    pass_length = get_minimum_length()
    include_numbers = numbers_inpassword()
    include_special = special_inpassword()
    print(generate(pass_length, include_numbers, include_special))




        
