#!/usr/bin/env python3
"""
    Fabric script that generates tgz archive from contents of web_static
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        generates a .tgz archine from contents of web_static
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    result = local("mkdir -p ./versions", capture=True)
    if result.failed:
        return None
    result = local("tar --create --verbose -z --file={} \
            ./web_static".format(file_name), capture=True)
    if result.failed:
        return None
    return file_name
