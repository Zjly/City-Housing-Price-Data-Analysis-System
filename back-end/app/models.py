import base64
from datetime import datetime, timedelta
from hashlib import md5
import json
import jwt
from time import time
from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for, current_app
from app.extensions import db


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        # 如果当前没有任何资源时，或者前端请求的 page 越界时，都会抛出 404 错误
        # 由 @bp.app_errorhandler(404) 自动处理，即响应 JSON 数据：{ error: "Not Found" }
        resources = query.paginate(page, per_page)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data




# 粉丝关注他人
followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('timestamp', db.DateTime, default=datetime.utcnow)
)

# 评论点赞
comments_likes = db.Table(
    'comments_likes',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('comment_id', db.Integer, db.ForeignKey('comments.id')),
    db.Column('timestamp', db.DateTime, default=datetime.utcnow)
)

# 黑名单(user_id 屏蔽 block_id)
blacklist = db.Table(
    'blacklist',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('block_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('timestamp', db.DateTime, default=datetime.utcnow)
)

# 喜欢文章
posts_likes = db.Table(
    'posts_likes',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
    db.Column('timestamp', db.DateTime, default=datetime.utcnow)
)

class Permission:
    '''权限认证中的各种操作，对应二进制的位，比如
    FOLLOW: 0b00000001，转换为十六进制为 0x01
    COMMENT: 0b00000010，转换为十六进制为 0x02
    WRITE: 0b00000100，转换为十六进制为 0x04
    ...
    ADMIN: 0b10000000，转换为十六进制为 0x80

    中间还预留了第 4、5、6、7 共4位二进制位，以备后续增加操作权限
    '''
    # 关注其它用户的权限
    FOLLOW = 0x01
    # 发表评论、评论点赞与踩的权限
    COMMENT = 0x02
    # 撰写文章的权限
    WRITE = 0x04
    # 管理网站的权限(对应管理员角色)
    ADMIN = 0x80


class Role(PaginatedAPIMixin, db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))  # 角色名称
    default = db.Column(db.Boolean, default=False, index=True)  # 当新增用户时，是否将当前角色作为默认角色赋予新用户
    permissions = db.Column(db.Integer)  # 角色拥有的权限，各操作对应一个二进制位，能执行某项操作的角色，其位会被设为 1
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    @staticmethod
    def insert_roles():
        '''应用部署时，应该主动执行此函数，添加以下角色
        注意: 未登录的用户，可以浏览，但不能评论或点赞等
        shutup:        0b0000 0000 (0x00) 用户被关小黑屋，收回所有权限
        reader:        0b0000 0011 (0x03) 读者，可以关注别人、评论与点赞，但不能发表文章
        author:        0b0000 0111 (0x07) 作者，可以关注别人、评论与点赞，发表文章
        administrator: 0b1000 0111 (0x87) 超级管理员，拥有全部权限

        以后如果要想添加新角色，或者修改角色的权限，修改 roles 数组，再运行函数即可
        '''
        roles = {
            'shutup': ('小黑屋', ()),
            'reader': ('读者', (Permission.FOLLOW, Permission.COMMENT)),
            'author': ('作者', (Permission.FOLLOW, Permission.COMMENT, Permission.WRITE)),
            'administrator': ('管理员', (Permission.FOLLOW, Permission.COMMENT, Permission.WRITE, Permission.ADMIN)),
        }
        default_role = 'reader'
        for r in roles:  # r 是字典的键
            role = Role.query.filter_by(slug=r).first()
            if role is None:
                role = Role(slug=r, name=roles[r][0])
            role.reset_permissions()
            for perm in roles[r][1]:
                role.add_permission(perm)
            role.default = (role.slug == default_role)
            db.session.add(role)
        db.session.commit()

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def get_permissions(self):
        '''获取角色的具体操作权限列表'''
        p = [(Permission.FOLLOW, 'follow'), (Permission.COMMENT, 'comment'), (Permission.WRITE, 'write'), (Permission.ADMIN, 'admin')]
        # 过滤掉没有权限，注意不能用 for 循环，因为遍历列表时删除元素可能结果并不是你想要的，参考: https://segmentfault.com/a/1190000007214571
        new_p = filter(lambda x: self.has_permission(x[0]), p)
        return ','.join([x[1] for x in new_p])  # 用逗号拼接成str

    def to_dict(self):
        data = {
            'id': self.id,
            'slug': self.slug,
            'name': self.name,
            'default': self.default,
            'permissions': self.permissions,
            '_links': {
                'self': url_for('api.get_role', id=self.id)
            }
        }
        return data

    def from_dict(self, data):
        for field in ['slug', 'name', 'permissions']:
            if field in data:
                setattr(self, field, data[field])

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Role {}>'.format(self.name)


