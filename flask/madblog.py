import click
import os
import sys
import json
from app import create_app
from app.extensions import db
from app.models import User, Post, Comment, Notification, Message
from config import Config
from app.models import Role

app = create_app(Config)

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