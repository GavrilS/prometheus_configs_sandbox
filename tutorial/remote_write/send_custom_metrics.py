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

        metrics = generate_metrics(timestamp)

        for metric in metrics:
            pass

        response = requests.post(PROMETHEUS_WRITE_URL, json=metrics, headers=headers, verify=False)

        print('Response: ', response)
        print(response.text)
        # print(response.json())
        print('*'*100)

        time.sleep(30)


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
            'value': [timestamp, '1']
        },
        {
            'labels': {
                'name': 'random_test',
                'instance': 'localhost:9090',
                'job': 'python'
            },
            'value': [timestamp, '10']
        },
        {
            'labels': {
                'name': 'duplication_test',
                'instance': 'localhost:9090',
                'job': 'python'
            },
            'value': [timestamp, '100.2']
        }
    ]

    return metrics


if __name__=='__main__':
    main()