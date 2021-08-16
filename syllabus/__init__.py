from flask import Blueprint
from flask_restful import Api

syllabus_bp = Blueprint("syllabus", __name__, url_prefix="/api")
syllabus_api = Api(syllabus_bp)

from . import routes
