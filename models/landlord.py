from db import db


class LandLordModel(db.Model):
    __tablename__ = 'landlords'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    phone = db.Column(db.Integer, unique=True)

    properties = db.relationship('PropertyModel', lazy='dynamic')

    def __init__(self, username, first_name, last_name, email, phone):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone


    def __str__(self):
        return self.first_name

    @classmethod
    def find_by_email(self, email):
        return self.query.filter_by(email=email).first()

    @classmethod
    def find_by_username(self, username):
        return self.query.filter_by(username=username).first()
    
    @classmethod
    def find_by_phone(self, phone):
        return self.query.filter_by(phone=phone).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def json(self):
        return {'first_name':self.first_name, 'last_name':self.last_name, 'properties':[property.json() for property in self.properties.all()]}

    