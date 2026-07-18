import json
from service_center import ServiceCenter


def load_service_centers(filename):

    centers = []

    with open(filename, "r") as file:

        data = json.load(file)

        for item in data:

            centers.append(

                ServiceCenter(
                    item["name"],
                    item["latitude"],
                    item["longitude"]
                )

            )

    return centers