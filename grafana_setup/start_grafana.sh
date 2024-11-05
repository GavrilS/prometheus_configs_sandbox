#!/bin/bash

# Start the grafana server with systemd
sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl status grafana-server

# Configure the grafana server to start at boot using systemd
sudo systemctl enable grafana-server.service

# Edit the config file
# Alternatively, create a file in /etc/systemd/system/grafana-server.service.d/override.conf
# sudo systemctl edit grafana-server.service

# Restart the grafana server using systemd
# sudo systemctl restart grafana-server

# Start the Grafana server using init.d
# - start the server:
# sudo service grafana-server start
# sudo service grafana-server status
# - configure grafana server to start at boot time with init.d:
# sudo update-rc.d grafana-server defaults
# sudo service grafana-server restart
