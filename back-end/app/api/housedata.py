from flask import jsonify, request
from app.api import bp
import pymysql
from app.api.errors import bad_request
from app.models import Newhouse, Esf,Info

# newInfo = NewsInfo()
# data = newInfo.findALL()
# print(data)
# 数据处理方法
def Class_to_data(data_list, fields, type=0):
    # 数组
    if not type:
        list = []
        for item in data_list:
            temp = {}
            for f in fields:
                temp[f] = getattr(item, f)
            list.append(temp)
    else:
        list = {}
        for f in fields:
            list[f] = getattr(data_list, f)

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
    conn = pymysql.connect(host='121.36.253.244', port=3306, user='root', password='root', database='houseprice',
                           charset='utf8')
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
        "status": 200,
        "data": house_location
    })


# 查询二手房省市
@bp.route('/houseaddress2', methods=['GET'])
def address_All_City2():
    '''选择查询内容'''
    # 连接云数据库
    conn = pymysql.connect(host='121.36.253.244', port=3306, user='root', password='root', database='houseprice',
                           charset='utf8')
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
        "status": 200,
        "data": house_location
    })

# 查询二手房省市
@bp.route('/houseaddress3', methods=['GET'])
def address_All_City3():
    '''选择查询内容'''
    # 连接云数据库
    conn = pymysql.connect(host='121.36.253.244', port=3306, user='root', password='root', database='houseprice',
                           charset='utf8')
    # 获取一个光标,返回字典数据类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 定义执行的sql语句
    sql = 'select * from info_location;'
    # 拼接并执行sql语句
    cursor.execute(sql)
    # 取得查询结果，这里是一个元组
    house_location = cursor.fetchall()
    # result = Class_to_data(house_location,__field__)
    print(type(house_location))
    cursor.close()
    conn.close()
    return jsonify({
        "status": 200,
        "data": house_location
    })


# 查询新房
@bp.route('/newhouses/<string:province>/<string:city>', methods=['POST'])
def query_newhouse(province, city):
    print(province, city)
    newhouse = Newhouse.query.filter(Newhouse.province == province, Newhouse.city == city, Newhouse.price > 0). \
        with_entities(Newhouse.id, Newhouse.district, Newhouse.name, Newhouse.area, Newhouse.price).all()
    return jsonify(newhouse)


# 查询二手房
@bp.route('/esfs/<string:province>/<string:city>', methods=['POST'])
def query_esf(province, city):
    esf = Esf.query.filter_by(province=province, city=city). \
        with_entities(Esf.id, Esf.address, Esf.name, Esf.area, Esf.price).all()
    print(type(esf))
    print(jsonify(esf))
    return jsonify(esf)

# 查询走势
@bp.route('/trendinfo/<string:province>/<string:city>', methods=['POST'])
def query_trendinfo(province, city):
    print(province, city)
    trendinfo = Info.query.filter(Info.province == province, Info.city == city). \
        with_entities(Info.id, Info.areaPrice, Info.esfareaPrice, Info.compareDate, Info.compareYear).all()
    return jsonify(trendinfo)
