'''
This script is for testing querying Prometheus metrics.

Usage:
    python3 pull_metrics.py
'''
import time
import requests


PROMETHEUS_ENDPOINT = 'http://localhost:9090'

METRICS_TO_PULL = [
    'up',
    'process_cpu_seconds_total',
    'process_open_fds'
]

def main():
    count = 0
    for metric in METRICS_TO_PULL:
        count += 1
        query = f"{metric}"

        params = {'query': query}
        print(params)
        query_url = f"{PROMETHEUS_ENDPOINT}/api/v1/query"

        response = requests.get(query_url, params=params, verify=False)

        print('Response: ', response)
        print(response.json())
        print('='*80)

        if count >= len(METRICS_TO_PULL):
            break
        time.sleep(5)


if __name__=='__main__':
    main()        