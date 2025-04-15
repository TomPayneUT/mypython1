import requests
import json

print('Welcome to Weather Alerts')

while True:
    state = input('Type in a 2 letter state code (or Q to quit): ').upper()

    if state == 'Q':
        print('goodbye')
        break


    response = requests.get(f'https://api.weather.gov/alerts/active?area={state}')

    my_dict = json.loads(response.text)

    for item in my_dict['features']:


        area = item['properties']['areaDesc']
        event = item['properties']['event']
        headline = item['properties']['headline']

        print(area)
        print(event)
        print(headline)
        print('-'*50)