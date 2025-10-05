"""
A script to test creating custom Prometheus metrics with python and sending them to Prometheus through remote_write.
"""

import time
from datetime import datetime
import requests
import metrics_pb2

PROMETHEUS_WRITE_URL = 'http://localhost:9090/api/v1/write'


def main():
    headers = set_request_headers()
    write_message = metrics_pb2.WriteRequest()
    python_test_series = write_message.timeseries.add()
    random_test_series = write_message.timeseries.add()
    duplication_test_series = write_message.timeseries.add()

    while True:
        timestamp = datetime.now().timestamp()

        metrics = generate_metrics(int(timestamp))
        
        populate_timeseries(python_test_series, metrics[0])
        populate_timeseries(random_test_series, metrics[1])
        populate_timeseries(duplication_test_series, metrics[2])

        response = requests.post(PROMETHEUS_WRITE_URL, data=write_message, headers=headers, verify=False)

        print('Response: ', response)
        print(response.text)
        # print(response.json())
        print('*'*100)

        time.sleep(30)

def populate_timeseries(timeseries, metric):
    for key, value in metric['labels'].items():
        label = timeseries.labels.add()
        label.name = key
        label.value = value
    
    sample = timeseries.samples.add()
    sample.value = metric['value'][1]
    sample.timestamp = metric['value'][0]

def set_request_headers():
    headers = {
        'Content-Encoding': 'snappy',
        'Content-Type': 'application/x-protobuf',
        'User-Agent': 'Python Custom V1',
        'X-Prometheus-Remote-Write-Version': '0.1.0'
    }

    return headers

def generate_metrics(timestamp):

    metrics = [
        {
            'labels': {
                'name': 'python_test',
                'instance': 'localhost:9090',
                'job': 'python'
            },
            'value': [timestamp, 1]
        },
        {
            'labels': {
                'name': 'random_test',
                'instance': 'localhost:9090',
                'job': 'python'
            },
            'value': [timestamp, 10]
        },
        {
            'labels': {
                'name': 'duplication_test',
                'instance': 'localhost:9090',
                'job': 'python'
            },
            'value': [timestamp, 100]
        }
    ]

    return metrics


if __name__=='__main__':
    main()