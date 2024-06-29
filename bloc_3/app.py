from flask import Flask, jsonify, request, make_response
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

    def __repr__(self):
        return f"User('{self.email}')"

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
    new_user = User(email=email, password=hashed_password, key=user_key)
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
        response = jsonify({"message": "Connexion réussie", "key": user.key})
        response.set_cookie('userToken', user.key, httponly=True, samesite='Strict')
        return response, 200
    else:
        return jsonify({"message": "Adresse email ou mot de passe incorrect"}), 401

@app.route('/api/logout', methods=['POST'])
def logout():
    response = jsonify({"message": "Déconnexion réussie"})
    response.delete_cookie('userToken')
    return response, 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
