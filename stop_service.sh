#!/bin/bash

echo "Stopping service prometheus"
service prometheus stop
echo "Stopping service pushgateway"
service pushgateway stop