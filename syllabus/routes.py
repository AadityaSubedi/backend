from bson.objectid import ObjectId
from flask_restful import Resource
from . import syllabus_api
from flask import Flask, request


from json import loads
from bson.json_util import dumps
from utils import helper_functions as hf
from utils import file_helper_functions as fhf
from . import helper_functions as shf

from database import DB

from .programs import program
from .levels import levels
from .subject import subject
from .models import Level, Subject
from .models import Program
from syllabus import programs


@syllabus_api.resource("/program/<string:id>")
class OneProgram(Resource):
    def get(self,id):
        try:

            # program = DB.find_one(Program.collection, {'_id':ObjectId(id)})
            program = DB.find_one(Program.collection, {'code':str.upper(id)})


            # populate the subject field
            program = shf.populate_subjects(program) 


            return (hf.success(
                    "program fetch",
                    "program fetched succesfully",
                    loads(dumps(program))
                    # loads(dumps(a))

                    ),
                    200
                    )

        except Exception as e:
            return (hf.failure(

                    "program fetch",
                    str(e),
                    ),
                    500
                    )


@syllabus_api.resource("/programs")
class Programs(Resource):
    def post(self):
        try:
            inputData = {
                'code': request.form.get('code'),
                'name': request.form.get('name'),
                'description': request.form.get('description'),
                'semesters': loads(request.form.get('semesters'))
                # 'semesters':{ '1':[],
                #               '2':[]
                #               '3':[]
                # }

            }

            file = request.files['file']
            # handle file upload
            filename = fhf.save_image(file)

# check's the validiity of code here hai

            program = Program(
                code=inputData["code"], name=inputData["name"], image=filename, description=inputData["description"], semesters=inputData["semesters"])
            inserted_program = program.save()

            # return the command line output as the response
            return (hf.success(
                    "program insertion",
                    "program inserted succesfully",

                    ),
                    200
                    )

        except Exception as e:
            return (hf.failure(

                    "subject insertion",
                    str(e),
                    ),
                    500
                    )

    def get(self):
        try:

            programs = DB.find_many("programs", {})
            # return the command line output as the response

            return (hf.success(
                    "program fetch",
                    "program fetched succesfully",
                    loads(dumps(programs))
                    # loads(dumps(a))

                    ),
                    200
                    )

        except Exception as e:
            return (hf.failure(

                    "subject insertion",
                    str(e),
                    ),
                    500
                    )


@syllabus_api.resource("/levels")
class Levels(Resource):
    def put(self):
        try:

            inputData = {
                'code': request.form.get('code'),
                'name': request.form.get('name'),
                'programs': request.form.get('programs'),

            }
            # inputData = request.get_json()
            print(request.files)
            file = request.files['file']
            # handle file upload
            if file:
                filename = fhf.save_image(file)
            level = Level(
                code=inputData["code"], name=inputData["name"], programs=inputData["programs"], image=str(filename))
            inserted_level = level.save()

            # return the command line output as the response

            return (hf.success(
                    "level insertion",
                    "level inserted succesfully",

                    ),
                    200
                    )

        except Exception as e:
            return (hf.failure(

                    "level insertion",
                    str(e),
                    ),
                    500
                    )



    def post(self):
        try:

            inputData = {
                'code': "sample code",
                'name': "sample name",
                'programs': ["BCT", "BCE"],

            }
            # inputData = request.get_json()
            # print(request.files)
            # file = request.files['file']
            # handle file upload
            # if file:
                # filename = fhf.save_image(file)
            level = Level(
                code=inputData["code"], name=inputData["name"], programs=inputData["programs"])
            inserted_level = level.save()

            # return the command line output as the response

            return (hf.success(
                    "level insertion",
                    "level inserted succesfully",

                    ),
                    200
                    )

        except Exception as e:
            return (hf.failure(

                    "level insertion",
                    str(e),
                    ),
                    500
                    )

    def get(self):
        try:

            levels = DB.find_many("levels", {})

            return (hf.success(
                    "level fetch",
                    "level fetched succesfully",
                    loads(dumps(levels))
                    # loads(dumps(a))

                    ),
                    200
                    )

        except Exception as e:
            return (hf.failure(

                    "level fetch",
                    str(e),
                    ),
                    500
                    )



@syllabus_api.resource("/level/<string:id>")
class OneLevel(Resource):
    def delete(self,id):
        try:


            print("meeeeeeeeeeeeeee")
            _ = DB.delete_one(Level.collection, {'_id':ObjectId(id)})



            return (hf.success(
                    "level deletion",
                    "level deleted succesfully",

                    ),
                    200
                    )

        except Exception as e:
            return (hf.failure(

                    "level deletion",
                    str(e),
                    ),
                    500
                    )






@syllabus_api.resource("/subject/<string:code>")
class OneSubject(Resource):
    def get(self, code):

        # return the command line output as the reesponse
        return {'data': subject}


@syllabus_api.resource("/subjects")
class Subjects(Resource):
    def post(self):
        try:
            inputData = {
                'code': request.form.get('code'),
                'name': request.form.get('name'),
                'level': request.form.get('level'),

            }
            file = request.files['file']
            # handle file upload
            filename = fhf.save_pdf(file)
            subject = Subject(
                code=inputData["code"], name=inputData["name"], level=inputData["level"], filename=str(filename))
            inserted_subject = subject.save()

            # return the command line output as the response
            return (hf.success(
                    "subject insertion",
                    "subject inserted succesfully",

                    ),
                    200
                    )

        except Exception as e:
            return (hf.failure(

                    "subject insertion",
                    str(e),
                    ),
                    500
                    )

    def get(self):
        try:

            subjects = DB.find_many("subjects", {})

            return (hf.success(
                    "subjects fetch",
                    "subjects fetched succesfully",
                    loads(dumps(subjects))
                    # loads(dumps(a))

                    ),
                    200
                    )

        except Exception as e:
            return (hf.failure(

                    "subjects fetch",
                    str(e),
                    ),
                    500
                    )


@syllabus_api.resource("/comments")
class Comments(Resource):
    def post(self):

        # return the command line output as the response
        return {'data': subject}
