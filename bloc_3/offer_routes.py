# offer_routes.py

from flask import Blueprint, jsonify
from models import Offer

offer_bp = Blueprint('offer_bp', __name__)

@offer_bp.route('/api/offers', methods=['GET'])
def get_offers():
    offers = Offer.query.all()

    # Création de la liste des offres sous forme de dictionnaires
    offers_list = []
    for offer in offers:
        offer_data = {
            'id': offer.id,
            'title': offer.titre,
            'description': offer.description,
            'price': f"{offer.prix}€",
            'details': offer.details,
            'nombre_personnes': offer.nombre_personnes
        }
        offers_list.append(offer_data)

    # Renvoi de la liste des offres au format JSON
    return jsonify(offers_list)
