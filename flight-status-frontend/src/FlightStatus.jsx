import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FlightStatus = () => {
  const [flights, setFlights] = useState([]);
  const [subscribedFlights, setSubscribedFlights] = useState([]);
  const [userId, setUserId] = useState('user1'); 
  const [fcmToken, setFcmToken] = useState('');  

  useEffect(() => {
    const fetchFlights = async () => {
      try {
        const response = await axios.get('http://localhost:5000/flights');
        setFlights(response.data);
      } catch (error) {
        console.error('Error fetching flight data:', error);
      }
    };

    fetchFlights();
  }, []);

  const handleSubscribe = async (flightNumber) => {
    try {
      const response = await axios.post('http://localhost:5000/subscribe', {
        userId,
        fcmToken,
        subscribedFlights: [...subscribedFlights, flightNumber],
      });
      setSubscribedFlights([...subscribedFlights, flightNumber]);
      console.log(response.data.message);
    } catch (error) {
      console.error('Error subscribing to flight:', error);
    }
  };

  return (
    <div>
      <h1>Flight Status</h1>
      <table>
        <thead>
          <tr>
            <th>Flight Number</th>
            <th>Status</th>
            <th>Departure</th>
            <th>Arrival</th>
            <th>Gate</th>
            <th>Subscribe</th>
          </tr>
        </thead>
        <tbody>
          {flights.map((flight) => (
            <tr key={flight.flightNumber}>
              <td>{flight.flightNumber}</td>
              <td>{flight.status}</td>
              <td>{new Date(flight.departure).toLocaleString()}</td>
              <td>{new Date(flight.arrival).toLocaleString()}</td>
              <td>{flight.gate}</td>
              <td>
                <button onClick={() => handleSubscribe(flight.flightNumber)}>
                  Subscribe
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default FlightStatus;
