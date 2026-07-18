from math import radians
from math import sin
from math import cos
from math import sqrt
from math import atan2


def haversine(lat1, lon1, lat2, lon2):

    R = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        +
        cos(radians(lat1))
        *
        cos(radians(lat2))
        *
        sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def recommend_service(vehicle_lat,
                      vehicle_lon,
                      severity,
                      centers):

    if severity == "LOW":
        radius = 5

    elif severity == "MEDIUM":
        radius = 3

    else:
        radius = 10

    result = []

    for center in centers:

        distance = haversine(
            vehicle_lat,
            vehicle_lon,
            center.latitude,
            center.longitude
        )

        if distance <= radius:

            result.append(
                (center.name, distance)
            )

    result.sort(key=lambda x: x[1])

    return result