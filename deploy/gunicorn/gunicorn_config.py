import multiprocessing
bind = "0.0.0.0:11000"
workers = multiprocessing.cpu_count()

BASE_PATH = '/opt/projects/django-scaffold'

max_requests = 5000

timeout = 300

preload_app = True

user = 'root'
group = 'root'

pidfile = '/run/django-scaffold-gunicorn.pid'
