#!/bin/bash

# Install steps for Ubuntu 22.04
# Update system packages with the sudo command
apt update

# Create a system user for prometheus - with the sudo command
groupadd --system prometheus
useradd -s /sbin/nologin --system -g prometheus prometheus

# Create directories for prometheus - with the sudo command
mkdir /etc/prometheus
mkdir /var/lib/prometheus

# Download prometheus and extract files
wget https://github.com/prometheus/prometheus/releases/download/v2.55.0/prometheus-2.55.0.linux-amd64.tar.gz

tar vxf prometheus*.tar.gz

cd prometheus*/

# Move the binary files and set owner - with sudo
mv prometheus /usr/local/bin
mv promtool /usr/local/bin
chown prometheus:prometheus /usr/local/bin/prometheus
chown prometheus:prometheus /usr/local/bin/promtool

# Move the configuration files and set owner - with sudo
mv consoles /etc/prometheus
mv console_libraries /etc/prometheus
mv prometheus.yml /etc/prometheus
chown prometheus:prometheus /etc/prometheus
chown -R prometheus:prometheus /etc/prometheus/consoles
chown -R prometheus:prometheus /etc/prometheus/console_libraries
chown -R prometheus:prometheus /var/lib/prometheus

cd ../

# Copy the base prometheus config content to the actual config file - with sudo
cp prometheus.yml /etc/prometheus/prometheus.yml

# Create prometheus systemd service and reload systemd - with sudo
cp prometheus.service /etc/systemd/system/prometheus.service
systemctl daemon-reload

# Start prometheus service - with sudo
systemctl enable prometheus
systemctl start prometheus
systemctl status prometheus

# Accessing prometheus interface - with sudo
ufw allow 9090/tcp
