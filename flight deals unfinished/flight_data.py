import requests
import datetime as dt
time = dt.datetime.now() 
time_to = time + dt.timedelta(days=180)

class FlightData:
    def get_info(self, code):

        head = { 
            "apikey": "Wx0kDb6JNSK0F4G_xuEOmppedSTkfyHZ",
        }

        price_params = {
            "fly_from": "LON",
            "fly_to": code,
            "date_from": time.strftime(f"{'%d'}/{'%m'}/{'%Y'}"),
            "date_to": time_to.strftime(f"{'%d'}/{'%m'}/{'%Y'}"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "limit": 1,
        }

        price_response = requests.get(url="https://api.tequila.kiwi.com/v2/search", params=price_params, headers=head).json()
        return price_response["data"][0]