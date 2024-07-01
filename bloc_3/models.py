from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Offer('{self.title}', '{self.price}')"
