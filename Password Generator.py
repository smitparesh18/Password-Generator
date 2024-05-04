import random
import string

def password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be included")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Enter Your Password Choice")
    length = int(input("Length of the password: "))
    include_uppercase = input("Uppercase letters? (yes/no): ").lower() == 'yes'
    include_lowercase = input("Lowercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Digits? (yes/no): ").lower() == 'yes'
    include_special_chars = input("Special characters? (yes/no): ").lower() == 'yes'

    try:
        password = password(
            length=length,
            uppercase=include_uppercase,
            lowercase=include_lowercase,
            digits=include_digits,
            special_chars=include_special_chars
        )
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)
