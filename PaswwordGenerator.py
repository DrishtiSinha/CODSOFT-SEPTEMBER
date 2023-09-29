import random
import string

def generate_password(length):
    # Define character sets for the password
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets
    all_chars = lower_letters + upper_letters + digits + special_chars

    # Check if the password length is valid
    if length < 8:
        print("Password length should be at least 8 characters.")
        return

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "_main_":
    try:
        # Prompt the user for the desired password length
        password_length = int(input("Enter the desired password length: "))

        # Generate and display the password
        generated_password = generate_password(password_length)
        if generated_password:
            print("Generated Password:", generated_password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")