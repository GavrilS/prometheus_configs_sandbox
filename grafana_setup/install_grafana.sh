#!/bin/bash

# First move to the /tmp/ directory
# cd /tmp/

# Install from the APT repository
# - install the prerequisite packages:
sudo apt-get install -y apt-transport-https software-properties-common wget
# - import GPG key:
sudo mkdir -p /etc/apt/keyrings/
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null
# - add a repository for stable release:
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
# - updates the list of available packages
sudo apt-get update
# - installs the latest OSS release:
sudo apt-get install grafana
