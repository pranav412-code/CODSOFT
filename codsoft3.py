import random
import string


def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():
    print("Welcome to the Password Generator!")
    try:
        # Get desired password length from user
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive integer for password length.")
            return

        # Generate the password
        password = generate_password(length)

        # Display the password
        print("Your generated password is:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")


if __name__ == "__main__":
    main()
