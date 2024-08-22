from geopy.geocoders import Nominatim
import requests 



url = "https://api-ubt.mukuru.com/taurus/v1/resources/pay-out-partners"

def main():

    # res = requests.get(url)
    # print(res.json())



    # importing geopy library
    
    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")
    
    # entering the location name
    getLoc = loc.geocode("Rosebank Parkwood")
    
    # printing address
    print(getLoc.address)
    
    # printing latitude and longitude
    print("Latitude = ", getLoc.latitude, "\n")
    print("Longitude = ", getLoc.longitude)

    
    


if __name__ == "__main__":
    main()