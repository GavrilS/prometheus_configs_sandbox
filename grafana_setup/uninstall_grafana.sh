#!/bin/bash

# Stop grafana with systemd service:
sudo systemctl stop grafana-server

# Stop grafana with init.d service:
# sudo service grafana-server stop

# Uninstall Grafana OSS:
sudo apt-get remove grafana

# Optional - remove the Grafana repository:
# sudo rm -i /etc/apt/sources.list.d/grafana.list
