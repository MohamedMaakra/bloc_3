from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'votre_cle_secrete'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/jo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    key = db.Column(db.String(36), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.email}', Admin: {self.is_admin})"

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

if __name__ == '__main__':
    app.run(debug=True)
