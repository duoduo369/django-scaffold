#!/usr/bin/env bash

if [ "x$(whoami)" != "xroot" ]; then
    echo "Only root can run this script."
    exit 1
fi

echo "install linux dependence"
apt-get install python-dev
apt-get install mysql-server mysql-client libmysqlclient-dev
apt-get install memcached nginx

echo "install pip"
apt-get install python-pip


echo "config pip"
mkdir -p ~/.pip/

if [ -e ~/.pip/pip.conf ];then
  mv ~/.pip/pip.conf ~/.pip/pip.conf.old
fi

echo "[global]" >> ~/.pip/pip.conf
echo "index-url = http://pypi.douban.com/simple" >> ~/.pip/pip.conf

deactivate

echo "install virtualenv"
pip install virtualenv

echo "config virtualenv"
mkdir -p ~/python_env
cd ~/python_env
if [ -e /opt/python_env ];then
  touch /opt/python_env;
else
  ln -s $(pwd) /opt
fi

cd /opt/python_env
if [ -d /opt/python_env/django-scaffold ];then
  touch /opt/python_env/django-scaffold;
  source /opt/python_env/django-scaffold/bin/activate
else
  virtualenv django-scaffold && source /opt/python_env/django-scaffold/bin/activate
fi


echo "install python libs"
pip install -r /opt/projects/django-scaffold/requirements.txt

echo "mkdir log dirs"
mkdir -p /var/log/django-scaffold
mkdir -p /var/log/django-scaffold/supervisordchild
