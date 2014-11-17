#!/usr/bin/env bash
case $1 in
    "start")
        yes yes | python /opt/projects/django-scaffold/manage.py collectstatic
        if [ -e /run/django-scaffold-supervisord.pid ] ;then
          /opt/python_env/django-scaffold/bin/supervisorctl -c /opt/projects/django-scaffold/deploy/supervisor/supervisord.conf restart django-scaffold
        else
          /opt/python_env/django-scaffold/bin/supervisord -c /opt/projects/django-scaffold/deploy/supervisor/supervisord.conf
        fi
        exit ${ret}
        ;;
    "stop")
        if [ -e /run/django-scaffold-supervisord.pid ] ;then
          /opt/python_env/django-scaffold/bin/supervisorctl -c /opt/projects/django-scaffold/deploy/supervisor/supervisord.conf stop django-scaffold && /opt/python_env/django-scaffold/bin/supervisorctl -c /opt/projects/django-scaffold/deploy/supervisor/supervisord.conf shutdown
        fi
        ;;
    "restart")
        if [ -e /run/django-scaffold-supervisord.pid ] ;then
          yes yes | python /opt/projects/django-scaffold/manage.py collectstatic
          /opt/python_env/django-scaffold/bin/supervisorctl -c /opt/projects/django-scaffold/deploy/supervisor/supervisord.conf restart django-scaffold
        else
          $0 start
        fi
        ;;
    *)
        echo "usage: $(basename $0) {start|stop|restart}"
        exit 1
        ;;
esac
