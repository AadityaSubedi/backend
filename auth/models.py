from database import DB


class User:
    
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
        username: str,
        email: str,
        password: str,

    ):
        self.username = username
        self.email = email

        self.password = password


    def save(self):
        return DB.insert_one(self.collection, data=self.json())

    def json(self):
        return {
        'username' :self.username,
        'email' :self.email,
        'password' :self.password,
        }




