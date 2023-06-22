from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    age = db.Column(db.Float, nullable=False)
    owner_details = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"Patient(name='{self.name}', details='{self.details}', weight='{self.weight}', age='{self.age}', owner_details='{self.owner_details}')"