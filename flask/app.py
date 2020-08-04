from flask import Flask,request
import json
from flask_cors import CORS
# 实例化这个类，创建一个程序对象 app
app = Flask(__name__)

# 跨域问题
# pip install flask-cors
CORS(app, supports_credentials=True)

# 首页
@ app.route('/')
def index():
    return "hello" 

# 为折线图 平均工资 无参数 get
@app.route('/line')
def line():
    with open('./json/average.json','r') as f:
        # content = f.read() # 字符串不能直接返回给前端，前端不好处理
        content = json.load(f)
        return json.dumps({"status":200,"data":content})

# 饼图 百分比 无参数 get
@app.route('/pie')
def pie():
    with open('./json/pie.json','r')as f:
        content = json.load(f)
        return json.dumps({"status":200,"data":content})


# 词云图 百分比 数据过多 参数:num = 
@app.route('/cloud')
def cloud():
    num = request.args.get('num') # 从前端获取
    with open('./json/count_list.json','r')as f:
        content = json.load(f)
        # 从content中取num条
        result = []
        for i in range(int(num)):
            result.append(content[i])
        return json.dumps({"status":200,"data":result})



app.run()
