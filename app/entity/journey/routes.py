from flask import render_template, url_for,flash,redirect,request,abort,Blueprint
from app.Models import User,Bus,Journey,Location,Journey_client,Destiny
from app.entity.journey.forms import CreateForm,BookForm,destinyForm
from app import db,login_manager
from flask_login import login_user,current_user,logout_user,login_required
from sqlalchemy import or_, and_, distinct, func




journey =Blueprint('journey',__name__)






@journey.route('/insertbus',methods=['GET','POST'])
def bus():
    form=CreateForm()
    if form.validate_on_submit():
        buses=Bus(bus_name=form.Name.data)
        db.session.add(buses)
        db.session.commit()
        return redirect(url_for('journey.viewbus'))
    return render_template('bus.html',legend="login",form=form)

@journey.route('/viewbus')
def viewbus():
    bus=Bus.query.all()
    return render_template('viewbus.html',legend="login",bus=bus)
 
@journey.route('/viewlocation')
def viewlocation():
    loc=Location.query.all()
    return render_template('viewlocation.html',legend="login",loc=loc)

@journey.route('/viewdestiny')
def viewdestiny():
    des=Destiny.query.all()
    return render_template('viewdestiny.html',legend="login",des=des)

@journey.route('/insertlocation',methods=['GET','POST'])
def location():
    form=CreateForm()
    if form.validate_on_submit():
        buses=Location(location=form.Name.data)
        db.session.add(buses)
        db.session.commit()
        return redirect(url_for('journey.viewlocation'))
    return render_template('location.html',legend="login",form=form)

@journey.route('/insertdestiny',methods=['GET','POST'])#tofix
def destiny():
    form=destinyForm()
    if form.validate_on_submit():
        buses=Destiny(location_id=form.loc.data,start=form.start.data,end=form.end.data,fee=form.fee.data,bus_id=form.bus.data)
        db.session.add(buses)
        db.session.commit()
        db.session.add(Journey(destiny_id=buses.id))
        db.session.commit()
        return redirect(url_for('journey.viewdestiny'))
    return render_template('destiny.html',legend="login",form=form)


@journey.route('/bookjourney/<id>/',methods=['GET','POST'])
def bookjourney(id):
    form=BookForm()
    jo=Journey_client.query.filter(and_(Journey_client.id==id,Journey_client.user_id==current_user.id)).first()
    if jo:
        return redirect(url_for('users.dashboard'))
    if form.validate_on_submit():
        journ=Journey_client(journey_id=id,user_id=current_user.id,package=form.package.data)
        db.session.add(journ)
        jo=Journey.query.filter_by(id=id).first()
        jo.sits-=1 #check for the 30 mark
        db.session.commit()
        return redirect(url_for('users.dashboard'))
    return render_template('book.html',legend="login",form=form)

