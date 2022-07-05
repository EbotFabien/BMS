from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField#, TextAreaField
from wtforms.validators import DataRequired,length,Email,EqualTo,ValidationError
from app.Models import User





class CreateForm(FlaskForm):
    imp=SelectField('impressions',
                             choices=[(1,'Late Departure'), (2,'Very Good'),(3,'Very Poor'),(4,'disrespecful')])    
    sug =StringField('Suggestions')                       
    submit = SubmitField('Submit')



 