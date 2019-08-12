from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name

class Account(db.Model):
    '''The model used for capuring the first name, last name,
       nickname, and email.'''
       
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True)

    def __init__(self, first_name, last_name, nickname, email):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.email = email

    def __repr__(self):
        return '<Account %r>' % self.first_name
