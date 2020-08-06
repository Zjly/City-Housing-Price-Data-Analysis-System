from flask import Blueprint
from decorators import login_required
from models import User,City,Worker,Cooperation,Workshop,Product,Warehouse,Produce,Order,Attendance,Performance,Store,Order_product
from flask import Flask,render_template,request,redirect,url_for,session,jsonify
from exts import db
from sqlalchemy import and_,or_
mainpage_bp = Blueprint('mainpage',__name__) #url_prefix url前缀 template_folder static_folder

#城市与对应时间（列表）
@mainpage_bp.route('/city/',methods=['GET','POST'])
@login_required
def city():
    if request.method == 'GET':
        return render_template('mainpage/city.html')
    else:
        title = request.form.get('title')
        city = City(title=title)
        db.session.add(city)
        db.session.commit()
        return redirect(url_for('index'))
