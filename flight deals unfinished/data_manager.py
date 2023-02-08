import requests

URL = "https://api.sheety.co/3477170bf5d6e68f4c821752fdc23d83/flightDeals/prices"
URL2 = "https://api.sheety.co/3477170bf5d6e68f4c821752fdc23d83/flightDeals/users"

class DataManager:
    def __init__(self):
        self.dist_data = {}

    def get_data(self):
        sheet_endpoint = requests.get(url=URL).json()
        data = sheet_endpoint["prices"]
        return data

    def update(self):
        for row in self.dist_data:
            params = {
                "price": {
                    "iataCode": row["iataCode"],
                }
            } 
            requests.put(url=f"{URL}/{row['id']}", json=params)

    def add_user(self):
        print("Welcome to DMC Flight Club.\nWe find the best flight deals and email you")
        first_name = input("What is your first name?\n")
        last_name = input("What is your last name?\n")
        email1 = input("What is your email?\n")
        email2 = input("Type you email again.\n")

        if email1 == email2:
            params = {
                "user": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email1,
                }
            }
            requests.post(url=URL2, json=params)
            print("Success! You email has been added")
        else:
            print("Emails not same, try again")