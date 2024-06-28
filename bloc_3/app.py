from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_cle_secrete'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/jo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Définition du modèle User SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# Route pour créer un nouvel utilisateur
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"message": "Tous les champs sont requis"}), 400

    # Vérifier si l'utilisateur existe déjà
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "Cet utilisateur existe déjà"}), 409

    # Créer un nouvel utilisateur
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Utilisateur créé avec succès"}), 201

# Route pour vérifier l'existence d'un utilisateur
@app.route('/api/users/<username>', methods=['GET'])
def check_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"message": "Utilisateur trouvé"}), 200
    else:
        return jsonify({"message": "Utilisateur non trouvé"}), 404

if __name__ == '__main__':
    app.run(debug=True)
