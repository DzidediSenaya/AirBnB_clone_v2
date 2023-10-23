#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder.
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if successful, None otherwise.
    """
    try:
        # Create the "versions" directory if it doesn't exist
        if not os.path.exists("versions"):
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


if __name__ == "__main__":
    do_pack()
