import random
import string

def random_password_generator(password_lenght):
    """
    This script will create a strong random password
    following the next rules. It must:
    - Be at least 8 characters long
    - Contain at least 2 special characters
    - Contain at least 2 numbers
    """
    
    if password_lenght < 8:
        print("Password lenght must equal or higher than 8")
        return
    
    punctuation_chars = list(string.punctuation)
    digits = [str(i) for i in range (10)]
    ascii_letters = list(string.ascii_letters)
    character_set = punctuation_chars + digits + ascii_letters

    chars = []
    for i in range(password_lenght):
        if i < 2:
            chars.append(random.choice(punctuation_chars))
        elif i < 4:
            chars.append(random.choice(digits))
        else:
            chars.append(random.choice(character_set))
    
    random.shuffle(chars)
    password = "".join(chars)

    print(password)
    
if __name__ == "__main__":
    random_password_generator(15)
