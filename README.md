##Flight Status Tracker

Flight Status Tracker is a web application that provides real-time updates on flight statuses, including delays, cancellations, gate changes, and dynamic time updates for departure and arrival. The system also sends notifications about flight status changes using Firebase Cloud Messaging.

#Technologies Used
Frontend: HTML, CSS, React.js
Backend: Python, Flask
Database: MongoDB
Notifications: Firebase Cloud Messaging

# Ensure you have the following installed:
Node.js
Python
MongoDB

##Installation#

#Clone the Repository
git clone https://github.com/yourusername/flight-status-tracker.git
cd flight-status-tracker
Backend Setup

#Create and activate a virtual environment:
py -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

#Install the required packages:
pip install Flask flask-cors pymongo
Run the backend server:
py app.py

#Frontend Setup
Navigate to the frontend directory:
cd frontend

#Install the required packages:
npm install

#Start the frontend application:
npm start

#Database Setup
Insert Initial Flight Data
Use the provided script or MongoDB client to insert sample flight data into the flights collection.
Usage
Once the backend server and frontend application are running, you can access the Flight Status Tracker in your browser. The application will display real-time flight statuses and send notifications for any changes.

Contributing
Feel free to fork the repository, make improvements, and submit pull requests. For any questions or suggestions, open an issue or contact the maintainer directly.
