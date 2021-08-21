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
        image:str = "sample.jpg",

    ):
        self.code = code
        self.name = name
        self.image = image
        self.programs = programs


    def save(self):
        return DB.insert_one(self.collection, data=self.json())

    def json(self):
        return {
        'code' :self.code,
        'name' :self.name,
        'programs' :self.programs,
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
        image:str,
        description:str,
        semesters: dict,

    ):
        self.code = code
        self.name = name
        self.image = image

        self.description = description
        self.semesters = semesters


    def save(self):
        return DB.insert_one(self.collection, data=self.json())

    def json(self):
        return {
        'code' :self.code,
        'name' :self.name,
        'image':self.image,
        'description' :self.description,
        'semesters' :self.semesters,
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

    def __init__(
        self,
        code: str,
        name: str,
        level:str,
        filename:str,
        

    ):
        self.code = code
        self.name = name
        self.level =level
        self.filename = filename


    def save(self):
        return DB.insert_one(self.collection, data=self.json())

    def json(self):
        return {
        'code' :self.code,
        'level':self.level,
        'name' :self.name,
        'filename' :self.filename,
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
        programId:str,
       
        

    ):
        self.text = text
        self.subjectId = subjectId
        self.programId =programId


    def save(self):
        return DB.insert_one(self.collection, data=self.json())

    def json(self):
        return {
        'text': self.text ,
        'subjectId': self.subjectId,
        'programId' :self.programId
        }
