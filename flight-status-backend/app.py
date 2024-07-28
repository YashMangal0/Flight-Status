from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import firebase_admin
from firebase_admin import credentials, messaging

app = Flask(__name__)
CORS(app)

# MongoDB setup
client = MongoClient('YOUR_MONGODB_URL')
db = client['flightdb']
flights_collection = db['flights']
subscriptions_collection = db['subscriptions']

cred = credentials.Certificate("YOUR_CREDENTIAL_FILE")
firebase_admin.initialize_app(cred)

def send_fcm_notification(token, message_body):
    message = messaging.Message(
        notification=messaging.Notification(
            title='Flight Status Update',
            body=message_body
        ),
        token=token
    )
    response = messaging.send(message)
    return response

@app.route('/flights', methods=['GET'])
def get_flights():
    flights = list(flights_collection.find({}, {'_id': 0}))
    return jsonify(flights)

@app.route('/update-flight-status', methods=['POST'])
def update_flight_status():
    data = request.get_json()
    flight_number = data['flightNumber']
    new_status = data['status']
    
    flights_collection.update_one(
        {'flightNumber': flight_number},
        {'$set': {'status': new_status}}
    )

    subscriptions = subscriptions_collection.find({'subscribedFlights': flight_number})
    for subscription in subscriptions:
        user_token = subscription['fcmToken']
        notification_message = f"Flight {flight_number} status has changed to {new_status}."
        send_fcm_notification(user_token, notification_message)
    
    return jsonify({'message': 'Flight status updated and notification sent.'})

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    user_id = data['userId']
    fcm_token = data['fcmToken']
    subscribed_flights = data['subscribedFlights']

    subscription = {
        'userId': user_id,
        'fcmToken': fcm_token,
        'subscribedFlights': subscribed_flights
    }

    subscriptions_collection.update_one(
        {'userId': user_id},
        {'$set': subscription},
        upsert=True
    )

    return jsonify({'message': 'Subscribed to flights successfully.'})

if __name__ == '__main__':
    app.run(debug=True)
