#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static.

# Install Nginx if it is not already installed
if ! dpkg -l | grep -q nginx; then
    apt-get -y update
    apt-get -y install nginx
fi

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "Fake content for testing" > /data/web_static/releases/test/index.html

# Create a symbolic link to the test release
if [ -e /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve web_static content
config_file="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" $config_file; then
    sed -i "/server_name _;/a location /hbnb_static/ { alias /data/web_static/current/; }" $config_file
fi

# Restart Nginx
service nginx restart

exit 0
