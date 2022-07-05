from flask import render_template, url_for,flash,redirect,request,abort,Blueprint
from app.entity.ml.forms import CreateForm
from app.Models import User,Suggestion,Journey,Impression
from flask_login import login_user,current_user,logout_user,login_required
from app import bcrypt,db
from datetime import date,timedelta,datetime,timezone 
import random
from sqlalchemy import or_, and_, desc,asc
from werkzeug.utils import secure_filename
from flask import  url_for,current_app
import os
from app.entity.ml.utils import  mla





ml =Blueprint('ml',__name__)


#create a list of imps
@ml.route('/insertsuggestion',methods=['GET','POST'])
def suggestion():
    mlv=None
    form=CreateForm()
    sug=Suggestion.query.all()
    
    if form.validate_on_submit():
        for i in sug:
            mlv=mla(form.sug.data,i.suggestions)
            if mlv == True:
        
                if int(form.imp.data)== int(i.immpression_id):
                    
                    imp=Impression.query.filter_by(id=form.imp.data).first()
                    imp.count+=1
                    db.session.commit()
                    i.count+=1
                    db.session.commit()
                    break
        if mlv != True:
            buses=Suggestion(immpression_id=form.imp.data,suggestions=form.sug.data)
            db.session.add(buses)
            imp=Impression.query.filter_by(id=form.imp.data).first()
            imp.count+=1
            db.session.commit()
        if current_user.Type =='admin':
            return redirect(url_for('ml.viewimpression'))#suggestion sent message
        else:
            return redirect(url_for('users.dashboard'))
    return render_template('impression.html',legend="login",form=form)


@ml.route('/viewimpression')
def viewimpression():
    imp=Impression.query.all()
    return render_template('viewimp.html',legend="login",loc=imp)


@ml.route('/viewsuggestion/<id>/')
def viewsuggestion(id):
    sug=Suggestion.query.all()
    return render_template('viewsug.html',legend="login",imp=sug)




#view impressions
#view suggestions
#suggestions have count if they are added on