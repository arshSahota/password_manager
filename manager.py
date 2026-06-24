import json
from utils import logger, log_message

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

@logger
def add_password(site, username, password):
    data = load_data()

    if site in data:
        print("Site already exists. Updating password.")

    data[site] = {
        "username": username,
        "password": password
    }

    save_data(data)
    log_message(f"Added/Updated password for {site}")

def view_passwords():
    data = load_data()

    if not data:
        print("No passwords stored.")
        return

    print("\nStored Passwords:\n")

    for site, details in data.items():
        print(site)
        print(f"  Username: {details['username']}")
        print(f"  Password: {details['password']}")
        print("-" * 25)
    
def get_password(site):
    data = load_data()

    if site in data:
        print(f"Site: {site}")
        print(f"Username: {data[site]['username']}")
        print(f"Password: {data[site]['password']}")
    else:
        print("Site not found.")

@logger
def delete_password(site):
    data = load_data()

    if site in data:
        del data[site]
        save_data(data)
        print(f"{site} deleted successfully.")
        log_message(f"Deleted Password for {site}")
    else:
        print("Site not found.")
        log_message(f"Delete failed: site not found")