"""
A script to test creating custome Prometheus metrics with python.
"""
import time
from datetime import datetime
from prometheus_client import start_http_server, Counter, Gauge
import psutil

CHECK_COUNTER = Counter('resource_check_counter', 'Total number of checks in current session')
CPU_UTIL_PERCENT = Gauge('cpu_util_percent', 'CPU utilization percentage', ['status'])
MEMORY_UTIL_PERCENT = Gauge('memory_util_percent', 'Memory util percentage', ['status'])

HIGH_THRESHOLD = 85
CRITICAL_THRESHOLD = 98

WAIT_TIME_SECONDS = 5
MAX_RUNNING_TIME_SECONDS = 300

def set_status_label(util_percent):
    if util_percent >= HIGH_THRESHOLD and util_percent < CRITICAL_THRESHOLD:
        return 'high'
    elif util_percent >= CRITICAL_THRESHOLD:
        return 'critical'
    
    return 'normal'

def main():
    # Start server on port 8008 for prometheus to gather metrics
    start_http_server(8008)

    flag = True
    counter = 0
    while flag:
        counter += WAIT_TIME_SECONDS
        CHECK_COUNTER.inc()
        cpu_perc = psutil.cpu_percent(interval=1)
        mem_perc = psutil.virtual_memory().percent

        CPU_UTIL_PERCENT.labels(status=set_status_label(cpu_perc)).set(cpu_perc)
        MEMORY_UTIL_PERCENT.labels(status=set_status_label(mem_perc)).set(mem_perc)

        if counter > MAX_RUNNING_TIME_SECONDS:
            break
        
        time.sleep(WAIT_TIME_SECONDS)


if __name__=='__main__':
    print('Start time: ', str(datetime.now()))
    print('The script will run for ', str(MAX_RUNNING_TIME_SECONDS/60), 'minutes...')
    main()
    print('Script completed...')