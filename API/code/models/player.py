from database import db


class PlayerModel(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    club_name = db.Column(db.Integer, db.ForeignKey('clubs.club_name'))
    club = db.relationship('ClubModel')

    def __init__(self, player_name, price, club_name):
        self.player_name = player_name
        self.price = price
        self.club_name = club_name

    def json(self):
        return {'name': self.player_name, 'price': self.price}

    @classmethod
    def find_by_player_name(cls, player_name):
        return cls.query.filter_by(player_name=player_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()