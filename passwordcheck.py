import re

def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        return "Too short"
    
    # Check for use of special characters
    if not re.search(r"[!@#$%^&*()_+-=[]{};':\"\\|,.<>/?]", password):
        # Return "Weak" instead of "Too weak" for passwords without special characters
        return "Weak"
    
    return "Strong"

password = input("Enter your password: ")
strength = check_password_strength(password)
print("Your password is:", strength)