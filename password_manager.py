FILE = "data.txt"

def save_password(site, username, password):

    with open(FILE, "a") as f:
        f.write(site + "," + username + "," + password + "\n")

    print("Password saved successfully")


def view_passwords():

    try:
        with open(FILE, "r") as f:
            data = f.readlines()

        if not data:
            print("No passwords saved")

        for line in data:
            site, username, password = line.strip().split(",")
            print(f"Site: {site} | Username: {username} | Password: {password}")

    except FileNotFoundError:
        print("No data file found")


def search_password(site_name):

    with open(FILE, "r") as f:
        for line in f:
            site, username, password = line.strip().split(",")

            if site == site_name:
                print(f"Username: {username}")
                print(f"Password: {password}")
                return

    print("Site not found")


def delete_password(site_name):

    lines = []

    with open(FILE, "r") as f:
        lines = f.readlines()

    with open(FILE, "w") as f:
        for line in lines:
            site, username, password = line.strip().split(",")

            if site != site_name:
                f.write(line)

    print("Password deleted")


def update_password(site_name, new_password):

    lines = []

    with open(FILE, "r") as f:
        lines = f.readlines()

    with open(FILE, "w") as f:
        for line in lines:
            site, username, password = line.strip().split(",")

            if site == site_name:
                line = site + "," + username + "," + new_password + "\n"

            f.write(line)

    print("Password updated")