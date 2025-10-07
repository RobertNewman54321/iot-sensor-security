# Grant Pub/Sub permission to write to BigQuery
bq update --source cloud/dataset.json iot_dataset

# Ensure service account has role
gcloud projects add-iam-policy-binding iot-sensor-security \
  --member="serviceAccount:service-<PROJECT_NUMBER>@gcp-sa-pubsub.iam.gserviceaccount.com" \
  --role="roles/bigquery.dataEditor"
