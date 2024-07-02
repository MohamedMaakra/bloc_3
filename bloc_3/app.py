from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from models import db, User, Offer  # Assurez-vous d'importer db, User et Offer depuis models.py
from offer_routes import offer_bp  # Assurez-vous d'importer le Blueprint offer_bp depuis offer_routes.py

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'votre_cle_secrete'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/jo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisez l'instance db avec l'application Flask
db.init_app(app)

# Enregistrez le Blueprint pour les routes d'offres
app.register_blueprint(offer_bp)

# Fonction pour créer l'administrateur par défaut
def create_default_admin():
    default_admin_email = 'admin@live.fr'
    default_admin_password = 'Admin13'  

    existing_admin = User.query.filter_by(email=default_admin_email).first()
    if not existing_admin:
        user_key = str(uuid.uuid4())
        hashed_password = generate_password_hash(default_admin_password, method='pbkdf2:sha256', salt_length=8)
        new_admin = User(email=default_admin_email, password=hashed_password, key=user_key, is_admin=True)
        db.session.add(new_admin)
        db.session.commit()
        print(f"Admin par défaut créé avec email: {default_admin_email}")

# Créez l'administrateur par défaut lors du démarrage de l'application
with app.app_context():
    db.create_all()
    create_default_admin()

# Routes pour l'inscription et la connexion des utilisateurs
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Les champs 'email' et 'password' sont requis"}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "Cet email est déjà utilisé"}), 409

    user_key = str(uuid.uuid4())
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
    new_user = User(email=email, password=hashed_password, key=user_key, is_admin=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Utilisateur créé avec succès", "key": user_key}), 201

@app.route('/api/signin', methods=['POST'])
def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Les champs 'email' et 'password' sont requis"}), 400

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Connexion réussie", "key": user.key, "is_admin": user.is_admin}), 200
    else:
        return jsonify({"message": "Adresse email ou mot de passe incorrect"}), 401

# Route pour créer une nouvelle offre
@app.route('/api/offers', methods=['POST'])
def create_offer():
    data = request.get_json()
    titre = data.get('titre')
    description = data.get('description')
    prix = data.get('prix')
    details = data.get('details')
    nombre_personnes = data.get('nombre_personnes', 1)  # Nombre de personnes par défaut

    if not titre or not prix:
        return jsonify({"message": "Les champs 'titre' et 'prix' sont requis"}), 400

    new_offer = Offer(titre=titre, description=description, prix=prix, details=details, nombre_personnes=nombre_personnes)
    db.session.add(new_offer)
    db.session.commit()

    return jsonify({"message": "Nouvelle offre créée avec succès"}), 201

if __name__ == '__main__':
    app.run(debug=True)
