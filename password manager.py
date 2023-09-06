# Create an empty dictionary to store passwords
passwords = {}

while True:
    print("Options:")
    print("1. Add a password")
    print("2. Retrieve a password")
    print("3. List all passwords")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        website = input("Enter the website or app name: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        passwords[website] = {"username": username, "password": password}
        print("Password saved successfully.")

    elif choice == "2":
        website = input("Enter the website or app name to retrieve the password: ")
        if website in passwords:
            print(f"Username: {passwords[website]['username']}")
            print(f"Password: {passwords[website]['password']}")
        else:
            print("Website not found in the password manager.")

    elif choice == "3":
        print("Stored Passwords:")
        for website, data in passwords.items():
            print(f"Website: {website}")
            print(f"Username: {data['username']}")
            print(f"Password: {data['password']}")
            print("-------------------")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4).")