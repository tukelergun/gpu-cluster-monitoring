GPU Cluster Monitoring Stack

AI Infrastructure Engineer portfolio project.

 What this does
Simulates a real datacenter GPU telemetry pipeline:
- DCGM Mock — simulates 8 GPU nodes (temperature, power, utilization)
- Prometheus — scrapes metrics every 5 seconds  
- Grafana — live dashboard for GPU cluster monitoring

## Real datacenter equivalent
| This project | Real DC |
|---|---|
| dcgm_mock.py | DCGM on each DGX node |
| localhost:9400 | 192.168.x.x:9400 per node |
| Prometheus Docker | Central monitoring server |
| Grafana dashboard | NOC room display |

## Background
Thermal/cooling engineering background: CDU, chiller, direct liquid cooling.
Built as AI Infrastructure Engineer portfolio project.
