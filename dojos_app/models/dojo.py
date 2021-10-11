from dojos_app.config.mysqlconnection import connectToMySQL
from dojos_app.models import ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Index page
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    #New dojo   
    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at ) VALUES ( %(name)s , NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
    
    #Display dojo users
    @classmethod
    def Display_Data(cls, id):
        query = "SELECT * FROM ninjas WHERE dojo_id=%(id)s;"
        data={
            "id": id
        }
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results

    #Display one dojo
    @classmethod
    def Display_Dojo(cls, id):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        data={
            "id": id
        }
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results
    



