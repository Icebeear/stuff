import requests
class FlightSearch:
    def get_code(self, city):
        params = {
            "term": city,
            "limit": 1,
        }

        head = {
            "apikey": "Wx0kDb6JNSK0F4G_xuEOmppedSTkfyHZ",
        }

        code_response = requests.get(url="https://api.tequila.kiwi.com/locations/query", params=params, headers=head).json()
        try:
            return code_response["locations"][0]["code"]
        except:
            return "No flight data"