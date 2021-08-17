from auth.models import User
from flask_restful import Resource
from . import user_api
from flask import Flask, request
from .models import User
from database import DB

from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token



from utils import helper_functions as hf
from utils import file_helper_functions as fhf


@user_api.resource("/register")
class RegisterUsers(Resource):
    def post(self):
        try:
            inputData = {
                'username': request.form.get('username'),
                'email': request.form.get('email'),
                'password': request.form.get('password'),

            }

            file = request.files['file']
            # handle file upload
            filename = fhf.save_image(file)

            user = User(
                username=inputData['username'], email=inputData['email'], password=inputData['password'], image=filename)
            registered_user = user.save()

            # return the command line output as the response
            return (hf.success(
                    "user registration",
                    "user registered succesfully",

                    ),
                    200
                    )

        except Exception as e:
            return (hf.failure(

                    "user registration",
                    str(e),
                    ),
                    500
                    )


@user_api.resource("/login")
class LoginUser(Resource):
    def post(self):
        try:
            inputData = {
                'username': request.form.get('username'),
                'password': request.form.get('password'),

            }

            user = DB.find_one(User.collection, {
                               'username': inputData['username']})

            assert user, "Invalid credentials"

            token = {}
            if user and safe_str_cmp(user['password'], inputData['password']):
                token['access_token'] = create_access_token(
                    identity=user['username'], fresh=True)
                token['refresh_token'] = create_refresh_token(
                    identity=user['username'])
            # return the command line output as the response
            return (hf.success(
                    "user login",
                    "user logged in succesfully",
                    token
                    ),
                    200
                    )

        except Exception as e:
            return (hf.failure(

                    "user login",
                    str(e),
                    ),
                    401
                    )
