from geopy.geocoders import Nominatim
import requests 



url = "https://api-ubt.mukuru.com/taurus/v1/resources/pay-out-partners"



#  TODO: get user to pick country and enter their city to get actual location
def main():
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode("Rosebank South Africa")
    
    print("Address: ", getLoc.address)
    # print("Latitude = ", getLoc.latitude, "\n")
    # print("Longitude = ", getLoc.longitude)

    
    


if __name__ == "__main__":
    main()