import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False

def main():
    entered_emails = []  # To store entered email addresses
    while True:
        email = input("Enter a valid email address: ")

        if validate_email(email):
            print("Valid email address")
            entered_emails.append(email)  # Add valid email to the list
            with open("valid_emails.txt", "a") as file:
                file.write(email + '\n')
        else:
            print("Invalid email address")

        choice = input("Do you want to continue? (Yes/No): ").strip().lower()
        if choice != "yes":
            break

    print("\nEntered emails:")
    for email in entered_emails:
        print(email)

if __name__ == "__main__":
    main()
