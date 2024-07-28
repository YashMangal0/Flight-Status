from pymongo import MongoClient

client = MongoClient('YOUR_MONGODB_URL')
db = client['flightdb']
users_collection = db['users']

users = [
    {"userId": "user1", "fcmToken": "TOKEN1", "subscribedFlights": ["AA101", "BA202"]},
    {"userId": "user2", "fcmToken": "TOKEN2", "subscribedFlights": ["CA303", "DA404"]},
    {"userId": "user3", "fcmToken": "TOKEN3", "subscribedFlights": ["EA505", "FA606"]},
]

users_collection.insert_many(users)
print("Initial user data inserted.")
