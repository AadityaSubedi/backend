from flask_restful import Resource
from . import user_api
from flask import Flask, request


@user_api.resource("/login")
class OneProgram(Resource):
    def get(self):

        
        # return the command line output as the reesponse
        return { 'data' : "happy coding"}
