from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager


data_manager = DataManager()
flight_data = FlightData()
notification_manager = NotificationManager()
sheet_data = data_manager.get_data()


for data in sheet_data:
    if data["iataCode"] == "":
        flight_search = FlightSearch()
        data["iataCode"] = flight_search.get_code(data["city"])

data_manager.dist_data = sheet_data
data_manager.update()

for row in sheet_data:
    new_data = flight_data.get_info(row['iataCode'])
    price = new_data["price"]
    if price < row["lowestPrice"]:
        notification_manager.send_mail(subject="Low price detected!", 
                                       sms=(f"Low price alert! \n Only ${price} to fly from London \
                                            to {row['city']}, \
                                            from {(new_data['route'][0]['local_arrival']).split('T')[0]} \
                                            to {(new_data['route'][-1]['local_departure']).split('T')[0]}\n \
                                            Flight has {len(new_data['route']) - 2} stop overs"))  