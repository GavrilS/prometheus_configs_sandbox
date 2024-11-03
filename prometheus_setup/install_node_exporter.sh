#!/bin/bash

wget https://github.com/prometheus/node_exporter/releases/download/v1.8.2/node_exporter-1.8.2.linux-amd64.tar.gz
tar xvfz node_exporter-*.*-amd64.tar.gz
mv node_exporter-*.*-amd64 /etc/node_exporter-*.*-amd64
rm node_exporter-*.*-amd64.tar.gz
cd /etc/node_exporter-*.*-amd64
./node_exporter &
