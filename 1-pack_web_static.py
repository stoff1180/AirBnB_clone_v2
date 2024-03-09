#!/usr/bin/python3
"""
    Fabric script generating tgz archive from contents of web_static
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
<<<<<<< HEAD
        generates a .tgz archive from contents of web_static
=======
       Generates a .tgz archive from contents of web_static
>>>>>>> 6a1a6d125552c0cdb687e66001201cf4308a512b
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(file_name))
        return file_name
    except:
        return None
