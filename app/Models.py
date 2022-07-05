from flask import current_app
from itsdangerous import  TimedJSONWebSignatureSerializer as Serializer
import jwt, uuid, os
from datetime import datetime
from app import db,login_manager
from flask_login import UserMixin
from sqlalchemy import ForeignKeyConstraint,ForeignKey,UniqueConstraint
from sqlalchemy.dialects.mysql import TIME

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
   # image_file =db.Column(db.String(20),nullable=False,default='Billgates.jpg')
    password = db.Column(db.String(60),nullable=False)
    Type=db.Column(db.String)
    

    def get_reset_token(self,expire_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'],expire_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')
        
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token) ['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
         return '<User %r>' %self.id

class Journey_client(db.Model):
    __tablename__ = 'Journey_client'

    id = db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer, ForeignKey('user.id'))
    journey_id=db.Column(db.Integer, ForeignKey('Journey.id'))
    package=db.Column(db.String)
    

    def __repr__(self):
        return '<Journey_client %r>' %self.id


class Bus(db.Model):
    __tablename__ = 'Bus'

    id = db.Column(db.Integer,primary_key=True)
    bus_name=db.Column(db.String)

    def __repr__(self):
        return '<Bus %r>' %self.id


class Location(db.Model):
    __tablename__ = 'Location'

    id = db.Column(db.Integer,primary_key=True)
    location=db.Column(db.String)

    def __repr__(self):
        return '<Location %r>' %self.id

class Impression(db.Model):
    __tablename__ = 'Impression'

    id = db.Column(db.Integer,primary_key=True)
    impression=db.Column(db.String)
    count=db.Column(db.Integer,default=0)

    def __repr__(self):
        return '<Impression %r>' %self.id

class Suggestion(db.Model):
    __tablename__ = 'Suggestion'

    id = db.Column(db.Integer,primary_key=True)
    immpression_id=db.Column(db.Integer,ForeignKey('Impression.id'))
    suggestions=db.Column(db.String)
    count=db.Column(db.Integer,default=1)

    def __repr__(self):
        return '<Suggestion %r>' %self.id


class Destiny(db.Model):
    __tablename__ = 'Destiny'

    id = db.Column(db.Integer,primary_key=True)
    location_id=db.Column(db.Integer,ForeignKey('Location.id'))
    bus_id=db.Column(db.Integer, ForeignKey('Bus.id'))
    start=db.Column(db.TIME())
    end=db.Column(db.TIME())
    fee=db.Column(db.Integer)

    def __repr__(self):
        return '<Destiny %r>' %self.id


class Journey(db.Model):
    __tablename__ = 'Journey'

    id = db.Column(db.Integer,primary_key=True)
    destiny_id=db.Column(db.Integer, ForeignKey('Destiny.id'))
    destiny__=db.relationship("Destiny", 
            primaryjoin=(destiny_id == Destiny.id),
            backref=db.backref('client__nego',  uselist=False),  uselist=False)
    status=db.Column(db.Boolean,default=False)
    sits=db.Column(db.Integer,default=30)

    def __repr__(self):
        return '<Journey %r>' %self.id




