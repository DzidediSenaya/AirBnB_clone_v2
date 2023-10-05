#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.
"""
from fabric.api import env, run, local, lcd
import os
from datetime import datetime


env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = 'my_ssh_private_key'  # Replace with your private key path
env.use_ssh_config = True


def do_clean(number=0):
    """
    Delete out-of-date archives.

    Args:
        number: The number of archives to keep (default is 0).
    """
    if int(number) < 1:
        number = 1
    else:
        number = int(number) + 1

    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs -I {{}} rm -f {{}}".format(number))

    with cd("/data/web_static/releases"):
        run("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}".format(number))


if __name__ == "__main__":
    do_clean()
