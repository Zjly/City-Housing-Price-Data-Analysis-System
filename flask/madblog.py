import click
import os
import sys
import json
from app import create_app
from app.extensions import db
from app.models import User, Post, Comment, Notification, Message
from config import Config
from app.models import Role
from flask import request,Response
from flask_sqlalchemy import SQLAlchemy
app = create_app(Config)


DB = SQLAlchemy(app)
# 构建数据模型
class News(DB.Model):
    __tablename__ = 'sohu_news_details'
    id = DB.Column(DB.Integer,primary_key=True)
    title = DB.Column(DB.String,unique=True)
    time = DB.Column(DB.String,unique=True)
    content = DB.Column(DB.String,unique=True)
    def __init__(self,title,time,content,score):
        self.title = title
        self.time = time
        self.content = content
    
    # 重写
    def __repr__(self):
        return self.title

# 数据库操作模型
class NewsInfo():
    def __init__(self):
        self.__fields__ = ['id','title','time','content']

    def findALL(self):
        return News.query.all()
    def find_by_id(self,find_id):
        # 根据条件筛选
        return News.query.filter_by(id = find_id).all()

# newInfo = NewsInfo()
# data = newInfo.findALL()
# print(data)
# 数据处理方法
def Class_to_data(data_list,fields,type=0):
    # 数组
    if not type:
        list = []
        for item in data_list:
            temp = {}
            for f in fields:
                temp[f] = getattr(item,f)
            list.append(temp)
    else:
        list = {}
        for f in fields:
            list[f] = getattr(data_list,f)
    
    return list


@app.route('/news')
def all():
    newInfo = NewsInfo()
    data = newInfo.findALL()
    # 处理data，json可以解析的
    result = Class_to_data(data,newInfo.__fields__)
    return Response(json.dumps({
        'status':200,
        'data':result
    }))
    

# 创建 coverage 实例
COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()


@app.route('/')
def hello_world():
    return 'Hello, World!'

# 为折线图 平均房价 无参数 get
@app.route('/line')
def line():
    with open('./json/average.json','r') as f:
        # content = f.read() # 字符串不能直接返回给前端，前端不好处理
        content = json.load(f)
        return json.dumps({"status":200,"data":content})


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Role': Role, 'User': User, 'Post': Post, 'Comment': Comment,
            'Notification': Notification, 'Message': Message}


@app.cli.command()
@click.option('--coverage/--no-coverage', default=False, help='Run tests under code coverage.')
def test(coverage):
    '''Run the unit tests.'''
    # 如果执行 flask test --coverage，但是FLASK_COVERAGE环境变量不存在时，给它配置上
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import subprocess
        os.environ['FLASK_COVERAGE'] = '1'  # 需要字符串的值
        sys.exit(subprocess.call(sys.argv))

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(os.path.join(basedir, 'tmp'), 'coverage')
        COV.html_report(directory=covdir)
        print('')
        print('HTML report be stored in: %s' % os.path.join(covdir, 'index.html'))
        COV.erase()