import re

def check_password_strength(password):
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Uppercase & lowercase
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 1

    # Numbers
    if re.search("[0-9]", password):
        strength += 1

    # Special characters
    if re.search("[@#$%^&*]", password):
        strength += 1

    # Result
    if strength == 4:
        return "Strong 💪"
    elif strength == 3:
        return "Medium ⚠️"
    else:
        return "Weak ❌"


if __name__ == "__main__":
    pwd = input("Enter your password: ")
    print("Password Strength:", check_password_strength(pwd))
