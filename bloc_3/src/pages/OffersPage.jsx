import React, { useContext } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import '../OfferPages.css';
import { CartContext } from '../CartContext';

const offers = [
  {
    id: 1,
    title: "Offre Solo",
    description: "Accès pour 1 personne à tous les événements.",
    price: "50€",
    details: "Profitez des jeux olympiques en solo avec un accès à toutes les épreuves pour une personne."
  },
  {
    id: 2,
    title: "Offre Duo",
    description: "Accès pour 2 personnes à tous les événements.",
    price: "90€",
    details: "Partagez l'expérience des jeux olympiques avec un ami ou un membre de votre famille avec un accès pour deux personnes."
  },
  {
    id: 3,
    title: "Offre Familiale",
    description: "Accès pour 4 personnes à tous les événements.",
    price: "150€",
    details: "Vivez les jeux olympiques en famille avec un accès complet pour quatre personnes à toutes les épreuves."
  }
];

const OfferPage = () => {
  const { addToCart } = useContext(CartContext);

  return (
    <div className="container mt-5">
      <h2 className="text-center mb-4">Nos Offres</h2>
      <div className="row">
        {offers.map(offer => (
          <div key={offer.id} className="col-md-4">
            <div className="card mb-4">
              <div className="card-body">
                <h5 className="card-title">{offer.title}</h5>
                <p className="card-text">{offer.description}</p>
                <p className="card-text"><strong>{offer.price}</strong></p>
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
        ))}
      </div>
    </div>
  );
};

export default OfferPage;
