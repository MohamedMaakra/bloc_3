from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import os
from dotenv import load_dotenv
from offer_routes import offer_bp
from models import db, User, Offer
from config import config
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# Charger les variables d'environnement depuis .env
load_dotenv()

# Enregistrer CORS pour les routes d'API
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000", "methods": ["GET", "POST", "PUT", "DELETE"], "allow_headers": ["Content-Type", "Authorization"]}})

# Enregistrer le Blueprint pour les routes d'offres
app.register_blueprint(offer_bp)

# Fonction pour créer l'administrateur par défaut
def create_default_admin():
    default_admin_email = os.getenv('DEFAULT_ADMIN_EMAIL')
    default_admin_password = os.getenv('DEFAULT_ADMIN_PASSWORD')
    default_admin_nom = 'Admin'
    default_admin_prenom = 'User'

    existing_admin = User.query.filter_by(email=default_admin_email).first()
    if not existing_admin:
        user_key = str(uuid.uuid4())
        hashed_password = generate_password_hash(default_admin_password, method='pbkdf2:sha256', salt_length=8)
        new_admin = User(email=default_admin_email, password=hashed_password, key=user_key, nom=default_admin_nom, prenom=default_admin_prenom, is_admin=True)
        db.session.add(new_admin)
        db.session.commit()
        print(f"Admin par défaut créé avec email: {default_admin_email}")

# Créer l'administrateur par défaut lors du démarrage de l'application
with app.app_context():
    db.create_all()
    create_default_admin()

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in '!@#$%^&*(),.?":{}|<>' for char in password):
        return False
    return True

# Routes pour l'inscription et la connexion des utilisateurs
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    nom = data.get('nom')
    prenom = data.get('prenom')

    # Vérification des champs requis
    if not email or not password or not nom or not prenom:
        return jsonify({"error": "Les champs 'email', 'password', 'nom' et 'prenom' sont requis"}), 400

    if not validate_password(password):
        return jsonify({"error": "Le mot de passe doit contenir au moins 8 caractères, une majuscule, une minuscule, un chiffre et un caractère spécial"}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "Cet email est déjà utilisé"}), 409

    user_key = str(uuid.uuid4())
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
    new_user = User(email=email, password=hashed_password, key=user_key, nom=nom, prenom=prenom, is_admin=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Utilisateur créé avec succès", "key": user_key}), 201

# Seulement une définition pour /api/signin
@app.route('/api/signin', methods=['POST'])
def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Les champs 'email' et 'password' sont requis"}), 400

    user = User.query.filter_by(email=email).first()

    if user and user.lockout_time and user.lockout_time > datetime.utcnow():
        return jsonify({"message": "Compte verrouillé. Réessayez plus tard"}), 403

    if user and check_password_hash(user.password, password):
        user.failed_attempts = 0
        user.lockout_time = None
        db.session.commit()
        return jsonify({"message": "Connexion réussie", "key": user.key, "is_admin": user.is_admin}), 200
    else:
        if user:
            user.failed_attempts += 1
            if user.failed_attempts >= 5:
                user.lockout_time = datetime.utcnow() + timedelta(minutes=15)
            db.session.commit()
        return jsonify({"message": "Adresse email ou mot de passe incorrect"}), 401

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
