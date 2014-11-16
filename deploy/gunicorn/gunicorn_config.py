import multiprocessing
bind = "0.0.0.0:11000"
workers = multiprocessing.cpu_count()

BASE_PATH = '/opt/projects/django-scaffold'

max_requests = 5000

user = 'root'
group = 'root'

accesslog = '/var/log/django-scaffold/gunicorn-access.log'
errorlog =  '/var/log/django-scaffold/gunicorn-error.log'

pidfile = '/run/django-scaffold-gunicorn.pid'
