import random
import string

length = int(input("Enter the desired password length: "))

character_pool = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(character_pool) for i in range(length))
6
print("Your generated password is:", password)