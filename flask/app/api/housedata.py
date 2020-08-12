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



# # @bp.route('/address', methods=['GET'])
# # def address_esf_province():
# #     '''查询二手房时列出省份'''
# #     # 连接云数据库
# #     conn = pymysql.connect(host='121.36.253.244',port=3306,user='root',password='root',database='houseprice',charset='utf8')
# #     # 获取一个光标,返回字典数据类型
# #     cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# #     # 定义执行的sql语句
# #     sql = 'select province from esf_location;'
# #     # 拼接并执行sql语句
# #     cursor.execute(sql)
# #     # 取得查询结果，这里是一个元组
# #     province = cursor.fetchall()
# #     cursor.close()
# #     conn.close()
# #     return jsonify({'province':province.to_dict()})

# @bp.route('/address', methods=['GET'])
# def address_esf_city():
#     '''查询二手房时列出城市'''
#     data = request.get_json()
#     if not data:
#         return bad_request('You must post JSON data.')
#     if 'province' not in data or not data.get('province', None):
#         return bad_request('Please provide a valid province')
#     else:
#         conn = pymysql.connect(host='121.36.253.244',port=3306,user='root',password='root',database='houseprice',charset='utf8')
#         cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#         sql = 'select city from esf_location where province = %s;'
#         cursor.execute(sql,data.get('province'))
#         city = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return jsonify({'city':city})

# @bp.route('/address', methods=['GET'])
# def address_esf_list(city):
#     '''查询二手房时列出房价列表'''
#     data = request.get_json()
#     if not data:
#         return bad_request('You must post JSON data.')
#     if 'city' not in data or not data.get('city', None):
#         return bad_request('Please provide a valid city')
#     else:
#         conn = pymysql.connect(host='121.36.253.244',port=3306,user='root',password='root',database='houseprice',charset='utf8')
#         cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#         sql = 'select province from esf where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         province = cursor.fetchall()
#         sql = 'select name from esf where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         name = cursor.fetchall()
#         sql = 'select rooms from esf where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         rooms = cursor.fetchall()
#         sql = 'select floor from esf where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         floor = cursor.fetchall()
#         sql = 'select towards from esf where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         towards = cursor.fetchall()
#         sql = 'select address from esf where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         address = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return jsonify({'province':province.to_dict(),'city':city.to_dict(),'name':name.to_dict(),'rooms':rooms.to_dict(),
#                         'fllor':floor.to_dict(),'towards':towards.to_dict(),'address':address.to_dict()})


# @bp.route('/address', methods=['GET'])
# def address_new_province():
#     '''查询新房时列出省份'''
#     conn = pymysql.connect(host='121.36.253.244',port=3306,user='root',password='root',database='houseprice',charset='utf8')
#     cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#     sql = 'select province from newhouse_location;'
#     cursor.execute(sql)
#     province = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return jsonify({'province':province.to_dict()})

# @bp.route('/address', methods=['GET'])
# def address_new_city(province):
#     '''查询新房时列出城市'''
#     data = request.get_json()
#     if not data:
#         return bad_request('You must post JSON data.')
#     if 'province' not in data or not data.get('province', None):
#         return bad_request('Please provide a valid province')
#     else:
#         conn = pymysql.connect(host='121.36.253.244', port=3306, user='root', password='root', database='houseprice',
#                                charset='utf8')
#         cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#         sql = 'select city from newhouse_location where province = %s;'
#         cursor.execute(sql, data.get('province'))
#         city = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return jsonify({'city': city.to_dict()})

# @bp.route('/address', methods=['GET'])
# def address_new_list(city):
#     '''查询新房时列出房价列表'''
#     data = request.get_json()
#     if not data:
#         return bad_request('You must post JSON data.')
#     if 'city' not in data or not data.get('city', None):
#         return bad_request('Please provide a valid city')
#     else:
#         conn = pymysql.connect(host='121.36.253.244',port=3306,user='root',password='root',database='houseprice',charset='utf8')
#         cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#         sql = 'select province from newhouse_location where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         province = cursor.fetchall()
#         sql = 'select name from newhouse_location where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         name = cursor.fetchall()
#         sql = 'select rooms from newhouse_location where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         rooms = cursor.fetchall()
#         sql = 'select floor from newhouse_location where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         floor = cursor.fetchall()
#         sql = 'select towards from newhouse_location where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         towards = cursor.fetchall()
#         sql = 'select address from newhouse_location where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         address = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return jsonify({'province':province.to_dict(),'city':city.to_dict(),'name':name.to_dict(),'rooms':rooms.to_dict(),
#                             'fllor':floor.to_dict(),'towards':towards.to_dict(),'address':address.to_dict()})


# @bp.route('/address', methods=['GET'])
# def address_info_province():
#     '''查询历史房价时列出省份'''
#     conn = pymysql.connect(host='121.36.253.244',port=3306,user='root',password='root',database='houseprice',charset='utf8')
#     cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#     sql = 'select province from info_location;'
#     cursor.execute(sql)
#     province = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return jsonify({'province':province.to_dict()})

# @bp.route('/address', methods=['GET'])
# def address_info_city(province):
#     '''查询历史房价时列出城市'''
#     data = request.get_json()
#     if not data:
#         return bad_request('You must post JSON data.')
#     if 'province' not in data or not data.get('province', None):
#         return bad_request('Please provide a valid province')
#     else:
#         conn = pymysql.connect(host='121.36.253.244', port=3306, user='root', password='root', database='houseprice',
#                                charset='utf8')
#         cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#         sql = 'select city from info_location where province = %s;'
#         cursor.execute(sql, data.get('province'))
#         city = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return jsonify({'city': city.to_dict()})

# @bp.route('/address', methods=['GET'])
# def address_info_list(city):
#     '''查询历史房价时列出房价列表'''
#     data = request.get_json()
#     if not data:
#         return bad_request('You must post JSON data.')
#     if 'city' not in data or not data.get('city', None):
#         return bad_request('Please provide a valid city')
#     else:
#         conn = pymysql.connect(host='121.36.253.244',port=3306,user='root',password='root',database='houseprice',charset='utf8')
#         cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#         sql = 'select province from info where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         province = cursor.fetchall()
#         sql = 'select name from info where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         name = cursor.fetchall()
#         sql = 'select areaPrice from info where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         areaPrice = cursor.fetchall()
#         sql = 'select esfareaPrice from info where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         esfareaPrice = cursor.fetchall()
#         sql = 'select compareDate from info where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         compareDate = cursor.fetchall()
#         sql = 'select compareYear from info where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         compareYear = cursor.fetchall()
#         sql = 'select new_avg from info where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         new_avg = cursor.fetchall()
#         sql = 'select esf_avg from info where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         esf_avg = cursor.fetchall()
#         sql = 'select new_cgreen from info where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         new_cgreen = cursor.fetchall()
#         sql = 'select esf_cgreen from info where city = %s;'
#         cursor.execute(sql, data.get('city'))
#         esf_cgreen = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return jsonify({'province':province.to_dict(), 'city':city.to_dict(), 'name':name.to_dict(), 'areaPrice':areaPrice.to_dict(),
#                         'esfareaPrice':esfareaPrice.to_dict(),'compareDate':compareDate.to_dict(),'compareYear':compareYear.to_dict(),
#                         'new_avg':new_avg.to_dict(),'esf_avg':esf_avg.to_dict(),'new_cgreen':new_cgreen.to_dict(),'esf_cgreen':esf_cgreen.to_dict()})

