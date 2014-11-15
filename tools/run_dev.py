#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import os

@click.command()
def run():
    this_file_path = os.path.split(os.path.realpath(__file__))[0]
    project_path = os.path.split(this_file_path)[0]
    cmd = "python {} runserver 0.0.0.0:10000 2>&1 &".format(os.path.join(project_path, 'manage.py'))
    os.system(cmd)

if __name__ == '__main__':
    run()
