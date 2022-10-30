import os
import multiprocessing
workers = multiprocessing.cpu_count() * 2 + 1
threads = 3
daemon = 'false'
worker_connections = 2000
max_requests = 2000
backlog = 512
keepalive = 3
pidfile = '/home/cwy/Documents/gunicorn.pid'
accesslog = '/home/cwy/Documents/gunicorn_acess.log'
errorlog = '/home/cwy/Documents/gunicorn_error.log'
bind = f'{os.getenv("IP")}:{os.getenv("GUNICORN_PORT")}'
worker_class = "gevent"
timeout = 120
debug = False