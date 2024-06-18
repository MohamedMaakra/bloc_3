import React from 'react';

const EventCard = ({ event }) => {
  return (
    <div className="event-card">
      <h3>{event.name}</h3>
      {event.image && <img src={event.image} alt={event.name} />} {/* Vérifiez l'utilisation de l'image */}
      <p>Date : {event.date}</p>
      <p>Lieu : {event.location}</p>
    </div>
  );
};

export default EventCard;
