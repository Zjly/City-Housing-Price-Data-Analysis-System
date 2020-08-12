from flask import request, url_for, jsonify
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request
from app.extensions import db
from app.models import Role
from app.utils.decorator import admin_required


@bp.route('/roles/perms', methods=['GET'])
def get_perms():
    '''获取所有Permissions'''
    data = [
        {'name': 'FOLLOW', 'dec': 1},
        {'name': 'COMMENT', 'dec': 2},
        {'name': 'WRITE', 'dec': 4},
        {'name': 'ADMIN', 'dec': 128}
    ]
    return jsonify(data)


@bp.route('/roles', methods=['POST'])
@token_auth.login_required
@admin_required
def create_role():
    '''注册一个新角色'''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')

    message = {}
    if 'slug' not in data or not data.get('slug', None).strip():
        message['slug'] = 'Please provide a valid slug.'
    if 'name' not in data or not data.get('name', None).strip():
        message['name'] = 'Please provide a valid name.'

    if Role.query.filter_by(slug=data.get('slug', None)).first():
        message['slug'] = 'Please use a different slug.'
    if message:
        return bad_request(message)

    permissions = 0
    for perm in data.get('permissions', 0):
        permissions += perm
    data['permissions'] = permissions

    role = Role()
    role.from_dict(data)
    db.session.add(role)
    db.session.commit()

    response = jsonify(role.to_dict())
    response.status_code = 201
    # HTTP协议要求201响应包含一个值为新资源URL的Location头部
    response.headers['Location'] = url_for('api.get_role', id=role.id)
    return response


@bp.route('/roles', methods=['GET'])
@token_auth.login_required
@admin_required
def get_roles():
    '''返回所有角色的集合'''
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Role.to_collection_dict(Role.query, page, per_page, 'api.get_roles')
    return jsonify(data)


@bp.route('/roles/<int:id>', methods=['GET'])
@token_auth.login_required
@admin_required
def get_role(id):
    '''返回一个角色'''
    role = Role.query.get_or_404(id)
    data = role.to_dict()

    # 当前角色已拥有的操作权限列表(整数列表)
    choices = [
        {'name': 'FOLLOW', 'dec': 1},
        {'name': 'COMMENT', 'dec': 2},
        {'name': 'WRITE', 'dec': 4},
        {'name': 'ADMIN', 'dec': 128}
    ]
    new_choices = filter(lambda x: role.has_permission(x['dec']), choices)
    data['perms'] = [x['dec'] for x in new_choices]
    return jsonify(data)


@bp.route('/roles/<int:id>', methods=['PUT'])
@token_auth.login_required
@admin_required
def update_role(id):
    '''修改一个角色'''
    role = Role.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')

    message = {}
    if 'slug' not in data or not data.get('slug', None).strip():
        message['slug'] = 'Please provide a valid slug.'
    if 'name' not in data or not data.get('name', None).strip():
        message['name'] = 'Please provide a valid name.'

    r = Role.query.filter_by(slug=data.get('slug', None)).first()
    if r and r.id != role.id:
        message['slug'] = 'Please use a different slug.'
    if message:
        return bad_request(message)

    permissions = 0
    for perm in data.get('permissions', 0):
        permissions += perm
    data['permissions'] = permissions

    role.from_dict(data)
    db.session.commit()
    return jsonify(role.to_dict())


@bp.route('/roles/<int:id>', methods=['DELETE'])
@token_auth.login_required
@admin_required
def delete_role(id):
    '''删除一个角色'''
    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    return '', 204