#!/usr/bin/env bash
case $1 in
    "start")
        python /opt/projects/django-scaffold/manage.py  runserver --settings=django-scaffold.settings-dev 0.0.0.0:10000 >> /var/log/django-scaffold/dev-stdout.log 2>&1 &
        exit ${ret}
        ;;
    "stop")
        if [ $(netstat -ntlp | grep 10000 | awk '{print $7}' | awk -F/ '/^[0-9]/ {print $1}' | uniq | wc -l) = 0 ]; then
          touch /var
        else
          netstat -ntlp | grep 10000 | awk '{print $7}' | awk -F/ '/^[0-9]/ {print $1}' | uniq | xargs kill
        fi
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
