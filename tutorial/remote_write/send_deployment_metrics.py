"""
A script to test creating custome Prometheus metrics with python and sending them to Prometheus through remote_write.
"""
import time
from datetime import datetime
from prometheus_client import Gauge

g = Gauge('deployment_replicas', 'Deployment replicas', ['deployment', 'namespace', 'max_replicas', 'environment'])

def main():
    while True:


        g.labels(deployment='remote_write', namespace='python-test', max_replicas='3', environment='test').inc(10)
        print('Current deployment metrics: \n', g._value)
        # g.inc(10)
        # g.set_to_current_time()

        time.sleep(10)


if __name__=='__main__':
    main()