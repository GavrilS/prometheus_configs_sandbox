"""
A script to first get the currently available deployment metrics from prometheus and than 
extract the max replicas label value into a separate metric.
"""
from datetime import datetime
from prometheus_api_client import PrometheusHost
prom = PrometheusHost('localhost:9090', disable_ssl=True)


def main():
    pass


if __name__=='__main__':
    print('Start time: ', str(datetime.now()))
    print('-'*40)
    main()
    print('-'*40)
    print('Script completed...')