from models.property import PropertyModel
from flask_restful import Resource, reqparse


class Properti(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('location',
        type=str,
        required=True,
        help='That field cannot be left empty'
    )
    parser.add_argument('property_type',
        type=str,
        required=True,
        help='That field cannot be left empty'
    )
    parser.add_argument('description',
        type=str,
        required=True,
        help='That field cannot be left empty'
    )
    parser.add_argument('landlord_id',
        type=int,
        required=True,
        help='That field cannot be left empty'
    )


    def get(self, title):
        properti = PropertyModel.find_by_title(title)
        if properti:
            return properti.json()
        return {'message':'The property you are looking for does not exist'}, 404
    
    def post(self, title):
        if PropertyModel.find_by_title(title):
            return {'message':'a property by that title doe not exist'}
        data = self.parser.parse_args()
        new_property = PropertyModel(title, **data)
        new_property.save_to_db()

        return new_property.json()

    def delete(self, title):
        properti = PropertyModel.find_by_title(title)
        if properti:
            properti.delete_from_db()
            return {'message':'property successfully deleted'}
        return {'message':'property doesnot exists'}, 404

    def put(self, title):
        data = self.parser.parse_args()
        my_property = PropertyModel.find_by_title(title)
        if my_property:
            my_property.location = data['location']
            my_property.property_type = data['property_type']
            my_property.description = data['description']
            my_property.landlord_id = data['landlord_id']
            my_property.save_to_db()
            return my_property.json()
        my_property = PropertyModel(title, **data)
        my_property.save_to_db()

        return my_property.json()


class PropertyList(Resource):
    def get(self):
        return {'properties':[item.json() for item in PropertyModel.query.all()]}