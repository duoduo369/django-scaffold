#!/usr/bin/env bash

if [ "x$(whoami)" != "xroot" ]; then
    echo "Only root can run this script."
    exit 1
fi

cp /opt/projects/django-scaffold/deploy/nginx/django-scaffold-master.conf /etc/nginx/sites-enabled/django-scaffold-master.conf
nginx -s reload

echo "127.0.0.1 django-scaffold-master.com" >> /etc/hosts
