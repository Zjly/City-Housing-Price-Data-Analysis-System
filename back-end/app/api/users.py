from datetime import datetime
from operator import itemgetter
import re
from flask import request, jsonify, url_for, g, current_app
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request, error_response
from app.extensions import db
from app.models import comments_likes, posts_likes, User, Post, Comment, Notification, Message,Permission
from app.utils.email import send_email
from app.utils.decorator import permission_required


@bp.route('/users/', methods=['POST'])
def create_user():
    '''注册一个新用户'''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')

    message = {}
    if 'username' not in data or not data.get('username', None).strip():
        message['username'] = 'Please provide a valid username.'
    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' not in data or not re.match(pattern, data.get('email', None)):
        message['email'] = 'Please provide a valid email address.'
    if 'password' not in data or not data.get('password', None).strip():
        message['password'] = 'Please provide a valid password.'

    if User.query.filter_by(username=data.get('username', None)).first():
        message['username'] = 'Please use a different username.'
    if User.query.filter_by(email=data.get('email', None)).first():
        message['email'] = 'Please use a different email address.'
    if message:
        return bad_request(message)

    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()

    # 发送确认账户的邮件
    token = user.generate_confirm_jwt()
    if not data.get('confirm_email_base_url'):
        confirm_url = 'http://127.0.0.1:5000/api/confirm/' + token
    else:
        confirm_url = data.get('confirm_email_base_url') + token

    text_body = '''
    Dear {},
    Welcome to HousePriceCloud!
    To confirm your account please click on the following link: {}
    Sincerely,
    The HousePriceCloud 28 Team
    Note: replies to this email address are not monitored.
    '''.format(user.username, confirm_url)

    html_body = '''
    <table class="responsive-table" width="600" border="0" cellpadding="0" cellspacing="0" align="center" valign="top" bgcolor="#002650" style="width: 600px; min-width: 600px; border-spacing: 0; border-collapse: collapse; margin: 0 auto; word-wrap: break-word; word-break: break-word; -ms-word-break: break-word; overflow-wrap: break-word; background-color: #002650;">
    <tbody><tr>
    <td class="body-text-section-padding-0px-15px-10px" style="padding: 0;" align="center">
    <table class="responsive-table" width="600" border="0" cellpadding="0" cellspacing="0">
    <tbody><tr>
    <td bgcolor="#002650">
    <table width="100%" cellspacing="0" cellpadding="0" border="0" style="width: 100%; min-width: 100%; border-spacing: 0; border-collapse: collapse; word-wrap: break-word; word-break: break-word; -ms-word-break: break-word; overflow-wrap: break-word;">
    <tbody><tr>
    <p></p>
    <br>
    <td class="body-text-padding-0px-5p-30px-font-12px-left" style="font-family: 'Open Sans', Frutiger, 'Frutiger Linotype', Univers, 'Helvetica Neue', Helvetica, Arial, 'Gill Sans', 'Gill Sans MT', 'Myriad Pro', Myriad, 'DejaVu Sans Condensed', 'Liberation Sans', 'Nimbus Sans L', 'Malgun Gothic', 'Microsoft YaHei', AppleSDGothicNeo, AppleGothic, Dotum, 'Microsoft JhengHei', 'Hiragino Kaku Gothic Pro', 'Hiragino Kaku Gothic ProN W3', Osaka, メイリオ, Meiryo, 'ＭＳ Ｐゴシック', Calibri, Geneva, Display, Tahoma, Verdana, sans-serif; font-size: 14px; font-weight: 300; line-height: 24px; text-align: left; padding: 0 40px 40px; color: #bbbbbb;">
    <table id="" class="" style="" border="0" cellpadding="0" cellspacing="0" width="100%" height=""><tbody><tr><td style="font-family: 'Open Sans', Frutiger, 'Frutiger Linotype', Univers, 'Helvetica Neue', Helvetica, Arial, 'Gill Sans', 'Gill Sans MT', 'Myriad Pro', Myriad, 'DejaVu Sans Condensed', 'Liberation Sans', 'Nimbus Sans L', 'Malgun Gothic', 'Microsoft YaHei', AppleSDGothicNeo, AppleGothic, Dotum, 'Microsoft JhengHei', 'Hiragino Kaku Gothic Pro', 'Hiragino Kaku Gothic ProN W3', Osaka, メイリオ, Meiryo, 'ＭＳ Ｐゴシック', Calibri, Geneva, Display, Tahoma, Verdana, sans-serif;font-weight: 300; font-size: 24px; color: #FFFFFF; line-height: 32px;">点击以下按钮验证账号：</td></tr></tbody></table>
    <p style="text-align: center;margin: 30px auto;"><a href="{1}" target="_blank" style="display: inline-block;width: 120px;line-height: 26px;height: 26px;padding: 10px;background-color: #f55d54;color: white;text-align: center;font-size: 16px;text-decoration: none;" rel="noopener">验证账号</a></p>
    <p style=""> {0}，您好！
    </p>
    <p style=""> 我们收到了来自您的房价云的账号验证请求。请使用上面的按钮验证您的账号。
    </p>
    <p>如果按钮无效请点击<b><a href="{1}">{1}</a></b></p>
    <p style=""> <i><b>请注意：</b>该验证地址将在10分钟后过期，请尽快使用！</i>
    </p>
    <p style="">享受您在房价云的浏览！<br>
    房价云客服团队</p>
    </td>
    </tr>
    </tbody></table>
    </td>
    </tr>
    </tbody></table>
    </td>
    </tr>
    </tbody></table>
    '''.format(user.username, confirm_url)

    send_email('[HousePriceCloud] Confirm Your Account',
               sender=current_app.config['MAIL_SENDER'],
               recipients=[user.email],
               text_body=text_body,
               html_body=html_body)

    response = jsonify(user.to_dict())
    response.status_code = 201
    # HTTP协议要求201响应包含一个值为新资源URL的Location头部
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response


