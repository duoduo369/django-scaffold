#!/usr/bin/env bash

if [ "x$(whoami)" != "xroot" ]; then
    echo "Only root can run this script."
    exit 1
fi

cp /opt/projects/django-scaffold/deploy/nginx/django-scaffold-dev.conf /etc/nginx/sites-enabled/django-scaffold-dev.conf
nginx -s reload

echo "127.0.0.1 django-scaffold-demo.com" >> /etc/hosts
