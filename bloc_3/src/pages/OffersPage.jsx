import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css';
import '../OfferPages.css';
import { CartContext } from '../CartContext';

const OfferPage = () => {
  const { addToCart } = useContext(CartContext);
  const [offers, setOffers] = useState([]);

  useEffect(() => {
    // Fonction pour récupérer les offres depuis votre API
    const fetchOffers = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/offers');
        console.log("Données reçues : ", response.data);
        setOffers(response.data);
      } catch (error) {
        console.error('Erreur lors de la récupération des offres :', error);
      }
    };

    fetchOffers(); 
  }, []);

  return (
    <div className="container mt-5">
      <h2 className="text-center mb-4">Nos Offres</h2>
      <div className="row">
        {offers.length > 0 ? (
          offers.map((offer, index) => (
            <div key={offer.id || index} className="col-md-4">
              <div className="card mb-4">
                <div className="card-body">
                  <h5 className="card-title">{offer.titre}</h5>
                  <p className="card-text">{offer.description}</p>
                  <p className="card-text"><strong>{offer.prix} €</strong></p>
                  <p className="card-text">{offer.details}</p>
                  <button
                    className="btn btn-primary w-100"
                    onClick={() => addToCart(offer)}
                  >
                    Choisir cette offre
                  </button>
                </div>
              </div>
            </div>
          ))
        ) : (
          <p className="col">Aucune offre disponible.</p>
        )}
      </div>
    </div>
  );
};

export default OfferPage;
