from math import radians, sin, cos, sqrt, atan2


# ---------------------------------------------
# Service Center Class
# ---------------------------------------------
class ServiceCenter:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude


# ---------------------------------------------
# Calculate Distance using Haversine Formula
# ---------------------------------------------
def haversine(lat1, lon1, lat2, lon2):
    EARTH_RADIUS = 6371  # km

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return EARTH_RADIUS * c


# ---------------------------------------------
# Geo Service Recommendation Algorithm
# ---------------------------------------------
def geo_service_algorithm(vehicle_lat,
                          vehicle_lon,
                          fault_code,
                          severity,
                          service_centers):

    # Dynamic Geofence Radius
    if severity.upper() == "LOW":
        radius = 5

    elif severity.upper() == "MEDIUM":
        radius = 3

    elif severity.upper() == "HIGH":
        radius = 10

    else:
        radius = 5

    nearby_centers = []

    for center in service_centers:

        distance = haversine(
            vehicle_lat,
            vehicle_lon,
            center.latitude,
            center.longitude
        )

        if distance <= radius:
            nearby_centers.append(
                (center.name, distance)
            )

    nearby_centers.sort(key=lambda x: x[1])

    print("\n============================================")
    print("      VEHICLE DIAGNOSTIC REPORT")
    print("============================================")
    print(f"Fault Code          : {fault_code}")
    print(f"Fault Severity      : {severity}")
    print(f"GeoFence Radius     : {radius} km")
    print(f"Vehicle Location    : ({vehicle_lat}, {vehicle_lon})")
    print("============================================")

    if len(nearby_centers) == 0:

        print("\nNo Authorized Service Center Found.")
        return

    print("\nNearby Authorized Service Centers\n")

    for i, center in enumerate(nearby_centers, start=1):

        print(f"{i}. {center[0]}")
        print(f"   Distance : {center[1]:.2f} km")

        if severity.upper() == "HIGH":
            recommendation = "Visit Immediately"

        elif severity.upper() == "MEDIUM":
            recommendation = "Visit at Earliest Convenience"

        else:
            recommendation = "Monitor Vehicle"

        print(f"   Recommendation : {recommendation}")
        print("--------------------------------------------")


# ---------------------------------------------
# Authorized Service Centers Database
# ---------------------------------------------
service_centers = [

    ServiceCenter(
        "Royal Enfield Gurgaon",
        28.4595,
        77.0266
    ),

    ServiceCenter(
        "Royal Enfield Delhi",
        28.6139,
        77.2090
    ),

    ServiceCenter(
        "Royal Enfield Noida",
        28.5355,
        77.3910
    ),

    ServiceCenter(
        "Royal Enfield Cyber City",
        28.4940,
        77.0890
    ),

    ServiceCenter(
        "Royal Enfield MG Road",
        28.4802,
        77.0805
    )

]


# ---------------------------------------------
# Simulated Vehicle Data
# ---------------------------------------------
vehicle_latitude = 28.4600
vehicle_longitude = 77.0301

fault_code = "DTC-P0420"
fault_severity = "MEDIUM"


# ---------------------------------------------
# Execute Algorithm
# ---------------------------------------------
geo_service_algorithm(
    vehicle_latitude,
    vehicle_longitude,
    fault_code,
    fault_severity,
    service_centers
)