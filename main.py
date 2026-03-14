from password_generator import generate_password
import password_manager as pm


while True:

    print("\nPASSWORD MANAGER")
    print("1. Generate Password")
    print("2. Save Password")
    print("3. View Passwords")
    print("4. Search Password")
    print("5. Update Password")
    print("6. Delete Password")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        password = generate_password()
        print("Generated Password:", password)

    elif choice == "2":

        site = input("Enter site name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        pm.save_password(site, username, password)

    elif choice == "3":

        pm.view_passwords()

    elif choice == "4":

        site = input("Enter site name: ")
        pm.search_password(site)

    elif choice == "5":

        site = input("Enter site name: ")
        new_password = input("Enter new password: ")

        pm.update_password(site, new_password)

    elif choice == "6":

        site = input("Enter site name: ")
        pm.delete_password(site)

    elif choice == "7":

        print("Exiting program")
        break

    else:

        print("Invalid choice")