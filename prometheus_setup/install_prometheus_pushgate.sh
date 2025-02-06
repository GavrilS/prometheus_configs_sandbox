#!/bin/bash

# Create a user and group for the prometheus pushgate
useradd -M -r -s /bin/false pushgate

# Download and install the Pushgate binary
wget https://github.com/prometheus/pushgateway/releases/download/v1.2.0/pushgateway-1.2.0.linux-amd64.tar.gz

tar xvfz pushgateway-1.2.0.linux-amd64.tar.gz

mv pushgateway-1.2.0.linux-amd64/pushgateway /usr/local/bin/

chown pushgateway:pushgateway /usr/local/bin/pushgateway

rm pushgateway-1.2.0.linux-amd64.tar.gz

# Create a systemd unit file for Pushgateway
cp config_files/pushgateway.service /etc/systemd/system/

# Start and enable the pushgateway service
systemctl enable pushgateway

systemctl start pushgateway

# Verify the service
systemctl status pushgateway

curl localhost:9091/metrics