from flask import Blueprint
from decorators import login_required
from models import User,City,Worker,Cooperation,Workshop,Product,Warehouse,Produce,Order,Attendance,Performance,Store,Order_product
from flask import Flask,render_template,request,redirect,url_for,session,jsonify
from exts import db
from sqlalchemy import and_,or_
detail_bp = Blueprint('detail',__name__) #url_prefix url前缀 template_folder static_folder

#详情页
@detail_bp.route('/city/',methods=['GET','POST'])
@login_required
def detail():
    if request.method == 'GET':
        return render_template('detail/detail.html')
    else:
        title = request.form.get('title')
        detail = City(title=title)
        db.session.add(detail)
        db.session.commit()
        return redirect(url_for('index'))