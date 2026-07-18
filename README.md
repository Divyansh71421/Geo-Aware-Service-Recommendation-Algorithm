# Geo-Aware-Service-Recommendation-Algorithm
Provide the alert of vehicle to the user in phone device
# 🚗 Geo-Aware Service Recommendation Algorithm (GSRA)

An intelligent geofence-based recommendation system for connected vehicles that detects vehicle faults and recommends the nearest authorized service center based on the vehicle's real-time location and fault severity.

---

## 📖 Overview

The **Geo-Aware Service Recommendation Algorithm (GSRA)** is a proof-of-concept project that combines:

* Vehicle Diagnostics
* GPS Location Tracking
* Geofencing
* Fault Severity Analysis
* Intelligent Service Center Recommendation

Instead of simply showing nearby service centers, the system analyzes the severity of the detected fault and dynamically recommends the most suitable authorized service center within an adaptive search radius.

This concept is inspired by modern connected vehicle platforms and can be extended for integration with CAN, OBD-II, telematics, and cloud-based predictive maintenance systems.

---

# ✨ Features

* Real-time vehicle location support
* Dynamic geofence radius based on fault severity
* Haversine distance calculation
* Intelligent nearest service center recommendation
* REST API using Flask (can be migrated to FastAPI)
* JSON-based service center database
* Modular project architecture
* Easily extendable to CAN/OBD-II integration

---

# 🏗️ System Architecture

```text
                +----------------------+
                |    Connected Bike    |
                | (ECU / OBD-II / CAN) |
                +----------+-----------+
                           |
                           |
                   Vehicle Fault
                           |
                           v
                +----------------------+
                |   Mobile Application |
                |   GPS + Diagnostics  |
                +----------+-----------+
                           |
                     HTTP Request
                           |
                           v
                +----------------------+
                |   Flask REST Server  |
                |      (app.py)        |
                +----------+-----------+
                           |
                           |
          +----------------+----------------+
          |                                 |
          v                                 v
  GeoFence Algorithm             Service Center Database
 (algorithm.py)                (service_centers.json)
          |                                 |
          +----------------+----------------+
                           |
                           v
                Recommended Service Center
                           |
                           v
                    Mobile Notification
```

---

# 📂 Project Structure

```text
Geo-Aware-Service-Recommendation-Algorithm/

├── algorithm.py
├── app.py
├── database.py
├── gps.py
├── requirements.txt
├── service_center.py
├── service_centers.json
├── Geo_Fence_Algo.docx
├── README.md
└── LICENSE
```

---

# ⚙️ Technologies Used

* Python 3
* Flask
* JSON
* REST API
* Haversine Formula
* GPS
* Geofencing
* Git & GitHub

---

# 🧠 Algorithm Workflow

1. Detect vehicle fault.
2. Read Diagnostic Trouble Code (DTC).
3. Classify fault severity.
4. Obtain current GPS location.
5. Assign a geofence search radius.
6. Search nearby authorized service centers.
7. Calculate distances using the Haversine formula.
8. Sort service centers by proximity.
9. Recommend the nearest service center.
10. Return the result to the mobile application.

---

# 🚨 Fault Severity Mapping

| Severity | Search Radius |
| -------- | ------------: |
| LOW      |          5 km |
| MEDIUM   |         10 km |
| HIGH     |         20 km |

> These values are configurable and can be adjusted based on vehicle type or OEM requirements.

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Divyansh71421/Geo-Aware-Service-Recommendation-Algorithm.git
```

Move into the project folder:

```bash
cd Geo-Aware-Service-Recommendation-Algorithm
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python app.py
```

The API will be available at:

```text
http://localhost:5000
```

---

# 📡 API Example

## Request

**POST**

```text
/recommend
```

### Request Body

```json
{
  "latitude": 28.4600,
  "longitude": 77.0300,
  "fault_code": "P0420",
  "severity": "HIGH"
}
```

---

## Response

```json
{
  "fault_code": "P0420",
  "severity": "HIGH",
  "recommendations": [
    {
      "service_center": "Royal Enfield Gurgaon",
      "distance_km": 0.34
    }
  ]
}
```

---

# 🌍 Future Enhancements

* Bluetooth OBD-II integration
* CAN Bus integration
* UDS diagnostics
* Android application
* FastAPI backend
* Google Maps navigation
* Live traffic analysis
* Service center ratings
* Predictive maintenance using AI/ML
* Cloud deployment
* Vehicle health dashboard
* Push notifications

---

# 🎯 Potential Applications

* Connected Motorcycles
* Connected Cars
* Fleet Management
* Automotive OEMs
* Roadside Assistance
* Predictive Vehicle Maintenance
* Smart Mobility Platforms

---

# 📈 Roadmap

* [x] Geofence recommendation algorithm
* [x] REST API backend
* [x] Service center database
* [ ] Android mobile application
* [ ] Live GPS integration
* [ ] OBD-II support
* [ ] CAN Bus integration
* [ ] Google Maps integration
* [ ] Cloud deployment
* [ ] Predictive maintenance module

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you find an issue or have an enhancement idea, please open an issue or submit a pull request.

---

# 📄 License

This project is licensed under the MIT License. See the **LICENSE** file for details.

---

# 👨‍💻 Author

**Divyansh Singh**

GitHub: https://github.com/Divyansh71421

---

⭐ If you find this project useful, consider giving it a star on GitHub.
