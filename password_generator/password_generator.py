import random
import string


def generator_password(min_len, digit_characters=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    # print(letters, digits, special)

    characters = letters
    if digit_characters:
        characters += digits
    if special_characters:
        characters += special

    has_digit = False
    has_special = False
    criteria = False
    pwd = ""
    while not criteria or len(pwd) < min_len:
        c = random.choice(characters)
        pwd += c
        if c in digits:
            has_digit = True
        if c in special:
            has_special = True

        criteria = True
        if digit_characters:
            criteria = criteria and has_digit
        if special_characters:
            criteria = criteria and has_special

    return pwd


print(generator_password(10))
