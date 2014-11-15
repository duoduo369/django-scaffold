#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
import json

with open('./port.json') as f:
    PORT_CONFIG = json.load(f)

RENAME_DEV_FILES = [
    'deploy/nginx/django-scaffold-dev.conf',
    'tools/run_dev.py'
    'tools/port.json'
]

RENAME_MASTER_FILES = [
    'deploy/nginx/django-scaffold-master.conf',
    'tools/run_master.py'
    'tools/port.json'
]

def get_config(reset_type):
    config = {}
    if reset_type != 'master':
        config['rename_files'] = RENAME_DEV_FILES
        config['old_port'] = PORT_CONFIG['DEV_PORT']
    else:
        config['rename_files'] = RENAME_MASTER_FILES
        config['old_port'] = PORT_CONFIG['MASTER_PORT']
    return config



@click.command()
@click.option('--reset_type', default='dev', help='port type: [dev|master], default dev')
@click.option('--new_port', prompt='new port', help='Please input new port')
def reset_port(reset_type, new_port):
    this_file_path = os.path.split(os.path.realpath(__file__))[0]
    project_path = os.path.split(this_file_path)[0]
    config = get_config(reset_type)
    for each in config['rename_files']:
        file_path = os.path.join(project_path, each)
        os.system('''sed -i "" -e "s/{}/{}/g" "{}" 2>/dev/null'''.format(config['old_port'], new_port, file_path))

if __name__ == '__main__':
    reset_port()
