#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
项目重命名并且备份
'''

import click
import os
from sh import cp, mv

NGINX_CONFS = [
    'deploy/nginx/{}-dev.conf',
    'deploy/nginx/{}-master.conf',
]

@click.command()
@click.option('--newname', prompt='new project name', help='Please input new project name.')
def rename(newname):
    this_file_path = os.path.split(os.path.realpath(__file__))[0]
    old_project_path = os.path.split(this_file_path)[0]
    oldname = os.path.split(old_project_path)[-1]
    new_project_path = os.path.join(os.path.split(old_project_path)[0], newname)
    cp_cmd = cp('-r', old_project_path, new_project_path)
    click.echo(''.join(cp_cmd))
    django_settings_dir = os.path.join(new_project_path, oldname)
    if os.path.exists(django_settings_dir):
        mv(django_settings_dir, os.path.join(new_project_path, newname))
    for nginx_conf in NGINX_CONFS:
        file_path = os.path.join(new_project_path, nginx_conf)
        mv(nginx_conf.format(file_path, oldname), nginx_conf.format(file_path, newname))
    cmd ='cd {} && grep {} -ril ./ | xargs sed -i "s/{}/{}/g"'.format(new_project_path, oldname, oldname, newname)
    os.system(cmd)
    click.echo('new files in {}'.format(new_project_path))
    click.echo("please run cmd: 'cd {} && grep {} -ril ./' to check if all string has replaced!".format(new_project_path, oldname))
    click.echo('done.')

if __name__ == '__main__':
    rename()
