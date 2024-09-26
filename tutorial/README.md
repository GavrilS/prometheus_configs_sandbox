# Prometheus tutorial

To run the configuration:
docker-compose -f docker-compose.monitoring.yaml up -d

- setup prometheus with docker:
  docker run --name prometheus -v 'prometheus.yml:/etc/prometheus/prometheus.yml:ro' -d -p 127.0.0.1:9090:9090 prom/prometheus
