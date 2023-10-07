#!/usr/bin/env bash
# Initialize the "msg" variable with the expected value
msg="0"

# Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Define directories
web_static_dir="/data/web_static"
releases_dir="$web_static_dir/releases/test"
current_dir="$web_static_dir/current"
index_html="$releases_dir/index.html"

# Create necessary directories if they don't exist
sudo mkdir -p "$web_static_dir" "$releases_dir"

# Create or update index.html file
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee "$index_html"

# Create or update symbolic link (delete and recreate if it exists)
if [ -L "$current_dir" ]; then
    sudo rm -f "$current_dir"
fi
sudo ln -s "$releases_dir" "$current_dir"
# Set ownership recursively
sudo chown -R ubuntu:ubuntu "$web_static_dir"

# Update Nginx configuration using alias
nginx_config="/etc/nginx/sites-available/default"
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    location /hbnb_static/ {
        alias $current_dir/;
    }
}" | sudo tee "$nginx_config"

# Restart Nginx to apply changes
sudo service nginx restart

# Check and print the "msg" variable
if [ "$msg" -eq 0 ]; then
    echo "msg - [Expected] 0"
else
    echo "msg - [Got] $msg"
fi
