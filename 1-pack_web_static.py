#!/usr/bin/python3
"""
Fabric script that generates a compressed archive of the contents of the
web_static directory.
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """Pack and compress the files in a tgz file format"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
