import time, json, random
from google.cloud import pubsub_v1

PROJECT_ID = "iot-sensor-security"
TOPIC_ID = "iot-sensor"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

def generate_data():
    return {
        "sensor_id": "temp-001",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "type": "temperature",
        "value": round(random.uniform(20.0, 90.0), 2),
        "unit": "°C"
    }

def main():
    while True:
        data = json.dumps(generate_data()).encode("utf-8")
        publisher.publish(topic_path, data)
        print(f"Published: {data}")
        time.sleep(5)

if __name__ == "__main__":
    main()
