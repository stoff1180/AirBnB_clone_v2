#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""
from fabric.api import env, run, local
import os
import sys

env.hosts = ['54.209.110.192', '54.237.218.150']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = int(number)
    if number < 0:
        return
    with cd("/data/web_static/releases"):
        archives = run("ls -1").split()
        archives.sort(key=lambda x: os.path.getmtime(x))
        num_to_keep = min(number + 1, len(archives))
        archives_to_delete = archives[:-num_to_keep]
        for archive in archives_to_delete:
            run("rm -rf {}".format(archive))
    with cd("/data/web_static/current"):
        archives = run("ls -1").split()
        archives.sort(key=lambda x: os.path.getmtime(x))
        num_to_keep = min(number + 1, len(archives))
        archives_to_delete = archives[:-num_to_keep]
        for archive in archives_to_delete:
            run("rm -rf {}".format(archive))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fab -f 3-deploy_web_static.py do_clean:number=N")
    else:
        do_clean(sys.argv[1].split('=')[1])
