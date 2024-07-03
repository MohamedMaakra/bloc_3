from flask import Blueprint, jsonify, request
from models import db, Offer  # Assurez-vous d'importer votre instance db et le modèle Offer

# Définition du Blueprint pour les offres
offer_bp = Blueprint('offer_bp', __name__)

@offer_bp.route('/api/offers', methods=['GET'])
def get_offers():
    offers = Offer.query.all()
    return jsonify([offer.serialize() for offer in offers]), 200

@offer_bp.route('/api/offers/<int:offer_id>', methods=['GET'])
def get_offer(offer_id):
    offer = Offer.query.get_or_404(offer_id)
    return jsonify(offer.serialize()), 200

@offer_bp.route('/api/offers', methods=['POST'])
def create_offer():
    data = request.get_json()
    titre = data.get('titre')
    description = data.get('description')
    prix = data.get('prix')
    details = data.get('details')
    nombre_personnes = data.get('nombre_personnes', 1)  # Par défaut, une personne

    if not titre or not prix:
        return jsonify({"message": "Les champs 'titre' et 'prix' sont requis"}), 400

    new_offer = Offer(titre=titre, description=description, prix=prix, details=details, nombre_personnes=nombre_personnes)
    db.session.add(new_offer)

    try:
        db.session.commit()
        return jsonify({"message": "Nouvelle offre créée avec succès"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Erreur lors de la création de l'offre: {str(e)}"}), 500

@offer_bp.route('/api/offers/<int:offer_id>', methods=['PUT'])
def update_offer(offer_id):
    offer = Offer.query.get_or_404(offer_id)
    data = request.get_json()

    if not data:
        return jsonify({"message": "Aucune donnée reçue pour la mise à jour"}), 400

    if 'titre' in data:
        offer.titre = data['titre']
    if 'description' in data:
        offer.description = data['description']
    if 'prix' in data:
        offer.prix = data['prix']
    if 'details' in data:
        offer.details = data['details']
    if 'nombre_personnes' in data:
        offer.nombre_personnes = data['nombre_personnes']

    try:
        db.session.commit()
        return jsonify({'message': 'Offre mise à jour avec succès'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Erreur lors de la mise à jour de l\'offre: {str(e)}'}), 500

@offer_bp.route('/api/offers/<int:offer_id>', methods=['DELETE'])
def delete_offer(offer_id):
    offer = Offer.query.get_or_404(offer_id)

    try:
        db.session.delete(offer)
        db.session.commit()
        return jsonify({'message': 'Offre supprimée avec succès'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Erreur lors de la suppression de l\'offre: {str(e)}'}), 500

# Assurez-vous de retourner le Blueprint pour l'enregistrement dans l'application principale
# Aucune action d'enregistrement ne doit être effectuée ici, car cela devrait être fait dans le fichier principal de l'application

