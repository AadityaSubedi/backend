from flask import Flask,Blueprint, send_from_directory
from syllabus import syllabus_bp
from flask_restful import Resource,Api  
from flask_cors import CORS
from auth import user_bp
UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.register_blueprint(syllabus_bp)
app.register_blueprint(user_bp)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/images/<string:imagename>')
def download_file(imagename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               'images/'+imagename)



CORS(app) # This will enable CORS for all routes

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