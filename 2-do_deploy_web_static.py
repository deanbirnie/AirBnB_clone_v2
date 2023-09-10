#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['100.26.226.80', '54.166.136.119']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        filetype = file_n.split(".")[0]
        directory = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(directory, filetype))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, directory, filetype))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(directory, filetype))
        run('rm -rf {}{}/web_static'.format(directory, filetype))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(directory, filetype))
        return True
    except:
        return False
