# Goals
1. Testing how to set up custom metrics with python and send them to Prometheus
2. Set up a specific metric with labels and try to read it from Prometheus, after that extract the value of a specific label into a separate metric and send it to Prometheus using Prometheus Pushgateway

# Requirements
- this setup was tested on a linux server
- python 3.10
- python libraries for the scripts - prometheus_client, prometheus_api_client
- prometheus 2.55.0
- prometheus pushgateway 1.2.0
- configuration for prometheus can be seen in 'prometheus_setup/config_files/prometheus.yml'

# Scripts overview
- setup_custom_metrics.py - creating custom metrics(Gauge, Counter) and expose them to Prometheus via a python server which is scraped by Prometheus

- replicate_deployment_metrics.py - create a custom metric that has a specific label which we want to extract into a separate metric and expose the metric for scraping through a python server

- get_deployment_max_replicas.py - query the 'deployment' metric we have created before and extract the label we want to turn into a metric; create a new Gauge metric to hold the value of the label and populate it with the relevant labels; after the metric is created send it to Prometheus through Prometheus Pushgateway; this script is also a test on how to use Prometheus Pushgateway