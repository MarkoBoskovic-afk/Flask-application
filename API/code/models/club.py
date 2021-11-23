from database import db
from models.player import PlayerModel

class ClubModel(db.Model):
    __tablename__ = 'clubs'

    id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String(80))

    player = db.relationship('PlayerModel', lazy='dynamic')

    def __init__(self, club_name):
        self.club_name = club_name

    def json(self):
        return {'club_name': self.club_name, 'players': [player.json() for player in self.player.all()]}

    @classmethod
    def find_by_club_name(cls, club_name):
        return cls.query.filter_by(club_name=club_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()