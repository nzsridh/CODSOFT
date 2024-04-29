import random
import string

# Function to generate a password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to validate user input for password length
def get_password_length():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Password length must be greater than 0.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("PASSWORD GENERATOR")
    username = input("Enter your username: ")
    
    while True:
        length = get_password_length()
        generated_password = generate_password(length)
        
        print(f"\nGenerated password: {generated_password}")
        
        accept = input("Do you accept the generated password? (yes/no): ").lower()
        if accept == 'yes':
            print("Password accepted. Goodbye!")
            break
        else:
            print("Generating a new password...")

if __name__ == "__main__":
    main()
