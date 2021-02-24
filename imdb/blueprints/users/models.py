from imdb.extensions import db


class Logs(db.Model):
    __tablename__='logs'

    date=db.Column(db.Date, primary_key=True)
    top500=db.relationship("Top500")
    
class Top500(db.Model):
    __tablename__='top500episodes'
    
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100))
    rank=db.Column(db.Integer)
    episode=db.Column(db.String(100))
    date=db.Column(db.Date, db.ForeignKey('logs.date'))



