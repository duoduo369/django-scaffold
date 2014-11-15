#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os

# deploy/nginx/django-scaffold-dev.conf
DEV_PORT = 9888

RENAME_FILES = [
    '{}/deploy/nginx/django-scaffold-dev.conf',
]

@click.command()
def reset_port():
    this_file_path = os.path.split(os.path.realpath(__file__))[0]
    project_path = os.path.split(this_file_path)[0]
    nginx_dev_conf = ''.format(project_path)
    os.system('''sed -i "" -e "s/%s/%s/g" "%s" 2>/dev/null''' % (old_port, new_port, file_path))

if __name__ == '__main__':
    reset_port()
