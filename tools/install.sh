#!/usr/bin/env bash

if [ "x$(whoami)" != "xroot" ]; then
    echo "Only root can run this script."
    exit 1
fi

echo "install linux dependence"
apt-get install python-dev
apt-get install mysql-server mysql-client libmysqlclient-dev
apt-get install memcached nginx gettext

echo "install pip"
apt-get install python-pip

echo "install virtualenv"
pip install virtualenv

echo "mkdir log dirs"
mkdir -p /var/log/django-scaffold
mkdir -p /var/log/django-scaffold/supervisordchild

echo "pre install done."
