from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modèle User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    key = db.Column(db.String(255), nullable=False)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.email

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
