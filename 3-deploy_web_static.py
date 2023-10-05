#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers.
"""
from fabric.api import run, put, env
from os.path import exists
from datetime import datetime
import os

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = 'my_ssh_private_key'  # Replace with your private key path


def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if successful, None otherwise.
    """
    try:
        # Create the "versions" directory if it doesn't exist
        if not exists("versions"):
            os.makedirs("versions")

        # Generate the archive path
        now = datetime.now()
        archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second
        )

        # Create the .tgz archive
        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distribute an archive to your web servers.

    Args:
        archive_path: The path to the archive to deploy.

    Returns:
        True if all operations have been done correctly, otherwise returns False.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web servers
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/
        filename = os.path.basename(archive_path)
        release_path = '/data/web_static/releases/{}'.format(filename[:-4])
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(filename, release_path))

        # Delete the archive from the web servers
        run('rm /tmp/{}'.format(filename))

        # Move the contents of the extracted folder to the release folder
        run('mv {}/web_static/* {}'.format(release_path, release_path))

        # Remove the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link to the new version of your code
        run('ln -s {} /data/web_static/current'.format(release_path))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed:", str(e))
        return False


def deploy():
    """
    Deploy the web_static content to your web servers.

    Returns:
        True if successful, otherwise returns False.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
