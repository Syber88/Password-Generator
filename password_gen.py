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


def generate(min_length=8, numbers=True, special_characters=True) -> str:
    str = ""
    str += string.ascii_letters
    if numbers:
        str += string.digits
    if special_characters:
        str += string.punctuation
    password = ""



    valid = False
    while len(password) < min_length:
        candidate = random.choice(str)
        if numbers and candidate.isdigit():
            valid = True
        if special_characters and candidate in string.punctuation:
            valid = True

        password += candidate
        
    if valid:
        return password


if __name__ == "__main__":
    pass_length = get_minimum_length()
    include_numbers = numbers_inpassword()
    include_special = special_inpassword()
    print(generate(pass_length, include_numbers, include_special))




        
