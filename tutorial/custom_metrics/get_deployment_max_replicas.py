"""
A script to first get the currently available deployment metrics from prometheus and than 
extract the max replicas label value into a separate metric.
"""
from datetime import datetime
from prometheus_api_client import PrometheusConnect
prom = PrometheusConnect(url='http://localhost:9090', disable_ssl=True)


def main():
    results = prom.custom_query(query="deployment_replicas")

    # print('Printing results in the format: metric \\n metric_name, metric_labels', '\n*******\n')
    for item in results:
        print(item)
        # print(item.metric_name, item.label_config, '\n*******\n')
        


if __name__=='__main__':
    print('Start time: ', str(datetime.now()))
    print('-'*40)
    main()
    print('-'*40)
    print('Script completed...')