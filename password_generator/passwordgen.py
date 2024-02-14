import random
def passwordgen(len):
    
    low_char = "abcdefghijklmnopqrstuvwxyz"
    upper_char = low_char.upper()
    num = "0123456789"
    special = "~,!@#$%^&*+-"

    mix = low_char + upper_char + num + special

    password = ""
    for i in range(len):
        password+= "".join(random.choice(mix))

    return password

len = int(input("Enter Length of Password: "))

result = passwordgen(len)

print("Your Password is: ", result)