from flask_restful import Resource
from models.club import ClubModel


class Club(Resource):
    def get(self, club_name):
        club = ClubModel.find_by_club_name(club_name)
        if club:
            return club.json()
        return {'message': 'Club not found'}, 404

    def post(self, club_name):
        if ClubModel.find_by_club_name(club_name):
            return {'message': "A club with name '{}' already exists.".format(club_name)}, 400

        club = ClubModel(club_name)
        try:
            club.save_to_db()
        except:
            return {"message": "An error occurred creating a club."}, 500

        return club.json(), 201

    def delete(self, club_name):
        club = ClubModel.find_by_club_name(club_name)
        if club:
            club.delete_from_db()

        return {'message': 'Club deleted'}


class ClubList(Resource):
    def get(self):
        return {'Clubs': list(map(lambda x: x.json(), ClubModel.query.all()))}