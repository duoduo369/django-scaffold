#!/usr/bin/env bash
case $1 in
    "start")
        python /opt/projects/django-scaffold/manage.py runserver 0.0.0.0:10000 >> /var/log/django-scaffold-stdout.log 2>&1 &
        exit ${ret}
        ;;
    "stop")
        ps x | grep django-scaffold | grep python | awk '{print $1}' | xargs kill
        ;;
    "restart")
        $0 stop
        $0 start
        ;;
    *)
        echo "usage: $(basename $0) {start|stop|restart}"
        exit 1
        ;;
esac
