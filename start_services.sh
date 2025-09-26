#!/bin/bash

echo "Starting service prometheus"
service prometheus start
echo "Starting service pushgateway"
service pushgateway start