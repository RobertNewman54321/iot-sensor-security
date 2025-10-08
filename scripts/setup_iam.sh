#!/bin/bash
set -e

PROJECT_ID="iot-sensor-security"

echo "Using project: $PROJECT_ID"

# 1. Create service accounts
echo "Creating service accounts..."
gcloud iam service-accounts create pubsub-publisher \
  --project="$PROJECT_ID" \
  --display-name="Pub/Sub Publisher Service Account"

gcloud iam service-accounts create cloud-function-sa \
  --project="$PROJECT_ID" \
  --display-name="Cloud Function Service Account"

gcloud iam service-accounts create looker-studio-sa \
  --project="$PROJECT_ID" \
  --display-name="Looker Studio Service Account"

# 2. Grant roles to service accounts

echo "Granting IAM roles..."

# Pub/Sub publisher: allow publishing to Pub/Sub
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member="serviceAccount:pubsub-publisher@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/pubsub.publisher"

# Cloud Function SA: allow subscription to Pub/Sub and BigQuery writes
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member="serviceAccount:cloud-function-sa@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/pubsub.subscriber"

gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member="serviceAccount:cloud-function-sa@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/bigquery.dataEditor"

# Looker Studio SA: allow read-only access to BigQuery
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member="serviceAccount:looker-studio-sa@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/bigquery.dataViewer"

echo "All IAM bindings applied."
