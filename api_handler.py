import requests
import time

class GeoAPI:
    
    
    __API_URL = "https://api.openweathermap.org"
    __API_KEY = "d81015613923e3e435231f2740d5610b"
    __LAT = "-35.836948753554054"
    __LON = "-61.870523905384076"
    __status = 200
       

    @classmethod
    def is_hot_in_pehuajo(cls):
        """
        Precondition: true  \n
        Postcondition: temp: bool === if the temperature in pehuajo is greater than 28° 
        """
        temp = None
        req_param = cls.__API_URL + "/data/2.5/weather?lat=" + cls.__LAT + "&lon=" + cls.__LON + "&appid=" + cls.__API_KEY 
        try:
            #start = time.time()#
            req = requests.get(req_param, timeout=3)
            req.raise_for_status()
            #end = time.time()#

            temp = req.json()["main"]["temp"]
            
            #print(end - start) #
         
        except requests.exceptions.HTTPError as err:
            __status = req.status_code
            raise SystemExit(err)
           
        else:
            temp = temp - 273.15
            return temp > float(28)

    @classmethod      
    def set_lat_long(cls, lat, lon):
        """
        Precondition: lat: str and lon: str  and lat.isdigit() and lon.isdigit() \n
        Postcondition: temp: bool === if the temperature in Pehuajo is greater than 28° 
        """
        cls.__LAT = str(lat)    
        cls.__LON = str(lon)


