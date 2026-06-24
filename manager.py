import json

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    
def add_password(site, username, password):
    data = load_data()

    data[site] = {
        "username": username,
        "password": password
    }

    save_data(data)

def view_passwords():
    data = load_data()

    if not data:
        print("No passwords stored.")
        return
    for site, details in data.items():
        print(f"Site: {site}")
        print(f"Username: {details['username']}")
        print(f"Password: {details['password']}")
        print("-" * 20)
    
def get_password(site):
    data = load_data()

    if site in data:
        print(f"Site: {site}")
        print(f"Username: {data[site]['username']}")
        print(f"Password: {data[site]['password']}")
    else:
        print("Site not found.")

def delete_password(site):
    data = load_data()

    if site in data:
        del data[site]
        save_data(data)
        print(f"{site} deleted successfully.")
    else:
        print("Site not found.")