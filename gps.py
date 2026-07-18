import requests


def get_live_location():

    try:

        url = "http://192.168.1.15:8080"

        response = requests.get(url)

        data = response.json()

        latitude = data["latitude"]
        longitude = data["longitude"]

        return latitude, longitude

    except Exception as e:

        print("GPS Error:", e)

        return None, None