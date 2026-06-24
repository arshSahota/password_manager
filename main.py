from manager import add_password, view_passwords, get_password, delete_password

while True:
    print("\n1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        site = input("Enter site: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        add_password(site, username, password)

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        site = input("Enter site to search: ")
        get_password(site)

    elif choice == "4":
        site = input("Enter site to delete: ")
        delete_password(site)

    elif choice == "5":
        break