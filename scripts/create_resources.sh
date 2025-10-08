#!/bin/bash
set -e

PROJECT_ID="iot-sensor-security-1"
REGION="us-central1"

echo "=== Creating Pub/Sub topics ==="
gcloud pubsub topics create iot-sensor --project=$PROJECT_ID || true
gcloud pubsub topics create alerts --project=$PROJECT_ID || true

echo "=== Creating BigQuery dataset ==="
bq --location=$REGION mk --dataset ${PROJECT_ID}:iot || true

echo "=== Creating tables ==="
bq mk --table ${PROJECT_ID}:iot.sensor_readings \
  sensor_id:STRING,timestamp:TIMESTAMP,type:STRING,value:FLOAT,unit:STRING || true

bq mk --table ${PROJECT_ID}:iot.anomalies \
  alert:STRING,value:FLOAT,timestamp:TIMESTAMP || true

echo "✅ All resources created successfully for project $PROJECT_ID"
