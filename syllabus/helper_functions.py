
from database import DB
from .models import Subject


def populate_subjects(program: dict) -> dict:
    """
    Populates with subject
    Args:
        program (dict): A program 
    Returns:
        dict: program populated with dict
    """

    semesters = {}
    for key, value in program['semesters'].items():
        semesters[key] = {}
        semesters[key]['subjects'] = [DB.find_one(
            Subject.collection, {'code': subject}) for subject in value['subjects']]
    program['semesters'] =semesters

    return program
