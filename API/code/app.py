from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.club import Club, ClubList
from resources.player import PlayerList, Player

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'MFK'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) #creates new endpoint /auth


#class Player(Resource): 
#    def get(self, player_name, club_name):
#        global players
#        for player in players:
#            if player['name'] == player_name:
#                return player
#        return{'message': "Player '{}' not found".format(player_name)}, 404
#          
#    def post(self, club_name, player_name):
#        for club in clubs:
#            if club['club_name'] == club_name:
#                data = request.get_json()
#                player = {'name': player_name, 'position': data['position'], 'number': data['number'], 'club_name': data['club_name']}
#                if player not in players:
#                        players.append(player)
#                else:
#                    return {'Message': "Seems like '{}' already exists".format(player_name)}, 
#                return player, 201
#        
#    def delete(self, club_name, player_name):
#            global clubs
#            global players
#            players = next(filter(lambda x: x['name'] != player_name, players))
#            return {'message': "Player '{}' has been deleted".format(player_name)}, 200
#
#api.add_resource(Player, '/club/<string:club_name>/<string:player_name>') #http://127.0.0.1:5000/club/RealMadrid/AlvaroMorata

#class Players_list(Resource):
#        def get(self, club_name):
#            global players
#            for player in players:
#                return player
#
#api.add_resource(Players_list, '/club/<string:club_name>/my_players')
#
#
#class Trainings(Resource):
#  #@jwt_required()
#    def get(self):
#            return {'Training': trainings}
#api.add_resource(Trainings, '/training', '/trainings') #http://127.0.0.1:5000/training/
#
#class Training(Resource):
#    def get(self, training_name):
#        for training in trainings:
#            if training['training_name'] == training_name:
#                return training
#        return {'Training': None}, 404
#
#    def post(self, training_name):
#        data = request.get_json()
#        training = { 'training_name': training_name, 'reps': data['reps'], 'rest_between_reps': data['rest_between_reps'], 'date': data['date_of_training'] }
#        if training not in trainings:
#                    trainings.append(training)
#        else: 
#            return {'message': "Training {} already exists".format(training_name)}
#        return training
#
#    def delete(self, training_name):
#        global  trainings
#        trainings = list(filter(lambda x: x['training_name'] != training_name, trainings))
#        return {'message': "Training '{}' has been deleted".format(training_name)}, 200
#api.add_resource(Training, '/training/<string:training_name>') #http://127.0.0.1:5000/training/Ankle Mobility 4
#
#class Player_training_list(Resource):
#    def get(self, club_name, player_name, training_name):
#        for player_training in players_training_list:
#                 return [player_name, player_training]
#        else:
#            return {'message': "No training for '{}' consider adding one.".format(player_name)},404
#                
#    def post(self, club_name, player_name, training_name):
#        data = request.get_json()
#        player_training = { 'training_name': training_name, 'reps': data['reps'], 'rest_between_reps': data['rest_between_reps'], 'date': data['date_of_training'] }
#        if player_training not in players_training_list:
#            players_training_list.append(player_training)
#        else: 
#            return {'message': "Training {} already exists for this player".format(training_name)}
#        return player_training, 201
#
#    def delete(self, training_name, club_name, player_name):
#        global  players_training_list
#        players_training_list = list(filter(lambda x: x['training_name'] != training_name, players_training_list))
#        return {'message': "Training '{}' has been deleted".format(training_name)}, 200
#
#
#api.add_resource(Player_training_list, '/club/<string:club_name>/<string:player_name>/trainings/<string:training_name>') #http://127.0.0.1:5000/training/Ankle Mobility 4
#
#class Training_list(Resource): #This is defaul training list.
#    def get(self, club_name, player_name, training_name):
#        if training_name in players_training_list:
#            for training_name in players_training_list:
#                return {'player': player_name, 'training': training_name}
#
#    def post(self, club_name, player_name, training_name):
#        data = request.get_json()
#        players_training_list = { 'training_name': training_name, 'reps': data['reps'], 'rest_between_reps': data['rest_between_reps'], 'date': data['date_of_training'] }
#        if training_name not in players_training_list:
#                    players_training_list.append(training_name)
#        else: 
#            return {'message': "Training {} already exists".format(training_name)}
#        return players_training_list
#api.add_resource(Training_list, '/club/<string:club_name>/<string:player_name>/trainings/<string:training_name>')
#
#
#class List_training(Resource): #Returns a list of ALL trainings for the playera
#    def get(self, club_name, player_name):
#        for player in players:
#            return (player_name, players_training_list)


api.add_resource(Club, '/club/<string:club_name>')
api.add_resource(ClubList, '/clubs')
#api.add_resource(Player, '/player/<string:player_name>')
api.add_resource(Player, '/<string:club_name>/<string:player_name>')
api.add_resource(PlayerList, '/players')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from database import db
    db.init_app(app)
    app.run(port=5000, debug=True)