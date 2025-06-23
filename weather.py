import sys
import requests

API_KEY = '43d7e71708054c428ad150519241806'
URL = 'http://api.weatherapi.com/v1/current.json'


def get_weather_data(location):
    try:
        url = f'{URL}?key={API_KEY}&q={location}'
        resp = requests.get(url, timeout=5)
        if resp.status_code != 200:
            print(
                f"API error \
                 {resp.status_code}: \
                 {resp.json().get('error', {}).get(
                     'message', 'Unknown error'
                     )}"
                )
            sys.exit(1)
        data = resp.json()
    
        if 'current' not in data or 'temp_c' not in data['current']:
            print(
                f'Unexpected API response. \
                Cannot retrieve current temperature in {location}'
                )
        return data['location']['name'], data['current']['temp_c']
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <city_name>")
        sys.exit(1)

    city = sys.argv[1].strip()
    if not city:
        print("Error: City name cannot be empty.")
        sys.exit(1)

location_name, temp_c = get_weather_data(city)

print(f"Current temperature in {location_name}: {temp_c}°C")
