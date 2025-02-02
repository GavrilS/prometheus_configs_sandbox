"""
A script to test creating custome Prometheus metrics with python.
"""
import time
from datetime import datetime
from prometheus_client import start_http_server, Gauge

DEPLOYMENT_REPLICAS = Gauge('deployment_replicas', 'Deployment replicas', ['deployment', 'namespace', 'max_replicas'])

WAIT_TIME_SECONDS = 5
MAX_RUNNING_TIME_SECONDS = 300

def main():
    # Start server on port 8008 for prometheus to gather metrics
    start_http_server(8008)

    flag = True
    counter = 0
    while flag:
        counter += WAIT_TIME_SECONDS

        DEPLOYMENT_REPLICAS.labels(deployment='prom_helper', namespace='test1', max_replicas='2')
        DEPLOYMENT_REPLICAS.labels(deployment='prom_helper2', namespace='test2', max_replicas='5')
        DEPLOYMENT_REPLICAS.labels(deployment='python_to_prom', namespace='py_runner', max_replicas='3')

        if counter > MAX_RUNNING_TIME_SECONDS:
            break
        
        time.sleep(WAIT_TIME_SECONDS)


if __name__=='__main__':
    print('Start time: ', str(datetime.now()))
    print('The script will run for ', str(MAX_RUNNING_TIME_SECONDS/60), 'minutes...')
    main()
    print('Script completed...')