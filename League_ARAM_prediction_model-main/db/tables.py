from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class poke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    champ_name = db.Column(db.String(255), nullable=False)
    Q = db.Column(db.Integer, nullable=True)
    W = db.Column(db.Integer, nullable=True)
    E = db.Column(db.Integer, nullable=True)
    R = db.Column(db.Integer, nullable=True)
    Total = db.Column(db.Integer, nullable=True)
    hard_CC = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Poke {self.name}>'

class champinfo(db.Model):
    champ_key = db.Column(db.Integer, primary_key=True)
    champ_name = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    difficulty = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String(255), nullable=False)
    champ_class = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<ChampInfo {self.name}>'

class aram_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gameId = db.Column(db.String(255), nullable=False)
    gameResult = db.Column(db.String(10), nullable=False)
    
    puuid_p1 = db.Column(db.String(255), nullable=False)
    level_p1 = db.Column(db.Integer, nullable=False)
    champ_name_p1 = db.Column(db.String(255), nullable=False)
    champ_id_p1 = db.Column(db.Integer, nullable=False)
    
    puuid_p2 = db.Column(db.String(255), nullable=False)
    level_p2 = db.Column(db.Integer, nullable=False)
    champ_name_p2 = db.Column(db.String(255), nullable=False)
    champ_id_p2 = db.Column(db.Integer, nullable=False)
    
    puuid_p3 = db.Column(db.String(255), nullable=False)
    level_p3 = db.Column(db.Integer, nullable=False)
    champ_name_p3 = db.Column(db.String(255), nullable=False)
    champ_id_p3 = db.Column(db.Integer, nullable=False)
    
    puuid_p4 = db.Column(db.String(255), nullable=False)
    level_p4 = db.Column(db.Integer, nullable=False)
    champ_name_p4 = db.Column(db.String(255), nullable=False)
    champ_id_p4 = db.Column(db.Integer, nullable=False)
    
    puuid_p5 = db.Column(db.String(255), nullable=False)
    level_p5 = db.Column(db.Integer, nullable=False)
    champ_name_p5 = db.Column(db.String(255), nullable=False)
    champ_id_p5 = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<aramData {self.name}>'
