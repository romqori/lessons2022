import requests
import pprint

URL = 'https://script.google.com/macros/s/AKfycbxa__2_Jhe608RgI4baodiYcGWqP2WRyu2onqPxFIwZa6L7BXYnf55ItbGz_BoIcl8L/exec'


def get_data(url:str=None):
    response = requests.get(URL)
    data = response.json()
    return data

