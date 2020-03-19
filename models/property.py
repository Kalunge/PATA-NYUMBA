from db import db

class PropertyModel(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(80))
    property_type = db.Column(db.String(80))    #rental or for sale
    description = db.Column(db.String(120))
    # image

    landlord_id = db.Column(db.Integer, db.ForeignKey('landlords.id'))
    landlord = db.relationship('LandLordModel')

    def __init__(self, title, location, property_type, description, landlord_id):
        self.title = title
        self.location = location
        self.property_type = property_type
        self.description = description
        self.landlord_id = landlord_id

    def __str__(self):
        return self.title
    
    @classmethod
    def find_by_title(self, title):
        return self.query.filter_by(title=title).first()
    
    @classmethod
    def find_by_landlord(self, landlord):
        return self.query.filter_by(landlord=landlord).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def json(self):
        return {'title':self.title, 'location':self.location, 'property_type':self.property_type, 'description':self.description}
    