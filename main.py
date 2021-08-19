from flask import Flask, Blueprint, send_from_directory
from flask_jwt_extended import jwt_manager, JWTManager
from syllabus import syllabus_bp
from flask_restful import Resource, Api
from flask_cors import CORS
from auth import user_bp
UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.register_blueprint(syllabus_bp)
app.register_blueprint(user_bp)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JWT_SECRET_KEY'] = 'will_edit_this_secret_key'


@app.route('/images/<string:imagename>')
def download_file(imagename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               'images/'+imagename)


jwt = JWTManager(app)


@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    print("----------------------------------")
    return {
        'data1': 'happy coding ',
        'data2': 'happy coding 2'
    }


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(decrypted_token):
    return decrypted_token['jti'] in {"blocklist"}
    #  modify this as per the need later


CORS(app)  # This will enable CORS for all routes


if __name__ == "__main__":
    app.run()


# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Hello Puppy!</h1>'

# @app.route('/information')
# def info():
#     return '<h1>Puppies are cute!</h1>'

# if __name__ == '__main__':
#     app.run()
