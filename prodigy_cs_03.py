import re

def check_password_strength(password):
    # Criteria 1: Length of at least 8 characters
    if len(password) < 8:
        return "Password too short! Use at least 8 characters."

    # Criteria 2: At least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password should have at least one uppercase letter."

    # Criteria 3: At least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password should have at least one lowercase letter."

    # Criteria 4: At least one digit
    if not re.search(r'\d', password):
        return "Password should have at least one number."

    # Criteria 5: At least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should have at least one special character."

    # If all criteria are met
    return "Strong Password!"

# Test the tool
password = input("Enter your password: ")
print(check_password_strength(password))
