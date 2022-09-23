import requests

city = 'Kharkiv'
URL = 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'.format(city_name=city)

def get_data(url: str = None):
    response = requests.get(url)
    data = response.json()
    return data

print(get_data(URL))