class User(PaginatedAPIMixin, db.Model):
    # 设置数据库表名，Post模型中的外键 user_id 会引用 users.id
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))  # 不保存原始密码
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    # 反向引用，直接查询出当前用户的所有博客文章; 同时，Post实例中会有 author 属性
    # cascade 用于级联删除，当删除user时，该user下面的所有posts都会被级联删除
    posts = db.relationship('Post', backref='author', lazy='dynamic',
                            cascade='all, delete-orphan')
    # followeds 是该用户关注了哪些用户列表
    # followers 是该用户的粉丝列表
    followeds = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    # 用户发表的评论列表
    comments = db.relationship('Comment', backref='author', lazy='dynamic',
                               cascade='all, delete-orphan')
    # 用户最后一次查看 收到的评论 页面的时间，用来判断哪些收到的评论是新的
    last_recived_comments_read_time = db.Column(db.DateTime)
    # 用户最后一次查看 用户的粉丝 页面的时间，用来判断哪些粉丝是新的
    last_follows_read_time = db.Column(db.DateTime)
    # 用户最后一次查看 收到的文章被喜欢 页面的时间，用来判断哪些喜欢是新的
    last_posts_likes_read_time = db.Column(db.DateTime)
    # 用户最后一次查看 收到的评论点赞 页面的时间，用来判断哪些点赞是新的
    last_comments_likes_read_time = db.Column(db.DateTime)
    # 用户最后一次查看 关注的人的博客 页面的时间，用来判断哪些文章是新的
    last_followeds_posts_read_time = db.Column(db.DateTime)
    # 用户的通知
    notifications = db.relationship('Notification', backref='user',
                                    lazy='dynamic', cascade='all, delete-orphan')
    # 用户发送的私信
    messages_sent = db.relationship('Message', foreign_keys='Message.sender_id',
                                    backref='sender', lazy='dynamic',
                                    cascade='all, delete-orphan')
    # 用户接收的私信
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic',
                                        cascade='all, delete-orphan')
    # 用户最后一次查看私信的时间
    last_messages_read_time = db.Column(db.DateTime)
    # harassers 骚扰者(被拉黑的人)
    # sufferers 受害者
    harassers = db.relationship(
        'User', secondary=blacklist,
        primaryjoin=(blacklist.c.user_id == id),
        secondaryjoin=(blacklist.c.block_id == id),
        backref=db.backref('sufferers', lazy='dynamic'), lazy='dynamic')
    # 用户注册后，需要先确认邮箱
    confirmed = db.Column(db.Boolean, default=False)
    # 用户所属的角色
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        '''设置用户密码，保存为 Hash 值'''
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        '''验证密码与保存的 Hash 值是否匹配'''
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        '''用户头像'''
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def to_dict(self, include_email=False):
        roles = {
            '1': '小黑屋',
            '2': '读者',
            '3': '作者',
            '4': '管理员'
        }
        data = {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'location': self.location,
            'about_me': self.about_me,
            'role_id': self.role_id,
            'role_name': roles[str(self.role_id)],
            'member_since': self.member_since.isoformat() + 'Z',
            'last_seen': self.last_seen.isoformat() + 'Z',
            'followeds_count': self.followeds.count(),
            'followers_count': self.followers.count(),
            'posts_count': self.posts.count(),
            'followeds_posts_count': self.followeds_posts().count(),
            'comments_count': self.comments.count(),
            'confirmed': self.confirmed,
            '_links': {
                'self': url_for('api.get_user', id=self.id),
                'avatar': self.avatar(128),
                'followeds': url_for('api.get_followeds', id=self.id),
                'followers': url_for('api.get_followers', id=self.id),
                'posts': url_for('api.get_user_posts', id=self.id),
                'followeds_posts': url_for('api.get_user_followeds_posts', id=self.id),
                'comments': url_for('api.get_user_comments', id=self.id)
            }
        }
        if include_email:
            data['email'] = self.email
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email', 'name', 'location', 'about_me', 'confirmed', 'role_id']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])
            # 新建用户时，给用户自动分配角色
            if self.role is None:
                if self.email in current_app.config['ADMINS']:
                    self.role = Role.query.filter_by(slug='administrator').first()
                else:
                    self.role = Role.query.filter_by(default=True).first()

    def ping(self):
        '''更新用户的最后访问时间'''
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def get_jwt(self, expires_in=3600):
        '''用户登录后，发放有效的 JWT'''
        now = datetime.utcnow()
        payload = {
            'user_id': self.id,
            'confirmed': self.confirmed,
            'user_name': self.name if self.name else self.username,
            'user_avatar': base64.b64encode(self.avatar(24).
                                            encode('utf-8')).decode('utf-8'),
            'permissions': self.role.get_permissions(),
            'exp': now + timedelta(seconds=expires_in),
            'iat': now
        }
        return jwt.encode(
            payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_jwt(token):
        '''验证 JWT 的有效性'''
        try:
            payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256'])
        except (jwt.exceptions.ExpiredSignatureError,
                jwt.exceptions.InvalidSignatureError,
                jwt.exceptions.DecodeError) as e:
            # Token过期，或被人修改，那么签名验证也会失败
            return None
        return User.query.get(payload.get('user_id'))

    def can(self, perm):
        '''检查用户是否有指定的权限'''
        return self.role is not None and self.role.has_permission(perm)

    def is_administrator(self):
        '''检查用户是否为管理员'''
        return self.can(Permission.ADMIN)

    def is_following(self, user):
        '''判断当前用户是否已经关注了 user 这个用户对象，如果关注了，下面表达式左边是1，否则是0'''
        return self.followeds.filter(
            followers.c.followed_id == user.id).count() > 0

    def follow(self, user):
        '''当前用户开始关注 user 这个用户对象'''
        if not self.is_following(user):
            self.followeds.append(user)

    def unfollow(self, user):
        '''当前用户取消关注 user 这个用户对象'''
        if self.is_following(user):
            self.followeds.remove(user)

    def followeds_posts(self):
        '''获取当前用户的关注者的所有博客列表'''
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.author_id)).filter(
                followers.c.follower_id == self.id)
        # 包含当前用户自己的博客列表
        # own = Post.query.filter_by(user_id=self.id)
        # return followed.union(own).order_by(Post.timestamp.desc())
        return followed.order_by(Post.timestamp.desc())

    def add_notification(self, name, data):
        '''给用户实例对象增加通知'''
        # 如果具有相同名称的通知已存在，则先删除该通知
        self.notifications.filter_by(name=name).delete()
        # 为用户添加通知，写入数据库
        n = Notification(name=name, payload_json=json.dumps(data), user=self)
        db.session.add(n)
        return n

    def new_recived_comments(self):
        '''用户收到的新评论计数
        包括:
        1. 用户的所有文章下面新增的评论
        2. 用户发表的评论(或下面的子孙)被人回复了
        '''
        last_read_time = self.last_recived_comments_read_time or datetime(1900, 1, 1)
        # 用户发布的所有文章
        user_posts_ids = [post.id for post in self.posts.all()]
        # 用户文章下面的新评论, 即评论的 post_id 在 user_posts_ids 集合中，且评论的 author 不是自己(文章的作者)
        q1 = set(Comment.query.filter(Comment.post_id.in_(user_posts_ids), Comment.author != self).all())

        # 用户发表的评论被人回复了，找到每个用户评论的所有子孙
        q2 = set()
        for c in self.comments:
            q2 = q2 | c.get_descendants()
        q2 = q2 - set(self.comments.all())  # 除去子孙中，用户自己发的(因为是多级评论，用户可能还会在子孙中盖楼)，自己回复的不用通知
        # 用户收到的总评论集合为 q1 与 q2 的并集
        recived_comments = q1 | q2
        # 最后，再过滤掉 last_read_time 之前的评论
        return len([c for c in recived_comments if c.timestamp > last_read_time])

    def new_follows(self):
        '''用户的新粉丝计数'''
        last_read_time = self.last_follows_read_time or datetime(1900, 1, 1)
        return self.followers.filter(followers.c.timestamp > last_read_time).count()

    def new_comments_likes(self):
        '''用户收到的新评论点赞计数'''
        last_read_time = self.last_comments_likes_read_time or datetime(1900, 1, 1)
        # 当前用户发表的所有评论当中，哪些被点赞了
        comments = self.comments.join(comments_likes).all()
        # 新的点赞记录计数
        new_likes_count = 0
        for c in comments:
            # 获取点赞时间
            for u in c.likers:
                if u != self:  # 用户自己点赞自己的评论不需要被通知
                    res = db.engine.execute("select * from comments_likes where user_id={} and comment_id={}".format(u.id, c.id))
                    timestamp = datetime.strptime(str(list(res)[0][2]), '%Y-%m-%d %H:%M:%S')
                    # 判断本条点赞记录是否为新的
                    if timestamp > last_read_time:
                        new_likes_count += 1
        return new_likes_count

    def new_followeds_posts(self):
        '''用户关注的人的新发布的文章计数'''
        last_read_time = self.last_followeds_posts_read_time or datetime(1900, 1, 1)
        return self.followeds_posts().filter(Post.timestamp > last_read_time).count()

    def new_recived_messages(self):
        '''用户未读的私信计数'''
        last_read_time = self.last_messages_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()

    def is_blocking(self, user):
        '''判断当前用户是否已经拉黑了 user 这个用户对象，如果拉黑了，下面表达式左边是1，否则是0'''
        return self.harassers.filter(
            blacklist.c.block_id == user.id).count() > 0

    def block(self, user):
        '''当前用户开始拉黑 user 这个用户对象'''
        if not self.is_blocking(user):
            self.harassers.append(user)

    def unblock(self, user):
        '''当前用户取消拉黑 user 这个用户对象'''
        if self.is_blocking(user):
            self.harassers.remove(user)

    def new_posts_likes(self):
        '''用户收到的文章被喜欢的新计数'''
        last_read_time = self.last_posts_likes_read_time or datetime(1900, 1, 1)
        # 当前用户发布的文章当中，哪些文章被喜欢了
        posts = self.posts.join(posts_likes).all()
        # 新的喜欢记录计数
        new_likes_count = 0
        for p in posts:
            # 获取喜欢时间
            for u in p.likers:
                if u != self:  # 用户自己喜欢自己的文章不需要被通知
                    res = db.engine.execute("select * from posts_likes where user_id={} and post_id={}".format(u.id, p.id))
                    timestamp = datetime.strptime(str(list(res)[0][2]), '%Y-%m-%d %H:%M:%S')
                    # 判断本条喜欢记录是否为新的
                    if timestamp > last_read_time:
                        new_likes_count += 1
        return new_likes_count

    def generate_confirm_jwt(self, expires_in=3600):
        '''生成确认账户的 JWT'''
        now = datetime.utcnow()
        payload = {
            'confirm': self.id,
            'exp': now + timedelta(seconds=expires_in),
            'iat': now
        }
        return jwt.encode(
            payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')

    def verify_confirm_jwt(self, token):
        '''用户点击确认邮件中的URL后，需要检验 JWT，如果检验通过，则把新添加的 confirmed 属性设为 True'''
        try:
            payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256'])
        except (jwt.exceptions.ExpiredSignatureError,
                jwt.exceptions.InvalidSignatureError,
                jwt.exceptions.DecodeError) as e:
            # Token过期，或被人修改，那么签名验证也会失败
            return False
        if payload.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_password_jwt(self, expires_in=3600):
        '''生成重置账户密码的 JWT'''
        now = datetime.utcnow()
        payload = {
            'reset_password': self.id,
            'exp': now + timedelta(seconds=expires_in),
            'iat': now
        }
        return jwt.encode(
            payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_jwt(token):
        '''用户点击重置密码邮件中的URL后，需要检验 JWT
        如果检验通过，则返回 JWT 中存储的 id 所对应的用户实例'''
        try:
            payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256'])
        except (jwt.exceptions.ExpiredSignatureError,
                jwt.exceptions.InvalidSignatureError,
                jwt.exceptions.DecodeError) as e:
            # Token过期，或被人修改，那么签名验证也会失败
            return None
        return User.query.get(payload.get('reset_password'))


class Post(PaginatedAPIMixin, db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    summary = db.Column(db.Text)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    views = db.Column(db.Integer, default=0)
    # 外键, 直接操纵数据库当user下面有posts时不允许删除user，下面仅仅是 ORM-level “delete” cascade
    # db.ForeignKey('users.id', ondelete='CASCADE') 会同时在数据库中指定 FOREIGN KEY level “ON DELETE” cascade
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic',
                               cascade='all, delete-orphan')
    # 博客文章与喜欢/收藏它的人是多对多关系
    likers = db.relationship('User', secondary=posts_likes, backref=db.backref('liked_posts', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<Post {}>'.format(self.title)

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        '''
        target: 有监听事件发生的 Post 实例对象
        value: 监听哪个字段的变化
        '''
        if not target.summary:  # 如果前端不填写摘要，是空str，而不是None
            target.summary = value[:200] + '  ... ...'  # 截取 body 字段的前200个字符给 summary

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'summary': self.summary,
            'body': self.body,
            'timestamp': self.timestamp,
            'views': self.views,
            'likers_id': [user.id for user in self.likers],
            'likers': [
                {
                    'id': user.id,
                    'username': user.username,
                    'name': user.name,
                    'avatar': user.avatar(128)
                } for user in self.likers
            ],
            'author': {
                'id': self.author.id,
                'username': self.author.username,
                'name': self.author.name,
                'avatar': self.author.avatar(128)
            },
            'likers_count': self.likers.count(),
            'comments_count': self.comments.count(),
            '_links': {
                'self': url_for('api.get_post', id=self.id),
                'author_url': url_for('api.get_user', id=self.author_id),
                'comments': url_for('api.get_post_comments', id=self.id)
            }
        }
        return data

    def from_dict(self, data):
        for field in ['title', 'summary', 'body', 'timestamp', 'views']:
            if field in data:
                setattr(self, field, data[field])

    def is_liked_by(self, user):
        '''判断用户 user 是否已经收藏过该文章'''
        return user in self.likers

    def liked_by(self, user):
        '''收藏'''
        if not self.is_liked_by(user):
            self.likers.append(user)

    def unliked_by(self, user):
        '''取消收藏'''
        if self.is_liked_by(user):
            self.likers.remove(user)


db.event.listen(Post.body, 'set', Post.on_changed_body)  # body 字段有变化时，执行 on_changed_body() 方法


class Comment(PaginatedAPIMixin, db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    mark_read = db.Column(db.Boolean, default=False)  # 文章作者会收到评论提醒，可以标为已读
    disabled = db.Column(db.Boolean, default=False)  # 屏蔽显示
    # 评论与对它点赞的人是多对多关系
    likers = db.relationship('User', secondary=comments_likes, backref=db.backref('liked_comments', lazy='dynamic'), lazy='dynamic')
    # 外键，评论作者的 id
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # 外键，评论所属文章的 id
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    # 自引用的多级评论实现
    parent_id = db.Column(db.Integer, db.ForeignKey('comments.id', ondelete='CASCADE'))
    # 级联删除的 cascade 必须定义在 "多" 的那一侧，所以不能这样定义: parent = db.relationship('Comment', backref='children', remote_side=[id], cascade='all, delete-orphan')
    parent = db.relationship('Comment', backref=db.backref('children', cascade='all, delete-orphan'), remote_side=[id])

    def __repr__(self):
        return '<Comment {}>'.format(self.id)

    def get_descendants(self):
        '''获取评论的所有子孙'''
        data = set()

        def descendants(comment):
            if comment.children:
                data.update(comment.children)
                for child in comment.children:
                    descendants(child)
        descendants(self)
        return data

    def get_ancestors(self):
        '''获取评论的所有祖先'''
        data = []

        def ancestors(comment):
            if comment.parent:
                data.append(comment.parent)
                ancestors(comment.parent)
        ancestors(self)
        return data

    def to_dict(self):
        data = {
            'id': self.id,
            'body': self.body,
            'timestamp': self.timestamp,
            'mark_read': self.mark_read,
            'disabled': self.disabled,
            'likers_id': [user.id for user in self.likers],
            'author': {
                'id': self.author.id,
                'username': self.author.username,
                'name': self.author.name,
                'avatar': self.author.avatar(128)
            },
            'post': {
                'id': self.post.id,
                'title': self.post.title,
                'author_id': self.post.author.id
            },
            'parent_id': self.parent.id if self.parent else None,
            # 'children': [child.to_dict() for child in self.children] if self.children else None,
            '_links': {
                'self': url_for('api.get_comment', id=self.id),
                'author_url': url_for('api.get_user', id=self.author_id),
                'post_url': url_for('api.get_post', id=self.post_id),
                'parent_url': url_for('api.get_comment', id=self.parent.id) if self.parent else None,
                'children_url': [url_for('api.get_comment', id=child.id) for child in self.children] if self.children else None
            }
        }
        return data

    def from_dict(self, data):
        for field in ['body', 'timestamp', 'mark_read', 'disabled', 'author_id', 'post_id', 'parent_id']:
            if field in data:
                setattr(self, field, data[field])

    def is_liked_by(self, user):
        '''判断用户 user 是否已经对该评论点过赞'''
        return user in self.likers

    def liked_by(self, user):
        '''点赞'''
        if not self.is_liked_by(user):
            self.likers.append(user)

    def unliked_by(self, user):
        '''取消点赞'''
        if self.is_liked_by(user):
            self.likers.remove(user)


class Notification(db.Model):  # 不需要分页
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    timestamp = db.Column(db.Float, index=True, default=time)
    payload_json = db.Column(db.Text)

    def __repr__(self):
        return '<Notification {}>'.format(self.id)

    def get_data(self):
        return json.loads(str(self.payload_json))

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'user': {
                'id': self.user.id,
                'username': self.user.username,
                'name': self.user.name,
                'avatar': self.user.avatar(128)
            },
            'timestamp': self.timestamp,
            'payload': self.get_data(),
            '_links': {
                'self': url_for('api.get_notification', id=self.id),
                'user_url': url_for('api.get_user', id=self.user_id)
            }
        }
        return data

    def from_dict(self, data):
        for field in ['body', 'timestamp']:
            if field in data:
                setattr(self, field, data[field])


class Message(PaginatedAPIMixin, db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Message {}>'.format(self.id)

    def to_dict(self):
        data = {
            'id': self.id,
            'body': self.body,
            'timestamp': self.timestamp,
            'sender': self.sender.to_dict(),
            'recipient': self.recipient.to_dict(),
            '_links': {
                'self': url_for('api.get_message', id=self.id),
                'sender_url': url_for('api.get_user', id=self.sender_id),
                'recipient_url': url_for('api.get_user', id=self.recipient_id)
            }
        }
        return data

    def from_dict(self, data):
        for field in ['body', 'timestamp']:
            if field in data:
                setattr(self, field, data[field])


class Newhouse(PaginatedAPIMixin, db.Model):
    __tablename__ = 'newhouse'
    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String(64))
    city = db.Column(db.String(64))
    district = db.Column(db.String(64))
    name = db.Column(db.String(128))
    address = db.Column(db.String(128))
    origin_url = db.Column(db.String(64))
    area = db.Column(db.String(32))
    price = db.Column(db.Integer)
    sale = db.Column(db.String(32))


class Esf(PaginatedAPIMixin, db.Model):
    __tablename__ = 'esf'
    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String(64))
    city = db.Column(db.String(64))
    name = db.Column(db.String(128))
    rooms = db.Column(db.String(64))
    floor = db.Column(db.String(64))
    toward = db.Column(db.String(64))
    address = db.Column(db.String(128))
    origin_url = db.Column(db.String(64))
    area = db.Column(db.Float)
    price = db.Column(db.Integer)
    unit = db.Column(db.Integer)

class Info(PaginatedAPIMixin, db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String(64))
    city = db.Column(db.String(64))
    areaPrice = db.Column(db.String(128))
    esfareaPrice = db.Column(db.String(128))
    compareDate = db.Column(db.String(128))
    compareYear = db.Column(db.String(128))
    miniPrice = db.Column(db.Float)
    maxPrice = db.Column(db.Float)
    threeEsfareaPrice = db.Column(db.String(128))
    threeAreaPrice = db.Column(db.String(128))
    threeCompareDate = db.Column(db.String(128))
    threeCompareYear = db.Column(db.String(128))
    threeminPrice = db.Column(db.Float)
    threemaxPrice = db.Column(db.Float)
    buildPriceNameList = db.Column(db.String(128))
    buildPriceCount = db.Column(db.String(128))
    esfPriceNameList = db.Column(db.String(512))
    esfPriceCount = db.Column(db.String(128))
    domain = db.Column(db.String(128))
    new_avg  = db.Column(db.Float)
    esf_avg = db.Column(db.Float)
    new_cgreen = db.Column(db.String(64))
    esf_cgreen = db.Column(db.String(64))
    cid = db.Column(db.Integer)