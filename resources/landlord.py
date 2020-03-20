from flask import request
from models.landlord import LandLordModel
from flask_restful import Resource, reqparse



class LandLord(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name',
        type=str,
        required=True,
        help='That field cannot be left blank'
    )
    parser.add_argument('email',
        type=str,
        required=True,
        help='That field cannot be left blank'
    )
    parser.add_argument('last_name',
        type=str,
        required=True,
        help='That field cannot be left blank'
    )
    parser.add_argument('phone',
        type=int,
        required=True,
        help='That field cannot be left blank'
    )
    
    def get(self, username):
        data = self.parser.parse_args()
        landlord = LandLordModel.find_by_username(username)
        if landlord:
            return landlord.json()
        return {'message':'that landlord does not exist'}, 404
    def post(self, username):
        data = self.parser.parse_args()
        if LandLordModel.find_by_username(username):
            return {'message':'that landlord already exist'}, 400
        landlord = LandLordModel(username, **data)
        landlord.save_to_db()

        return landlord.json()
    
    def delete(self, username):
        data = self.parser.parse_args()
        if LandLordModel.find_by_username(username):
            LandLord.delete_from_db()
            return {'message':'landlord successfully deleted'}
        return {'message':'that landlord does not exist'}, 404
    

class LandLordList(Resource):
    def get(self):
        return {'Landlords':[landlord.json() for landlord in LandLordModel.query.all()]}