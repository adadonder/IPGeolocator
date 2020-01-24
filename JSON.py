import requests


class JSON:

    def __init__(self, address):
        self.address = address

    def parse_json(self):
        API_URL = "http://ip-api.com/json/" + self.address
        response = requests.get(API_URL)
        response = response.json()
        try:
            print("\n")
            print("Geolocation results for " + response["query"] + ":")
            print("Country:                " + response["country"])
            print("City:                   " + response["city"])
            print("Region:                 " + response["regionName"])
            print("Coordinates:            " + "(" + str(response["lat"]) + " , " + str(response["lon"]) + ")")
            print("Zip:                    " + response["zip"])
            print("ISP:                    " + response["isp"])
            print("Organization:           " + response["org"])
        except KeyError:
            print("Please provide a global IP address to geolocate. For help use \"-h\" or \"--help\"")
