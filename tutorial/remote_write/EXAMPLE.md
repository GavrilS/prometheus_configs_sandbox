# Remote Write custom metrics

1. Components:

- the script send_custom_metrics.py is building timeseries samples and sending them to Prometheus via the remote write v1 protocol

- metrics.proto is a definition of the timeseries format in protobuf, which is needed according to Prometheus remote write documentation

2. Usage:

 - enable the python environment:

    source env/bin/activate

 - run the protobuf compiler on the metrics.proto file to build the python dependency
 - run the send_custom_metrics.py script:

    python3 send_custom_metrics.py

