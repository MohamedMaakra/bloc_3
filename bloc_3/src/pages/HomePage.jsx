import React from "react";
import EventCard from "../components/EventCard";
import athletismeImage from '../images/Athlétisme.jpg';
import gymnastiqueImage from '../images/Gymnastique.jpg';
import natationeImage from '../images/Natation.jpg';
import cyclismeImage from '../images/Cyclisme.jpg';

const HomePage = () => {
  // Exemple de données d'épreuves
  const events = [
    { id: 1, name: "Natation", date: "25 Juillet 2024", location: "Piscine Aquatique", image: natationeImage },
    { id: 2, name: "Athlétisme", date: "27 Juillet 2024", location: "Stade Olympique", image: athletismeImage },
    { id: 3, name: "Cyclisme", date: "29 Juillet 2024", location: "Vélodrome", image: cyclismeImage },
    { id: 4, name: "Gymnastique", date: "30 Juillet 2024", location: "Gymnase Principal", image: gymnastiqueImage },
    // Ajout d'une nouvelle épreuve
  ];

  return (
    <div className="home">
      <h2>Bienvenue aux Jeux Olympiques de France 2024</h2>
      <p>
        Les Jeux Olympiques de 2024 à Paris sont l'événement sportif mondial le plus
        attendu de l'année. Venez assister à des compétitions incroyables dans divers
        sports et soutenez les athlètes alors qu'ils visent l'excellence.
      </p>
      <div className="events-list">
        {events.map((event) => (
          <EventCard key={event.id} event={event} />
        ))}
      </div>
    </div>
  );
};

export default HomePage;
