from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField ,IntegerField#, TextAreaField
from wtforms.validators import DataRequired,length,Email,EqualTo,ValidationError
from app.Models import User
from wtforms.fields.html5 import DateField
from wtforms_components import TimeField





class CreateForm(FlaskForm):
    Name =StringField('Name')                           
    submit = SubmitField('Submit')


class destinyForm(FlaskForm):
    loc =IntegerField('location_id')   
    fee =IntegerField('Fee')    
    bus =IntegerField('BUS_Id') 
    start =TimeField('Start')  	
    end=TimeField('End')            

    submit = SubmitField('Submit')


class BookForm(FlaskForm):    
    package =StringField('package')            

    submit = SubmitField('Book')