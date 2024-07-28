from pymongo import MongoClient

client = MongoClient('YOUR_MONGODB_URL')
db = client['flightdb']
flights_collection = db['flights']

flights = [
    {"flightNumber": "AA101", "status": "On Time", "departure": "2023-07-25T08:00:00Z", "arrival": "2023-07-25T12:00:00Z", "gate": "A1"},
    {"flightNumber": "BA202", "status": "Delayed", "departure": "2023-07-25T09:00:00Z", "arrival": "2023-07-25T13:00:00Z", "gate": "B2"},
    {"flightNumber": "CA303", "status": "Cancelled", "departure": "2023-07-25T10:00:00Z", "arrival": "2023-07-25T14:00:00Z", "gate": "C3"},
    {"flightNumber": "DA404", "status": "On Time", "departure": "2023-07-25T11:00:00Z", "arrival": "2023-07-25T15:00:00Z", "gate": "D4"},
    {"flightNumber": "EA505", "status": "Delayed", "departure": "2023-07-25T12:00:00Z", "arrival": "2023-07-25T16:00:00Z", "gate": "E5"},
    {"flightNumber": "FA606", "status": "On Time", "departure": "2023-07-25T13:00:00Z", "arrival": "2023-07-25T17:00:00Z", "gate": "F6"},
    {"flightNumber": "GA707", "status": "On Time", "departure": "2023-07-25T14:00:00Z", "arrival": "2023-07-25T18:00:00Z", "gate": "G7"},
    {"flightNumber": "HA808", "status": "Delayed", "departure": "2023-07-25T15:00:00Z", "arrival": "2023-07-25T19:00:00Z", "gate": "H8"},
    {"flightNumber": "IA909", "status": "Cancelled", "departure": "2023-07-25T16:00:00Z", "arrival": "2023-07-25T20:00:00Z", "gate": "I9"},
    {"flightNumber": "JA1010", "status": "On Time", "departure": "2023-07-25T17:00:00Z", "arrival": "2023-07-25T21:00:00Z", "gate": "J10"}
]

flights_collection.insert_many(flights)
print("Initial flight data inserted.")
