from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.player import PlayerModel
from models.club import ClubModel

class Player(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('club_name',
                       type=str,
                        required=True,
                        help="Every Player needs a Club."
                        )

    @jwt_required()
    def get(self, player_name, club_name):
        club = ClubModel.find_by_club_name(club_name)
        if club:
            return club.json()
        
        player = PlayerModel.find_by_player_name(player_name)
        if player:
            return player.json()
        return {'message': 'Player not found'}, 404

    def post(self, player_name, club_name):
        if ClubModel.find_by_club_name(club_name):
            if PlayerModel.find_by_player_name(player_name):
                return {'message': "A player with name '{}' already exists.".format(player_name)}, 400

        data = Player.parser.parse_args()

        player = PlayerModel( player_name, **data )

        try:
            player.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return player.json(), 201

    def delete(self, player_name):
        player = PlayerModel.find_by_player_name(player_name)
        if player:
            player.delete_from_db()
            return {'message': 'Player deleted.'}
        return {'message': 'Player not found.'}, 404

    def put(self, player_name):
        data = Player.parser.parse_args()

        player = PlayerModel.find_by_player_name(player_name)

        if player:
            player.price = data['price']
        else:
            player = PlayerModel(player_name, **data)

        player.save_to_db()

        return player.json()


class PlayerList(Resource):
    def get(self):
        return {'players': list(map(lambda x: x.json(), PlayerModel.query.all()))}