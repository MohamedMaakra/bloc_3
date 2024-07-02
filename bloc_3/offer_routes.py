from flask import Flask, jsonify, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from models import db, Offer  # Assurez-vous d'importer votre instance db et le modèle Offer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/jo'  # Remplacez par votre URI de base de données
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Définition du Blueprint pour les offres
offer_bp = Blueprint('offer_bp', __name__)

@offer_bp.route('/api/offers', methods=['GET'])
def get_offers():
    offers = Offer.query.all()
    return jsonify([offer.serialize() for offer in offers])

@offer_bp.route('/api/offers/<int:offer_id>', methods=['GET'])
def get_offer(offer_id):
    offer = Offer.query.get_or_404(offer_id)
    return jsonify(offer.serialize())

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
    db.session.commit()

    return jsonify({"message": "Nouvelle offre créée avec succès"}), 201

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

# Enregistrez le Blueprint pour les routes d'offres dans l'application Flask
app.register_blueprint(offer_bp)

if __name__ == '__main__':
    app.run(debug=True)
