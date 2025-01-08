#!/bin/bash

if [ "$#" -eq 0 ];
then
    # Create prometheus systemd service and reload systemd - with sudo
    cp config_files/prometheus.service /etc/systemd/system/prometheus.service
    systemctl daemon-reload

    # Start prometheus service - with sudo
    systemctl enable prometheus
    systemctl start prometheus &&
    systemctl status prometheus

elif [ "$#" -eq 1 ] && [ $1 = "wsl" ]
then
    echo "Running on $1"
    /usr/local/bin/prometheus \
    --config.file /etc/prometheus/prometheus.yml \
    --storage.tsdb.path /var/lib/prometheus/ \
    --web.console.templates=/etc/prometheus/consoles \
    --web.console.libraries=/etc/prometheus/console_libraries &
fi

# Accessing prometheus interface - with sudo
ufw allow 9090/tcp
