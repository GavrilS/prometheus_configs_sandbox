"""
A script to first get the currently available deployment metrics from prometheus and than 
extract the max replicas label value into a separate metric.
"""
from datetime import datetime
from prometheus_client import Gauge, CollectorRegistry, push_to_gateway
from prometheus_api_client import PrometheusConnect
prom = PrometheusConnect(url='http://localhost:9090', disable_ssl=True)

registry = CollectorRegistry()
DEPLOYMENT_MAX_REPLICAS = Gauge(
    'deployment_max_replicas', 
    'Deployment max replicas', 
    ['deployment', 'namespace', 'job'],
    registry=registry
)

PUSHGATEWAY_ENDPOINT = 'localhost:9091'

def main():
    results = prom.custom_query(query="deployment_replicas")

    print('Printing results for deployment_replicas', '\n*******\n')
    for item in results:
        print(item)
        metric_labels = item.get('metric', {})
        deployment = metric_labels.get('deployment', '')
        max_replicas = int(metric_labels.get('max_replicas', 0))
        namespace = metric_labels.get('namespace', '')
        job = metric_labels.get('job', '')

        DEPLOYMENT_MAX_REPLICAS.labels(deployment=deployment, namespace=namespace, job=job).set(max_replicas)
        # DEPLOYMENT_MAX_REPLICAS.set_to_current_time()
        push_to_gateway(PUSHGATEWAY_ENDPOINT, job=job, registry=registry)


if __name__=='__main__':
    print('Start time: ', str(datetime.now()))
    print('-'*40)
    main()
    print('-'*40)
    print('Script completed...')