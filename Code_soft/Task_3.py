import random as r
import string as s

def generate_password(length, complexity):
    if complexity == "low":
        chars = s.ascii_letters + s.digits
    elif complexity == "medium":
        chars = s.ascii_letters + s.digits + s.punctuation
    elif complexity == "high":
        chars = s.ascii_letters + s.digits + s.punctuation + s.ascii_lowercase + s.ascii_uppercase
    else:
        print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
        return None

    password = ''.join(r.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator!")
    while True:
        length = int(input("Enter the length of the password: "))
        complexity = input("Enter the complexity level (low/medium/high): ").lower()
        
        password = generate_password(length, complexity)
        if password:
            print("Your generated password is:", password)
        
        choice = input("Do you want to generate another password? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you for using Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()

