#!/bin/bash
set -e

PROJECT_ID="iot-sensor-security-1"
REGION="us-central1"
BUCKET_NAME="iot-audit-snapshots"
DATE=$(date +%Y%m%d-%H%M%S)

gcloud config set project $PROJECT_ID

echo "=== Checking for export bucket ==="
if ! gsutil ls -b gs://$BUCKET_NAME >/dev/null 2>&1; then
  echo "Bucket not found. Creating bucket gs://$BUCKET_NAME ..."
  gsutil mb -l $REGION gs://$BUCKET_NAME
else
  echo "Bucket already exists. Skipping creation."
fi

echo "=== Exporting IAM policy snapshot ==="
gcloud projects get-iam-policy $PROJECT_ID --format yaml > docs/final_iam_snapshot_$DATE.yaml

echo "=== Exporting asset inventory snapshot ==="
gcloud asset inventory export \
  --project=$PROJECT_ID \
  --content-type=resource \
  --output-path=gs://$BUCKET_NAME/asset_snapshot_$DATE.json

echo "✅ Compliance snapshot exported to docs/ and $BUCKET_NAME"