@bp.route('/users/', methods=['GET'])
@token_auth.login_required
def get_users():
    '''返回用户集合，分页'''
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['USERS_PER_PAGE'], type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)


@bp.route('/users/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    '''返回一个用户'''
    user = User.query.get_or_404(id)
    if g.current_user == user:
        return jsonify(user.to_dict(include_email=True))
    # 如果是查询其它用户，添加 是否已关注过该用户 的标志位
    data = user.to_dict()
    data['is_following'] = g.current_user.is_following(user)
    return jsonify(data)


@bp.route('/users/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_user(id):
    '''修改一个用户'''
    user = User.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')

    message = {}
    if 'username' in data and not data.get('username', None).strip():
        message['username'] = 'Please provide a valid username.'

    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' in data and not re.match(pattern, data.get('email', None)):
        message['email'] = 'Please provide a valid email address.'

    if 'username' in data and data['username'] != user.username and \
            User.query.filter_by(username=data['username']).first():
        message['username'] = 'Please use a different username.'
    if 'email' in data and data['email'] != user.email and \
            User.query.filter_by(email=data['email']).first():
        message['email'] = 'Please use a different email address.'

    if message:
        return bad_request(message)

    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())


@bp.route('/users/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_user(id):
    '''删除一个用户'''
    user = User.query.get_or_404(id)
    if g.current_user != user and not g.current_user.can(Permission.ADMIN):
        return error_response(403)
    db.session.delete(user)
    db.session.commit()
    return '', 204


@bp.route('/users/<int:id>/notifications/', methods=['GET'])
@token_auth.login_required
def get_user_notifications(id):
    '''返回该用户的新通知'''
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)
    # 只返回上次看到的通知以来发生的新通知
    # 比如用户在 10:00:00 请求一次该API，在 10:00:10 再次请求该API只会返回 10:00:00 之后产生的新通知
    since = request.args.get('since', 0.0, type=float)
    notifications = user.notifications.filter(
        Notification.timestamp > since).order_by(Notification.timestamp.asc())
    return jsonify([n.to_dict() for n in notifications])


###
# 关注 / 取消关注
###
@bp.route('/follow/<int:id>', methods=['GET'])
@token_auth.login_required
@permission_required(Permission.FOLLOW)
def follow(id):
    '''开始关注一个用户'''
    user = User.query.get_or_404(id)
    if g.current_user == user:
        return bad_request('You cannot follow yourself.')
    if g.current_user.is_following(user):
        return bad_request('You have already followed that user.')
    g.current_user.follow(user)
    # 给该用户发送新粉丝通知
    user.add_notification('unread_follows_count', user.new_follows())
    db.session.commit()
    return jsonify({
        'status': 'success',
        'message': 'You are now following %s.' % (user.name if user.name else user.username)
    })


@bp.route('/unfollow/<int:id>', methods=['GET'])
@token_auth.login_required
@permission_required(Permission.FOLLOW)
def unfollow(id):
    '''取消关注一个用户'''
    user = User.query.get_or_404(id)
    if g.current_user == user:
        return bad_request('You cannot unfollow yourself.')
    if not g.current_user.is_following(user):
        return bad_request('You are not following this user.')
    g.current_user.unfollow(user)
    # 给该用户发送新粉丝通知(需要自动减1)
    user.add_notification('unread_follows_count', user.new_follows())
    db.session.commit()
    return jsonify({
        'status': 'success',
        'message': 'You are not following %s anymore.' % (user.name if user.name else user.username)
    })


###
# 用户关注了谁、用户的粉丝
###
@bp.route('/users/<int:id>/followeds/', methods=['GET'])
@token_auth.login_required
def get_followeds(id):
    '''返回用户已关注的人的列表'''
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['USERS_PER_PAGE'], type=int), 100)
    data = User.to_collection_dict(
        user.followeds, page, per_page, 'api.get_followeds', id=id)
    # 为每个 followed 添加 is_following 标志位
    for item in data['items']:
        item['is_following'] = g.current_user.is_following(
            User.query.get(item['id']))
        # 获取用户开始关注 followed 的时间
        res = db.engine.execute(
            "select * from followers where follower_id={} and followed_id={}".
            format(user.id, item['id']))
        item['timestamp'] = datetime.strptime(
            str(list(res)[0][2]), '%Y-%m-%d %H:%M:%S')
    # 按 timestamp 排序一个字典列表(倒序，最新关注的人在最前面)
    data['items'] = sorted(data['items'], key=itemgetter('timestamp'), reverse=True)
    return jsonify(data)


@bp.route('/users/<int:id>/followers/', methods=['GET'])
@token_auth.login_required
def get_followers(id):
    '''返回用户的粉丝列表'''
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['USERS_PER_PAGE'], type=int), 100)
    data = User.to_collection_dict(
        user.followers, page, per_page, 'api.get_followers', id=id)
    # 为每个 follower 添加 is_following 标志位
    for item in data['items']:
        item['is_following'] = g.current_user.is_following(
            User.query.get(item['id']))
        # 获取 follower 开始关注该用户的时间
        res = db.engine.execute(
            "select * from followers where follower_id={} and followed_id={}".
            format(item['id'], user.id))
        item['timestamp'] = datetime.strptime(
            str(list(res)[0][2]), '%Y-%m-%d %H:%M:%S')
    # 按 timestamp 排序一个字典列表(倒序，最新的粉丝在最前面)
    data['items'] = sorted(data['items'], key=itemgetter('timestamp'), reverse=True)
    # 标记哪些粉丝是新的
    last_read_time = user.last_follows_read_time or datetime(1900, 1, 1)
    for item in data['items']:
        if item['timestamp'] > last_read_time:
            item['is_new'] = True
    # 更新 last_follows_read_time 属性值
    user.last_follows_read_time = datetime.utcnow()
    # 将新粉丝通知的计数归零
    user.add_notification('unread_follows_count', 0)
    db.session.commit()
    return jsonify(data)


###
# 与用户资源相关的资源
##
@bp.route('/users/<int:id>/posts/', methods=['GET'])
@token_auth.login_required
def get_user_posts(id):
    '''返回该用户的所有文章列表'''
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['POSTS_PER_PAGE'], type=int), 100)
    data = Post.to_collection_dict(
        user.posts.order_by(Post.timestamp.desc()), page, per_page,
        'api.get_user_posts', id=id)
    return jsonify(data)


@bp.route('/users/<int:id>/liked-posts/', methods=['GET'])
@token_auth.login_required
def get_user_liked_posts(id):
    '''返回该用户喜欢别人的文章列表'''
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['POSTS_PER_PAGE'], type=int), 100)
    data = Post.to_collection_dict(
        user.liked_posts.order_by(Post.timestamp.desc()), page, per_page,
        'api.get_user_liked_posts', id=id)
    return jsonify(data)


@bp.route('/users/<int:id>/followeds-posts/', methods=['GET'])
@token_auth.login_required
def get_user_followeds_posts(id):
    '''返回该用户所关注的大神的所有博客文章列表'''
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['POSTS_PER_PAGE'], type=int), 100)
    data = Post.to_collection_dict(
        user.followeds_posts().order_by(Post.timestamp.desc()), page, per_page,
        'api.get_user_followeds_posts', id=id)
    # 标记哪些文章是新的
    last_read_time = user.last_followeds_posts_read_time or datetime(1900, 1, 1)
    for item in data['items']:
        if item['timestamp'] > last_read_time:
            item['is_new'] = True
    # 更新 last_followeds_posts_read_time 属性值
    user.last_followeds_posts_read_time = datetime.utcnow()
    # 将新文章通知的计数归零
    user.add_notification('unread_followeds_posts_count', 0)
    db.session.commit()
    return jsonify(data)


@bp.route('/users/<int:id>/comments/', methods=['GET'])
@token_auth.login_required
def get_user_comments(id):
    '''返回该用户发表过的所有评论列表'''
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['COMMENTS_PER_PAGE'], type=int), 100)
    data = Comment.to_collection_dict(
        user.comments.order_by(Comment.timestamp.desc()), page, per_page,
        'api.get_user_comments', id=id)
    return jsonify(data)


@bp.route('/users/<int:id>/recived-comments/', methods=['GET'])
@token_auth.login_required
def get_user_recived_comments(id):
    '''返回该用户收到的所有评论'''
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['COMMENTS_PER_PAGE'], type=int), 100)
    # 用户发布的所有文章ID集合
    user_posts_ids = [post.id for post in user.posts.all()]
    # 用户文章下面的新评论, 即评论的 post_id 在 user_posts_ids 集合中，且评论的 author 不是自己(文章的作者)
    q1 = Comment.query.filter(Comment.post_id.in_(user_posts_ids), Comment.author != user)
    # 用户发表的评论被人回复了
    descendants = set()
    for c in user.comments:
        descendants = descendants | c.get_descendants()
    descendants = descendants - set(user.comments.all())  # 除去自己在底下回复的
    descendants_ids = [c.id for c in descendants]
    q2 = Comment.query.filter(Comment.id.in_(descendants_ids))
    # 按时间倒序排列构成用户收到的所有评论
    recived_comments = q1.union(q2).order_by(Comment.mark_read, Comment.timestamp.desc())
    # 分页后的 JSON 数据
    data = Comment.to_collection_dict(recived_comments, page, per_page, 'api.get_user_recived_comments', id=id)
    # 标记哪些评论是新的
    last_read_time = user.last_recived_comments_read_time or datetime(1900, 1, 1)
    for item in data['items']:
        if item['timestamp'] > last_read_time:
            item['is_new'] = True
    # 更新 last_recived_comments_read_time 属性值
    user.last_recived_comments_read_time = datetime.utcnow()
    # 将新评论通知的计数归零
    user.add_notification('unread_recived_comments_count', 0)
    db.session.commit()
    return jsonify(data)


@bp.route('/users/<int:id>/recived-comments-likes/', methods=['GET'])
@token_auth.login_required
def get_user_recived_comments_likes(id):
    '''返回该用户收到的评论赞'''
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['COMMENTS_PER_PAGE'], type=int), 100)
    # 用户哪些评论被点赞了，分页
    comments = user.comments.join(comments_likes).paginate(page, per_page)
    # 点赞记录
    records = {
        'items': [],
        '_meta': {
            'page': page,
            'per_page': per_page,
            'total_pages': comments.pages,
            'total_items': comments.total
        },
        '_links': {
            'self': url_for('api.get_user_recived_comments_likes', page=page, per_page=per_page, id=id),
            'next': url_for('api.get_user_recived_comments_likes', page=page + 1, per_page=per_page, id=id) if comments.has_next else None,
            'prev': url_for('api.get_user_recived_comments_likes', page=page - 1, per_page=per_page, id=id) if comments.has_prev else None
        }
    }
    for c in comments.items:
        # 重组数据，变成: (谁) (什么时间) 点赞了你的 (哪条评论)
        for u in c.likers:
            if u != user:  # 用户自己点赞自己的评论不需要被通知
                data = {}
                data['user'] = u.to_dict()
                data['comment'] = c.to_dict()
                # 获取点赞时间
                res = db.engine.execute("select * from comments_likes where user_id={} and comment_id={}".format(u.id, c.id))
                data['timestamp'] = datetime.strptime(str(list(res)[0][2]), '%Y-%m-%d %H:%M:%S')
                # 标记本条点赞记录是否为新的
                last_read_time = user.last_comments_likes_read_time or datetime(1900, 1, 1)
                if data['timestamp'] > last_read_time:
                    data['is_new'] = True
                records['items'].append(data)
    # 按 timestamp 排序一个字典列表(倒序，最新点赞的人在最前面)
    records['items'] = sorted(records['items'], key=itemgetter('timestamp'), reverse=True)
    # 更新 last_comments_likes_read_time 属性值
    user.last_comments_likes_read_time = datetime.utcnow()
    # 将新点赞通知的计数归零
    user.add_notification('unread_comments_likes_count', 0)
    db.session.commit()
    return jsonify(records)


@bp.route('/users/<int:id>/recived-posts-likes/', methods=['GET'])
@token_auth.login_required
def get_user_recived_posts_likes(id):
    '''返回该用户收到的文章喜欢'''
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['POSTS_PER_PAGE'], type=int), 100)
    # 用户哪些文章被喜欢/收藏了，分页
    posts = user.posts.join(posts_likes).paginate(page, per_page)
    # 喜欢记录
    records = {
        'items': [],
        '_meta': {
            'page': page,
            'per_page': per_page,
            'total_pages': posts.pages,
            'total_items': posts.total
        },
        '_links': {
            'self': url_for('api.get_user_recived_posts_likes', page=page, per_page=per_page, id=id),
            'next': url_for('api.get_user_recived_posts_likes', page=page + 1, per_page=per_page, id=id) if posts.has_next else None,
            'prev': url_for('api.get_user_recived_posts_likes', page=page - 1, per_page=per_page, id=id) if posts.has_prev else None
        }
    }
    for p in posts.items:
        # 重组数据，变成: (谁) (什么时间) 喜欢了你的 (哪篇文章)
        for u in p.likers:
            if u != user:  # 用户自己喜欢自己的文章不需要被通知
                data = {}
                data['user'] = u.to_dict()
                data['post'] = p.to_dict()
                # 获取喜欢时间
                res = db.engine.execute("select * from posts_likes where user_id={} and post_id={}".format(u.id, p.id))
                data['timestamp'] = datetime.strptime(str(list(res)[0][2]), '%Y-%m-%d %H:%M:%S')
                # 标记本条喜欢记录是否为新的
                last_read_time = user.last_posts_likes_read_time or datetime(1900, 1, 1)
                if data['timestamp'] > last_read_time:
                    data['is_new'] = True
                records['items'].append(data)
    # 按 timestamp 排序一个字典列表(倒序，最新喜欢的人在最前面)
    records['items'] = sorted(records['items'], key=itemgetter('timestamp'), reverse=True)
    # 更新 last_posts_likes_read_time 属性值
    user.last_posts_likes_read_time = datetime.utcnow()
    # 将新喜欢通知的计数归零
    user.add_notification('unread_posts_likes_count', 0)
    db.session.commit()
    return jsonify(records)


@bp.route('/users/<int:id>/messages-recipients/', methods=['GET'])
@token_auth.login_required
def get_user_messages_recipients(id):
    '''我给哪些用户发过私信，按用户分组，返回我给各用户最后一次发送的私信
    即: 我给 (谁) 最后一次 发了 (什么私信)'''
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['MESSAGES_PER_PAGE'], type=int), 100)
    data = Message.to_collection_dict(
        user.messages_sent.group_by(Message.recipient_id).order_by(Message.timestamp.desc()), page, per_page,
        'api.get_user_messages_recipients', id=id)
    # 我给每个用户发的私信，他们有没有未读的
    for item in data['items']:
        # 发给了谁
        recipient = User.query.get(item['recipient']['id'])
        # 总共给他发过多少条
        item['total_count'] = user.messages_sent.filter_by(recipient_id=item['recipient']['id']).count()
        # 他最后一次查看收到的私信的时间
        last_read_time = recipient.last_messages_read_time or datetime(1900, 1, 1)
        # item 是发给他的最后一条，如果最后一条不是新的，肯定就没有啦
        if item['timestamp'] > last_read_time:
            item['is_new'] = True
            # 继续获取发给这个用户的私信有几条是新的
            item['new_count'] = user.messages_sent.filter_by(recipient_id=item['recipient']['id']).filter(Message.timestamp > last_read_time).count()
    return jsonify(data)


@bp.route('/users/<int:id>/messages-senders/', methods=['GET'])
@token_auth.login_required
def get_user_messages_senders(id):
    '''哪些用户给我发过私信，按用户分组，返回各用户最后一次发送的私信
    即: (谁) 最后一次 给我发了 (什么私信)'''
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['MESSAGES_PER_PAGE'], type=int), 100)
    data = Message.to_collection_dict(
        user.messages_received.group_by(Message.sender_id).order_by(Message.timestamp.desc()), page, per_page,
        'api.get_user_messages_senders', id=id)
    # 这个用户发给我的私信有没有新的
    last_read_time = user.last_messages_read_time or datetime(1900, 1, 1)
    new_items = []  # 最后一条是新的
    not_new_items = []  # 最后一条不是新的
    for item in data['items']:
        # 判断我有没有拉黑他
        if user.is_blocking(User.query.get(item['sender']['id'])):
            item['is_blocking'] = True
        # item 是他发的最后一条，如果最后一条不是新的，肯定就没有啦
        if item['timestamp'] > last_read_time:
            item['is_new'] = True
            # 继续获取这个用户发的私信有几条是新的
            item['new_count'] = user.messages_received.filter_by(sender_id=item['sender']['id']).filter(Message.timestamp > last_read_time).count()
            new_items.append(item)
        else:
            not_new_items.append(item)
    # 对那些最后一条是新的按 timestamp 正序排序，不然用户更新 last_messages_read_time 会导致时间靠前的全部被标记已读
    new_items = sorted(new_items, key=itemgetter('timestamp'))
    data['items'] = new_items + not_new_items
    return jsonify(data)


@bp.route('/users/<int:id>/history-messages/', methods=['GET'])
@token_auth.login_required
def get_user_history_messages(id):
    '''返回我与某个用户(由查询参数 from 获取)之间的所有私信记录'''
    user = User.query.get_or_404(id)
    if g.current_user != user:
        return error_response(403)
    page = request.args.get('page', 1, type=int)
    per_page = min(
        request.args.get(
            'per_page', current_app.config['MESSAGES_PER_PAGE'], type=int), 100)
    from_id = request.args.get('from', type=int)
    if not from_id:  # 必须提供聊天的对方用户的ID
        return bad_request('You must provide the user id of opposite site.')
    # 对方发给我的
    q1 = Message.query.filter(Message.sender_id == from_id, Message.recipient_id == id)
    # 我发给对方的
    q2 = Message.query.filter(Message.sender_id == id, Message.recipient_id == from_id)
    # 按时间正序排列构成完整的对话时间线
    history_messages = q1.union(q2).order_by(Message.timestamp)
    data = Message.to_collection_dict(history_messages, page, per_page, 'api.get_user_history_messages', id=id)
    # 现在这一页的 data['items'] 包含对方发给我和我发给对方的
    # 需要创建一个新列表，只包含对方发给我的，用来查看哪些私信是新的
    recived_messages = [item for item in data['items'] if item['sender']['id'] != id]
    sent_messages = [item for item in data['items'] if item['sender']['id'] == id]
    # 然后，标记哪些私信是新的
    last_read_time = user.last_messages_read_time or datetime(1900, 1, 1)
    new_count = 0
    for item in recived_messages:
        if item['timestamp'] > last_read_time:
            item['is_new'] = True
            new_count += 1
    if new_count > 0:
        # 更新 last_messages_read_time 属性值为收到的私信列表最后一条(最近的)的时间
        user.last_messages_read_time = recived_messages[-1]['timestamp']
        db.session.commit()  # 先提交数据库，这样 user.new_recived_messages() 才会变化
        # 更新用户的新私信通知的计数
        user.add_notification('unread_messages_count', user.new_recived_messages())
        db.session.commit()
    # 最后，重新组合 data['items']，因为收到的新私信添加了 is_new 标记
    messages = recived_messages + sent_messages
    messages.sort(key=data['items'].index)  # 保持 messages 列表元素的顺序跟 data['items'] 一样
    data['items'] = messages
    return jsonify(data)


###
# 拉黑 / 取消拉黑
###
@bp.route('/block/<int:id>', methods=['GET'])
@token_auth.login_required
@permission_required(Permission.FOLLOW)
def block(id):
    '''开始拉黑一个用户'''
    user = User.query.get_or_404(id)
    if g.current_user == user:
        return bad_request('You cannot block yourself.')
    if g.current_user.is_blocking(user):
        return bad_request('You have already blocked that user.')
    g.current_user.block(user)
    db.session.commit()
    return jsonify({
        'status': 'success',
        'message': 'You are now blocking %s.' % (user.name if user.name else user.username)
    })


@bp.route('/unblock/<int:id>', methods=['GET'])
@token_auth.login_required
@permission_required(Permission.FOLLOW)
def unblock(id):
    '''取消拉黑一个用户'''
    user = User.query.get_or_404(id)
    if g.current_user == user:
        return bad_request('You cannot unblock yourself.')
    if not g.current_user.is_blocking(user):
        return bad_request('You are not blocking this user.')
    g.current_user.unblock(user)
    db.session.commit()
    return jsonify({
        'status': 'success',
        'message': 'You are not blocking %s anymore.' % (user.name if user.name else user.username)
    })


@bp.route('/resend-confirm', methods=['POST'])
@token_auth.login_required
def resend_confirmation():
    '''重新发送确认账户的邮件'''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'confirm_email_base_url' not in data or not data.get('confirm_email_base_url').strip():
        return bad_request('Please provide a valid confirm email base url.')

    token = g.current_user.generate_confirm_jwt()

    text_body = '''
    Dear {},
    Welcome to HousePriceCloud!
    To confirm your account please click on the following link: {}
    Sincerely,
    The HousePriceCloud 28 Team
    Note: replies to this email address are not monitored.
    '''.format(g.current_user.username, data.get('confirm_email_base_url') + token)

    html_body = '''
    <table class="responsive-table" width="600" border="0" cellpadding="0" cellspacing="0" align="center" valign="top" bgcolor="#002650" style="width: 600px; min-width: 600px; border-spacing: 0; border-collapse: collapse; margin: 0 auto; word-wrap: break-word; word-break: break-word; -ms-word-break: break-word; overflow-wrap: break-word; background-color: #002650;">
    <tbody><tr>
    <td class="body-text-section-padding-0px-15px-10px" style="padding: 0;" align="center">
    <table class="responsive-table" width="600" border="0" cellpadding="0" cellspacing="0">
    <tbody><tr>
    <td bgcolor="#002650">
    <table width="100%" cellspacing="0" cellpadding="0" border="0" style="width: 100%; min-width: 100%; border-spacing: 0; border-collapse: collapse; word-wrap: break-word; word-break: break-word; -ms-word-break: break-word; overflow-wrap: break-word;">
    <tbody><tr>
    <p></p>
    <br>
    <td class="body-text-padding-0px-5p-30px-font-12px-left" style="font-family: 'Open Sans', Frutiger, 'Frutiger Linotype', Univers, 'Helvetica Neue', Helvetica, Arial, 'Gill Sans', 'Gill Sans MT', 'Myriad Pro', Myriad, 'DejaVu Sans Condensed', 'Liberation Sans', 'Nimbus Sans L', 'Malgun Gothic', 'Microsoft YaHei', AppleSDGothicNeo, AppleGothic, Dotum, 'Microsoft JhengHei', 'Hiragino Kaku Gothic Pro', 'Hiragino Kaku Gothic ProN W3', Osaka, メイリオ, Meiryo, 'ＭＳ Ｐゴシック', Calibri, Geneva, Display, Tahoma, Verdana, sans-serif; font-size: 14px; font-weight: 300; line-height: 24px; text-align: left; padding: 0 40px 40px; color: #bbbbbb;">
    <table id="" class="" style="" border="0" cellpadding="0" cellspacing="0" width="100%" height=""><tbody><tr><td style="font-family: 'Open Sans', Frutiger, 'Frutiger Linotype', Univers, 'Helvetica Neue', Helvetica, Arial, 'Gill Sans', 'Gill Sans MT', 'Myriad Pro', Myriad, 'DejaVu Sans Condensed', 'Liberation Sans', 'Nimbus Sans L', 'Malgun Gothic', 'Microsoft YaHei', AppleSDGothicNeo, AppleGothic, Dotum, 'Microsoft JhengHei', 'Hiragino Kaku Gothic Pro', 'Hiragino Kaku Gothic ProN W3', Osaka, メイリオ, Meiryo, 'ＭＳ Ｐゴシック', Calibri, Geneva, Display, Tahoma, Verdana, sans-serif;font-weight: 300; font-size: 24px; color: #FFFFFF; line-height: 32px;">点击以下按钮验证账号：</td></tr></tbody></table>
    <p style="text-align: center;margin: 30px auto;"><a href="{1}" target="_blank" style="display: inline-block;width: 120px;line-height: 26px;height: 26px;padding: 10px;background-color: #f55d54;color: white;text-align: center;font-size: 16px;text-decoration: none;" rel="noopener">验证账号</a></p>
    <p style=""> {0}，您好！
    </p>
    <p style=""> 我们收到了来自您的房价云的账号验证请求。请使用上面的按钮验证您的账号。
    </p>
    <p>如果按钮无效请点击<b><a href="{1}">{1}</a></b></p>
    <p style=""> <i><b>请注意：</b>该验证地址将在10分钟后过期，请尽快使用！</i>
    </p>
    <p style="">享受您在房价云的浏览！<br>
    房价云客服团队</p>
    </td>
    </tr>
    </tbody></table>
    </td>
    </tr>
    </tbody></table>
    </td>
    </tr>
    </tbody></table>
    '''.format(g.current_user.username, data.get('confirm_email_base_url') + token)

    send_email('[HousePriceCloud] Confirm Your Account',
               sender=current_app.config['MAIL_SENDER'],
               recipients=[g.current_user.email],
               text_body=text_body,
               html_body=html_body)
    return jsonify({
        'status': 'success',
        'message': 'A new confirmation email has been sent to you by email.'
    })


@bp.route('/confirm/<token>', methods=['GET'])
@token_auth.login_required
def confirm(token):
    '''用户收到验证邮件后，验证其账户'''
    if g.current_user.confirmed:
        return bad_request('You have already confirmed your account.')
    if g.current_user.verify_confirm_jwt(token):
        g.current_user.ping()
        db.session.commit()
        # 给用户发放新 JWT，因为要包含 confirmed: true
        token = g.current_user.get_jwt()
        return jsonify({
            'status': 'success',
            'message': 'You have confirmed your account. Thanks!',
            'token': token
        })
    else:
        return bad_request('The confirmation link is invalid or has expired.')


@bp.route('/reset-password-request', methods=['POST'])
def reset_password_request():
    '''请求重置账户密码，需要提供注册时填写的邮箱地址'''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')

    message = {}
    if 'confirm_email_base_url' not in data or not data.get('confirm_email_base_url').strip():
        message['confirm_email_base_url'] = 'Please provide a valid confirm email base url.'
    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' not in data or not re.match(pattern, data.get('email', None)):
        message['email'] = 'Please provide a valid email address.'
    if message:
        return bad_request(message)

    user = User.query.filter_by(email=data.get('email')).first()
    if user:  # 如果提供的邮箱地址对应的用户实例对象存在，就发邮件
        token = user.generate_reset_password_jwt()

        text_body = '''
        Dear {0},
        To reset your password click on the following link: {1}
        If you have not requested a password reset simply ignore this message.
        Sincerely,
        The HousePriceCloud 28 Team
        Note: replies to this email address are not monitored.
        '''.format(user.username, data.get('confirm_email_base_url') + token)

        html_body = '''
        <table class="responsive-table" width="600" border="0" cellpadding="0" cellspacing="0" align="center" valign="top" bgcolor="#002650" style="width: 600px; min-width: 600px; border-spacing: 0; border-collapse: collapse; margin: 0 auto; word-wrap: break-word; word-break: break-word; -ms-word-break: break-word; overflow-wrap: break-word; background-color: #002650;">
        <tbody><tr>
        <td class="body-text-section-padding-0px-15px-10px" style="padding: 0;" align="center">
        <table class="responsive-table" width="600" border="0" cellpadding="0" cellspacing="0">
        <tbody><tr>
        <td bgcolor="#002650">
        <table width="100%" cellspacing="0" cellpadding="0" border="0" style="width: 100%; min-width: 100%; border-spacing: 0; border-collapse: collapse; word-wrap: break-word; word-break: break-word; -ms-word-break: break-word; overflow-wrap: break-word;">
        <tbody><tr>
        <p></p>
        <br>
        <td class="body-text-padding-0px-5p-30px-font-12px-left" style="font-family: 'Open Sans', Frutiger, 'Frutiger Linotype', Univers, 'Helvetica Neue', Helvetica, Arial, 'Gill Sans', 'Gill Sans MT', 'Myriad Pro', Myriad, 'DejaVu Sans Condensed', 'Liberation Sans', 'Nimbus Sans L', 'Malgun Gothic', 'Microsoft YaHei', AppleSDGothicNeo, AppleGothic, Dotum, 'Microsoft JhengHei', 'Hiragino Kaku Gothic Pro', 'Hiragino Kaku Gothic ProN W3', Osaka, メイリオ, Meiryo, 'ＭＳ Ｐゴシック', Calibri, Geneva, Display, Tahoma, Verdana, sans-serif; font-size: 14px; font-weight: 300; line-height: 24px; text-align: left; padding: 0 40px 40px; color: #bbbbbb;">
        <table id="" class="" style="" border="0" cellpadding="0" cellspacing="0" width="100%" height=""><tbody><tr><td style="font-family: 'Open Sans', Frutiger, 'Frutiger Linotype', Univers, 'Helvetica Neue', Helvetica, Arial, 'Gill Sans', 'Gill Sans MT', 'Myriad Pro', Myriad, 'DejaVu Sans Condensed', 'Liberation Sans', 'Nimbus Sans L', 'Malgun Gothic', 'Microsoft YaHei', AppleSDGothicNeo, AppleGothic, Dotum, 'Microsoft JhengHei', 'Hiragino Kaku Gothic Pro', 'Hiragino Kaku Gothic ProN W3', Osaka, メイリオ, Meiryo, 'ＭＳ Ｐゴシック', Calibri, Geneva, Display, Tahoma, Verdana, sans-serif;font-weight: 300; font-size: 24px; color: #FFFFFF; line-height: 32px;">点击以下按钮重置密码：</td></tr></tbody></table>
        <p style="text-align: center;margin: 30px auto;"><a href="{1}" target="_blank" style="display: inline-block;width: 120px;line-height: 26px;height: 26px;padding: 10px;background-color: #f55d54;color: white;text-align: center;font-size: 16px;text-decoration: none;" rel="noopener">重置密码</a></p>
        <p style=""> {0}，您好！
        </p>
        <p style=""> 我们收到了来自您的房价云的密码重置请求。请使用上面的按钮重置您的账号密码。
        </p>
        <p>如果按钮无效请点击<b><a href="{1}">{1}</a></b></p>
        <p style=""> <i><b>请注意：</b>该验证地址将在10分钟后过期，请尽快使用！</i>
        </p>
        <p style="">享受您在房价云的浏览！<br>
        房价云客服团队</p>
        </td>
        </tr>
        </tbody></table>
        </td>
        </tr>
        </tbody></table>
        </td>
        </tr>
        </tbody></table>
        '''.format(user.username, data.get('confirm_email_base_url') + token)

        send_email('[HousePriceCloud] Reset Your Password',
                   sender=current_app.config['MAIL_SENDER'],
                   recipients=[user.email],
                   text_body=text_body,
                   html_body=html_body)
    # 不管前端提供的邮箱地址有没有对应的用户实例(不排除有人想恶意重置别人的账户)，都给他回应
    return jsonify({
        'status': 'success',
        'message': 'An email with instructions to reset your password has been sent to you.'
    })


@bp.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    '''用户点击邮件中的链接，通过验证 JWT 来重置对应的账户的密码'''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')
    if 'password' not in data or not data.get('password', None).strip():
        return bad_request('Please provide a valid password.')
    user = User.verify_reset_password_jwt(token)
    if not user:
        return bad_request('The reset password link is invalid or has expired.')
    user.set_password(data.get('password'))
    db.session.commit()
    return jsonify({
        'status': 'success',
        'message': 'Your password has been reset.'
    })


@bp.route('/update-password', methods=['POST'])
@token_auth.login_required
def update_password():
    '''已登录的用户更新自己的密码'''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')

    if 'old_password' not in data or not data.get('old_password', None).strip():
        return bad_request('Please provide a valid old password.')
    if 'new_password' not in data or not data.get('new_password', None).strip():
        return bad_request('Please provide a valid new password.')
    if data.get('old_password') == data.get('new_password'):
        return bad_request('The new password is equal to the old password.')
    # 验证旧密码
    if not g.current_user.check_password(data.get('old_password')):
        return bad_request('The old password is wrong.')
    g.current_user.set_password(data.get('new_password'))
    db.session.commit()
    return jsonify({
        'status': 'success',
        'message': 'Your password has been updated.'
    })