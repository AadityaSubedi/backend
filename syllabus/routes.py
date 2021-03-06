from bson.objectid import ObjectId
from flask_restful import Resource
from . import syllabus_api
from flask import Flask, request
from datetime import datetime


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


@syllabus_api.resource("/program/<string:id>")
class OneProgram(Resource):
    def get(self, id):
        try:

            # program = DB.find_one(Program.collection, {'_id':ObjectId(id)})
            program = DB.find_one(Program.collection, {'code': str.upper(id)})

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

    def put(self, id):
        try:

            data = request.form

            data = {**data, 'semesters': loads(data['semesters'])}
            # print("me")
            file = request.files.get('file')
            # handle file upload
            if file:
                filename = fhf.save_image(file)
                data['image'] = filename

            # image xa vane xuttai handle garne hai

            oldProgram = DB.find_one_and_update(
                Program.collection, {'_id': ObjectId(id)}, data)

            # update the level with new program code
            if data['level'] and data["code"] != oldProgram["code"]:
                DB.update_one(
                    Level.collection, {'code': data['level']}, {
                        'programs': data["code"]}, "$push")
                DB.update_one(
                    Level.collection, {'code': data['level']}, {
                        'programs': oldProgram["code"]}, "$pull")

                # DB.update_one(Level.collection, {"code": inputData["level"]}, {
                #               'programs': inputData["code"]}, "$push")

            if file:
                fhf.remove_image(oldProgram['image'])

            return (hf.success(
                    "level update",
                    "level update succesfully",

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


@syllabus_api.resource("/programs")
class Programs(Resource):
    def post(self):
        try:
            inputData = {
                'code': "CODE",
                'name': "sampleName",
                'description': "Description",
                'semesters': {'1': {"subjects": []}, '2': {"subjects": []}},
                'level': request.get_json().get('levelCode')


            }

            # file = request.files['file']
            # handle file upload
            # filename = fhf.save_image(file)

# check's the validiity of code here hai

            program = Program(
                code=inputData["code"], name=inputData["name"], description=inputData["description"], level=inputData["level"], semesters=inputData["semesters"],)  # image=filename)
            inserted_program = program.save()

            # if level exist, update the current level ,
            if inputData["level"]:
                DB.update_one(Level.collection, {"code": inputData["level"]}, {
                              'programs': inputData["code"]}, "$push")

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
    def sample(self):
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
                'code': "SAMPLE CODE",
                'name': "sample name",
                'programs': [],

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
    def delete(self, id):
        try:

            # print("meeeeeeeeeeeeeee")
            _ = DB.delete_one(Level.collection, {'_id': ObjectId(id)})
            # _ = DB.delete_one(Level.collection, {'code':str.upper(id)})

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

    def get(self, id):
        try:

            # program = DB.find_one(Program.collection, {'_id':ObjectId(id)})
            level = DB.find_one(Level.collection, {'code': str.upper(id)})

            # populate the subject field
            level = shf.populate_programs(level)

            return (hf.success(
                    "program fetch",
                    "program fetched succesfully",
                    loads(dumps(level))
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

    def put(self, id):
        try:

            data = request.form
            data = {**data, 'programs': loads(data['programs'])}
            # print(data)

            # print("me")
            file = request.files.get('file')
            # handle file upload
            if file:
                filename = fhf.save_image(file)
                data['image'] = filename

            # image xa vane xuttai handle garne hai

            oldLevel = DB.find_one_and_update(
                Level.collection, {'_id': ObjectId(id)}, data)

            if file:
                fhf.remove_image(oldLevel['image'])

            return (hf.success(
                    "level update",
                    "level update succesfully",

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


@syllabus_api.resource("/subject/<string:id>")
class OneSubject(Resource):

    def get(self, id):
        try:

            # program = DB.find_one(Program.collection, {'_id':ObjectId(id)})
            subject = DB.find_one(Subject.collection, {'code': str.upper(id)})

            return (hf.success(
                    "program fetch",
                    "program fetched succesfully",
                    loads(dumps(subject))
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

    def delete(self, id):
        try:

            # print("meeeeeeeeeeeeeee")
            _ = DB.find_one_and_delete(
                Subject.collection, {'_id': ObjectId(id)})
            # _ = DB.delete_one(Level.collection, {'code':str.upper(id)})

# db.inventory.find( { tags: "red" } )
#
            # _ = DB.update_one(Program.collection,{'subjects':_["code"]},{})

            # write the python script to iterate over all the programs, and remove this
            # deleted subject searching over each semesters of each programs, (this is very tedious)

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

    def put(self, id):
        # try:

        data = request.form

        # updatedSubject = {'name': data["name"],
        # 'code': data["code"],
        # }
        # print("me")

        print(data)
        file = request.files.get('file')
        # handle file upload
        filename = None
        if file:
            filename = fhf.save_pdf(file)

        newSyllabus = {
            'theory': 100,
            'practical': 50,
            'teaching': 12,
            # 'batch': datetime.now().year,
            'remarks': data['remarks'],
            'filename': filename
        }
        revised = loads(data['revised'].lower())
        if revised:
            newSyllabus["batch"] = datetime.now().year
            # {
            #     'theory': 100,
            #     'practical': 50,
            #     'teaching': 12,
            #     'batch': datetime.now().year,
            #     'remarks': data['remarks'],
            #     'filename': filename
            # }
            actionData = {"$set": {"name": data["name"], "code": data["code"]}, "$push": {
                "syllabus": newSyllabus}}
            print("ffffffk")
            _ = DB.update_one_multiple_actions(
                Subject.collection, {'_id': ObjectId(id)}, actionData)
        else:
            print("else partttttttttttttttttttttttttttttttttttttttt")
            newSyllabus["batch"] = int(data["batch"])
            actionData = {"$set": {"name": data["name"], "code": data["code"]}, "$pull": {
                "syllabus": {"batch": newSyllabus["batch"]}}}
            _ = DB.update_one_multiple_actions(
                Subject.collection, {'_id': ObjectId(id)}, actionData)
            print(_)
            _ = DB.update_one(
                Subject.collection, {'_id': ObjectId(id)}, {"syllabus": newSyllabus}, "$push")

            # { $pull: { results: { answers: { $elemMatch: { q: 2, a: { $gte: 8 } } } } } },

        return (hf.success(
                "level update",
                "level update succesfully",

                ),
                200
                )

        # except Exception as e:
        return (hf.failure(

                "level deletion",
                str(e),
                ),
                500
                )


@syllabus_api.resource("/subjects")
class Subjects(Resource):
    def post(self):
        try:

            # print("a")
            subject = Subject()
            _ = subject.save()

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

    def put(self, id):
        try:

            data = request.form

            data = {**data, 'semesters': loads(data['semesters'])}
            # print("me")
            file = request.files.get('file')
            # handle file upload
            if file:
                filename = fhf.save_image(file)
                data['image'] = filename

            # image xa vane xuttai handle garne hai

            oldProgram = DB.find_one_and_update(
                Program.collection, {'_id': ObjectId(id)}, data)

            # update the level with new program code
            if data['level'] and data["code"] != oldProgram["code"]:
                DB.update_one(
                    Level.collection, {'code': data['level']}, {
                        'programs': data["code"]}, "$push")
                DB.update_one(
                    Level.collection, {'code': data['level']}, {
                        'programs': oldProgram["code"]}, "$pull")

                # DB.update_one(Level.collection, {"code": inputData["level"]}, {
                #               'programs': inputData["code"]}, "$push")

            if file:
                fhf.remove_image(oldProgram['image'])

            return (hf.success(
                    "level update",
                    "level update succesfully",

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
    def get(self):

        # return the command line output as the response
        return {'data': None}


@syllabus_api.resource("/search/<string:searchBy>/<string:searchOn>")
class Search(Resource):
    def get(self, searchBy, searchOn):
        try:

            # program = DB.find_one(Program.collection, {'_id':ObjectId(id)})

            program = DB.find_many(Subject.collection, {searchBy: {
                                   "$regex": searchOn, "$options": "i"}})

            return (hf.success(
                    "search fetch",
                    "search fetched succesfully",
                    loads(dumps(program))
                    ),
                    200
                    )

        except Exception as e:
            return (hf.failure(
                    "search fetch",
                    str(e),
                    ),
                    500
                    )
