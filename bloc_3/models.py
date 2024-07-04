from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modèle User
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    key = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    failed_attempts = db.Column(db.Integer, default=0)
    lockout_time = db.Column(db.DateTime, nullable=True)

    def __init__(self, email, password, nom, prenom, key, is_admin=False):
        self.email = email
        self.password = password
        self.nom = nom
        self.prenom = prenom
        self.key = key
        self.is_admin = is_admin
        self.failed_attempts = 0  # Initialiser à zéro lors de la création
        self.lockout_time = None  # Initialiser à None lors de la création

    def __repr__(self):
        return f"<User {self.email}>"

# Modèle Offer
class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    prix = db.Column(db.Float, nullable=False)
    details = db.Column(db.Text)
    nombre_personnes = db.Column(db.Integer, default=1)

    def serialize(self):
        return {
            'id': self.id,
            'titre': self.titre,
            'description': self.description,
            'prix': self.prix,
            'details': self.details,
            'nombre_personnes': self.nombre_personnes
            # Ajoutez d'autres champs si nécessaire
        }
