import requests
import json
from flatten_json import flatten

weather_key = ''
exec(open('.env').read())

_url = 'http://api.weatherapi.com/v1/history.json?key={}&q=28.6,77.2&dt=2022-06-01'.format(weather_key)

# get request to test weather api with key and history endpoint
response_API = requests.get(_url)
response_json = ''

if response_API.status_code == 200:
    response_json = json.loads(response_API.text)
    
    for key, value in flatten(response_json).items():
        print(key, value, sep=': ')
else:
    print('Error response code', response_API.status_code)
    print('Response Reason:', response_API.reason)
    print('Response Text:', response_API.text)
    

