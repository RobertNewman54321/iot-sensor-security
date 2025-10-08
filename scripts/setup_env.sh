#!/bin/bash
export PROJECT_ID="iot-sensor-security-1"
export REGION="us-central1"
export TOPIC_SENSOR="iot-sensor"
export TOPIC_ALERT="alerts"
export DATASET="iot"
gcloud config set project $PROJECT_ID
gcloud config set compute/region $REGION
echo "Environment configured for $PROJECT_ID in $REGION"
gcloud services enable pubsub.googleapis.com bigquery.googleapis.com cloudfunctions.googleapis.com monitoring.googleapis.com
