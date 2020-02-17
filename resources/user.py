from flask_restful import Resource, reqparse
from models.user import UserModel
from db import db


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):

            return {"message": "User with that username already exists."}, 400
        # argument unpacking, translated as data['username'], data['password']
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

    # returns all the users from users table
    def get(self):
        users = []
        userList = db.session.query(UserModel).all()
        for user in userList:
            users.append(user.json())
        return {"users": users}
