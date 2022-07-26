import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Projects(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    tags = db.Column(db.String(50))
    hourly_rate = db.Column(db.String(7))
