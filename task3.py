import random
import string

def generate_password(name, length, complexity):
    # Define character sets based on complexity
    chars = string.ascii_letters
    if complexity > 1:
        chars += string.digits
    if complexity > 2:
        chars += string.punctuation

    # Ensure the password is at least as long as the name
    name_length = len(name)
    if length < name_length:
        raise ValueError("Password length must be at least as long as the name")

    # Create a base password with the name and random characters
    base_password = name + ''.join(random.choice(chars) for _ in range(length - name_length))
    return ''.join(random.sample(base_password, len(base_password)))  # Shuffle to mix name with random characters

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length > 0:
                break
            print("Length must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            complexity = int(input("Enter the desired complexity level (1-3): "))
            if complexity in {1, 2, 3}:
                break
            print("Complexity level must be 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    name = input("Enter your name: ")
    try:
        password = generate_password(name, length, complexity)
        print("Generated password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
