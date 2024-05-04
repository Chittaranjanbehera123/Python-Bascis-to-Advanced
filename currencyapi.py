import requests
import json

countrycode = input("Enter country code: ")
url = f"https://api.exchangerate-api.com/v4/latest/{countrycode}"

try:
    req = requests.get(url)
    req.raise_for_status()  # Raise an HTTPError for bad responses

    if req.status_code == 200:
        data = req.json()
        print(type(data))
        print(data)
    else:
        print(f"Error: {req.status_code} - {req.text}")

except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)

except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)

except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)

except requests.exceptions.RequestException as err:
    print("Request Error:", err)
