import time, random
from prometheus_client import start_http_server, Gauge

GPU_TEMP    = Gauge('DCGM_FI_DEV_GPU_TEMP',    'GPU temperature', ['gpu'])
GPU_POWER   = Gauge('DCGM_FI_DEV_POWER_USAGE', 'GPU power usage', ['gpu'])
GPU_UTIL    = Gauge('DCGM_FI_DEV_GPU_UTIL',    'GPU utilization', ['gpu'])

print("DCGM Mock başladı → http://localhost:9400/metrics")
start_http_server(9400)

load = 0.0
while True:
    load = min(1.0, load + random.uniform(0.05, 0.15))
    if load > 0.95:
        load = 0.2
    for i in range(8):
        GPU_TEMP.labels(gpu=str(i)).set(round(42 + load*40 + random.uniform(-2,2), 1))
        GPU_POWER.labels(gpu=str(i)).set(round(200 + load*780 + random.uniform(-10,10), 1))
        GPU_UTIL.labels(gpu=str(i)).set(round(load*100 + random.uniform(-3,3), 1))
    time.sleep(1)
