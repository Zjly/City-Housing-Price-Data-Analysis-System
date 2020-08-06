后端部分文件结构：<br/>
1.blueprints文件夹：蓝图管理，存放视图函数<br/>
其中：options.py:管理员部分<br/>
mainpage.py:主页部分<br/>
detail.py:详情页面<br/>
myutils.py:登录注册注销<br/>
2.migrations文件夹：数据库迁移<br/>
3.config.py：连接数据库，配置基本信息<br/>
4.decorators.py：存装饰器（主要实现的是查看详情前要登录）<br/>
5.exts.py：数据库初始化<br/>
6.main.py：主app文件<br/>
7.manage.py：数据库迁移管理<br/>
8.models.py：创建数据库表<br/>
9.myutils.py：一些有用的函数<br/>