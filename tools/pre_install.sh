#!/usr/bin/env bash
echo "config pip"
mkdir -p ~/.pip/

if [ -e ~/.pip/pip.conf ];then
  mv ~/.pip/pip.conf ~/.pip/pip.conf.old
fi

echo "[global]" >> ~/.pip/pip.conf
echo "index-url = http://pypi.douban.com/simple" >> ~/.pip/pip.conf

deactivate

echo "config virtualenv"
mkdir -p ~/python_env
cd ~/python_env
if [ -e /opt/python_env ];then
  touch /opt/python_env;
else
  sudo ln -s $(pwd) /opt
fi

cd /opt/python_env
if [ -d /opt/python_env/django-scaffold ];then
  touch /opt/python_env/django-scaffold;
  source /opt/python_env/django-scaffold/bin/activate
else
  virtualenv django-scaffold && source /opt/python_env/django-scaffold/bin/activate
fi

echo "install python libs from pip"
pip install -r /opt/projects/django-scaffold/requirements/pip.txt

echo "pip install done."

echo "You might install python from github:"
echo "pip install -r /opt/projects/django-scaffold/requirements/github.txt"
echo "If install github wrong, you can clone the project first, then use 'pip install -e .'"
