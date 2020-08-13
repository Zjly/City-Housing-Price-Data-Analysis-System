from flask import jsonify,request
from app.api import bp
import pymysql
from app.api.errors import bad_request
import json


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

@bp.route('/housedata', methods=['GET'])
def housedata():
    '''前端Vue.js用来测试与后端Flask API的连通性'''
    return jsonify('Pong!')

@bp.route('/houseaddress', methods=['POST'])
def choose_address():
    '''选择查询内容'''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'choose' not in data or not data.get('choose', None):
        return bad_request('Please provide a valid choose')
    if data.get('choose', 'esf'):
        address_esf_province()
    if data.get('choose', 'esf'):
        address_new_province()
    if data.get('choose', 'esf'):
        address_info_province()

# 查询新房省市
@bp.route('/houseaddress', methods=['GET'])
def address_All_City():
    '''选择查询内容'''
    # 连接云数据库
    conn = pymysql.connect(host='121.36.253.244',port=3306,user='root',password='root',database='houseprice',charset='utf8')
    # 获取一个光标,返回字典数据类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 定义执行的sql语句
    sql = 'select * from newhouse_location;'
    # 拼接并执行sql语句
    cursor.execute(sql)
    # 取得查询结果，这里是一个元组
    house_location = cursor.fetchall()
    # result = Class_to_data(house_location,__field__)
    print(type(house_location))
    cursor.close()
    conn.close()
    return jsonify({
        "status":200,
        "data":house_location
    })
# 查询二手房省市
@bp.route('/houseaddress2', methods=['GET'])
def address_All_City2():
    '''选择查询内容'''
    # 连接云数据库
    conn = pymysql.connect(host='121.36.253.244',port=3306,user='root',password='root',database='houseprice',charset='utf8')
    # 获取一个光标,返回字典数据类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 定义执行的sql语句
    sql = 'select * from esf_location;'
    # 拼接并执行sql语句
    cursor.execute(sql)
    # 取得查询结果，这里是一个元组
    house_location = cursor.fetchall()
    # result = Class_to_data(house_location,__field__)
    print(type(house_location))
    cursor.close()
    conn.close()
    return jsonify({
        "status":200,
        "data":house_location
    })



