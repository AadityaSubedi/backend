from datetime import datetime
from typing import List

from bson.objectid import ObjectId
from database import DB


class Level:

    """
    {
        code: str, level code
        name: str, level name
        programs: List[ObjectId], list of programs

    }
    """

    collection = "levels"

    def __init__(
        self,
        code: str,
        name: str,
        programs: List[ObjectId],
        image: str = "sample.jpg",

    ):
        self.code = code
        self.name = name
        self.image = image
        self.programs = programs

    def save(self):
        return DB.insert_one(self.collection, data=self.json())

    def json(self):
        return {
            'code': self.code,
            'name': self.name,
            'programs': self.programs,
            'image': self.image
        }


class Program:

    """
    {
        code: str, level code
        name: str, level name
        semseter:{
            <semester number>:{
                List[ObjectId of Subject]
            }
        }

    }
    """

    collection = "programs"

    def __init__(
        self,
        code: str,
        name: str,
        description: str,
        semesters: dict,
        level: str = None,
        image: str = "sample.jpg",

    ):
        self.code = code
        self.name = name
        self.level = level
        self.image = image

        self.description = description
        self.semesters = semesters

    def save(self):
        return DB.insert_one(self.collection, data=self.json())

    def json(self):
        return {
            'code': self.code,
            'name': self.name,
            'level': self.level,
            'image': self.image,
            'description': self.description,
            'semesters': self.semesters,
        }


class Subject:

    """
    {
        name: str, level code
        name: str, level name
        semseter:{
            <semester number>:{
                List[ObjectId of Subject]
            }
        }

    }
    """

    collection = "subjects"

    def __init__(self):

        pass

    def save(self):
        return DB.insert_one(self.collection, data=self.json())

    #    gd496163-a123-4a50-b05d-415d0e72c0c1

    def json(self):
        print("json")
        return {
            'code': "CODE",
            'name': "subjectName",
            'syllabus': []
        }


class Comment:

    """
    {
        name: str, level code
        name: str, level name
        semseter:{
            <semester number>:{
                List[ObjectId of Subject]
            }
        }

    }
    """

    collection = "comments"

    def __init__(
        self,
        text: str,
        subjectId: str,
        programId: str,

    ):
        self.text = text
        self.subjectId = subjectId
        self.programId = programId

    def save(self):
        return DB.insert_one(self.collection, data=self.json())

    def json(self):
        return {
            'text': self.text,
            'subjectId': self.subjectId,
            'programId': self.programId
        }
