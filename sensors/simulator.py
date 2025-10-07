import json
import random
import datetime
from google.cloud import pubsub_v1

# Google Cloud configuration
PROJECT_ID = "iot-sensor-security"
TOPIC_ID = "iot-sensor"

def load_sensor_config():
    """Load sensor definitions from the JSON config file."""
    with open("sensor_config.json", "r") as file:
        return json.load(file)

def generate_sensor_value(sensor):
    """Generate a random value within the sensor's configured range."""
    return round(random.uniform(sensor["min_value"], sensor["max_value"]), 2)

def build_message(sensor):
    """Create a structured JSON message for each sensor reading."""
    message = {
        "sensor_id": sensor["sensor_id"],
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "type": sensor["type"],
        "value": generate_sensor_value(sensor),
        "unit": sensor["unit"],
        "status": "OK"
    }
    return json.dumps(message).encode("utf-8")

def publish_messages(dry_run=True):
    """Publish one message per sensor to the Pub/Sub topic or print locally."""
    if not dry_run:
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

    sensors = load_sensor_config()
    print(f"📡 Preparing {len(sensors)} sensor readings...")

    for sensor in sensors:
        message = build_message(sensor)

        if dry_run:
            # 👇 Just print messages instead of sending them
            print(f"🧪 Test Mode → {message.decode()}")
        else:
            try:
                future = publisher.publish(topic_path, message)
                print(f"✅ Sent {sensor['sensor_id']} ({sensor['type']}) → Message ID: {future.result()}")
            except Exception as e:
                print(f"❌ Error publishing {sensor['sensor_id']}: {e}")

if __name__ == "__main__":
    publish_messages(dry_run=True)
