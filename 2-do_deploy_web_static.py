#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers.
"""

from fabric.api import run, put, env
import os

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = 'my_ssh_private_key'  # Replace with your private key path

def do_deploy(archive_path):
    """
    Distribute an archive to your web servers.

    Args:
        archive_path: The path to the archive to deploy.

    Returns:
        True if all operations have been done correctly, otherwise returns False.
    """
    if not os.path.exists(archive_path):
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

if __name__ == "__main__":
    # Replace 'versions/web_static_20170315003959.tgz' with the actual archive path
    do_deploy('versions/web_static_20170315003959.tgz')
