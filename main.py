import random
import string

character_set = list(string.punctuation + string.digits + string.ascii_letters)
random.shuffle(character_set)
password = []
password_lenght = int(input("Enter password lenght: "))  # 5
for _ in range(password_lenght):
    password.append(random.choice(character_set))
new_password_string = "".join(password)
# for char in password:
#     new_password_string += char
print(new_password_string)
