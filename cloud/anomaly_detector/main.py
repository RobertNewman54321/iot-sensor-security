import base64, json
from google.cloud import pubsub_v1

THRESHOLD = 70.0
PROJECT_ID = "iot-sensor-security"
ALERTS_TOPIC = "alerts"

publisher = pubsub_v1.PublisherClient()
alerts_path = publisher.topic_path(PROJECT_ID, ALERTS_TOPIC)

def pubsub_trigger(event, context):
    if "data" not in event:
        print("No data received")
        return

    message = json.loads(base64.b64decode(event["data"]).decode("utf-8"))
    value = message.get("value")

    if value > THRESHOLD:
        alert = {"alert": "Temperature threshold exceeded", "data": message}
        publisher.publish(alerts_path, json.dumps(alert).encode("utf-8"))
        print(f"Alert published: {alert}")
    else:
        print(f"Value normal: {value}")
