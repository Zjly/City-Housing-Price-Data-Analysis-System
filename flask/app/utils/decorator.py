from functools import wraps
from flask import g
from app.api.errors import error_response
from app.models import Permission


def permission_required(permission):
    '''检查常规权限'''
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):  # 用户通过了Basic Auth认证后，就会在当前会话中附带 g.current_user
                return error_response(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    '''检查管理员权限'''
    return permission_required(Permission.ADMIN)(f)