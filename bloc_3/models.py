from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    key = db.Column(db.String(36), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.email}', Admin: {self.is_admin})"

class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    prix = db.Column(db.Float(precision=2), nullable=False)
    details = db.Column(db.Text)
    nombre_personnes = db.Column(db.Integer, default=1, nullable=False)

    def __repr__(self):
        return f"Offer('{self.titre}', Prix: {self.prix}, Personnes: {self.nombre_personnes})"

    def serialize(self):
        return {
            'id': self.id,
            'titre': self.titre,
            'description': self.description,
            'prix': self.prix,
            'details': self.details,
            'nombre_personnes': self.nombre_personnes
        }
