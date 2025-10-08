# IoT Sensor Security (Level 1 MVP)
Google Cloud prototype that simulates IoT sensor data and detects anomalies in real time.

## Architecture
Laptop (Python Simulator) → Pub/Sub → Cloud Function → BigQuery → Looker Studio → Email Alerts

## Quickstart
```bash
bash scripts/setup_env.sh
bash scripts/create_resources.sh
python sensors/simulator.py
bash scripts/deploy_cloud_function.sh
