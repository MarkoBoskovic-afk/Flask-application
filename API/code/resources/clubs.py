import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
#USED TO GET ALL CLUBS
class Clubs(Resource):
    parser = reqparse.RequestParser()

    def get(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM clubs"
        result = cursor.execute(query)
        row = result.fetchone()
        connection.close()
        if row:
            return {'clubs': {'club name': row[0]}}
        return {"message": "Sorry, I couldn't find any of the clubs yet."}