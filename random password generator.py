import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True, start_letter=None, end_letter=None):
    chars = ""
    
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    if not chars:
        return "Error: No character set selected."

    if length < 2 or length > 100:
        return "Error: Password length must be between 2 and 100 characters."

    if start_letter:
        # Ensure the specified start letter is uppercase
        start_letter = start_letter.upper()
        chars = chars.replace(start_letter, "", 1)  # Remove the specified start letter from the character set

    if end_letter:
        chars = chars.replace(end_letter, "", 1)  # Remove the specified end letter from the character set

    password = ''.join(random.choice(chars) for _ in range(length))

    if start_letter:
        password = start_letter + password[1:]

    if end_letter:
        password = password[:-1] + end_letter

    return password

def password_strength(password):
    # Define a simple password strength assessment logic here
    if len(password) >= 2 and len(password) < 12:  # Set password strength to "Weak" for lengths 2 to 11
        return "Weak"
    elif len(password) >= 12:
        return "Moderate"
    elif len(password) >= 16:
        return "Strong"
    else:
        return "Weak"  # Set password strength to "Weak" for other lengths

def main():
    print("Random Password Generator")
    
    while True:
        try:
            length = int(input("Enter the length of the password (type a number from 2 to 100): "))
            if length < 2 or length > 100:
                print("Password length must be between 2 and 100 characters.")
                continue  # Retry input
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue  # Retry input
        break  # Exit the loop if valid input is provided

    while True:
        include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower()
        if include_lowercase in ['y', 'n', 'yes', 'no']:
            use_lowercase = include_lowercase.startswith("y")
            break  # Exit the loop if valid input is provided

    while True:
        include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower()
        if include_uppercase in ['y', 'n', 'yes', 'no']:
            use_uppercase = include_uppercase.startswith("y")
            break  # Exit the loop if valid input is provided

    while True:
        include_digits = input("Include digits? (y/n): ").strip().lower()
        if include_digits in ['y', 'n', 'yes', 'no']:
            use_digits = include_digits.startswith("y")
            break  # Exit the loop if valid input is provided

    while True:
        include_special = input("Include special characters? (y/n): ").strip().lower()
        if include_special in ['y', 'n', 'yes', 'no']:
            use_special_chars = include_special.startswith("y")
            break  # Exit the loop if valid input is provided

    while True:
        start_letter = input("Specify a character to start with (press Enter to skip): ").strip()
        if not start_letter or len(start_letter) == 1:
            break  # Exit the loop if valid input is provided
        else:
            print("Start letter should be a single character.")

    while True:
        end_letter = input("Specify a character to end with (press Enter to skip): ").strip()
        if not end_letter or len(end_letter) == 1:
            break  # Exit the loop if valid input is provided
        else:
            print("End letter should be a single character.")

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars, start_letter, end_letter)
    
    strength = password_strength(password)
    
    print(f"\nYour generated password is: {password}")
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
