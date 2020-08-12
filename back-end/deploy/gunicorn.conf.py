import multiprocessing

bind = '0.0.0.0:5000'
workers = multiprocessing.cpu_count() * 2 + 1
# daemon = True
pidfile = '/run/gunicorn.pid'
loglevel = 'info'
errorlog = '/tmp/gunicorn-error.log'
accesslog = '/tmp/gunicorn-access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
