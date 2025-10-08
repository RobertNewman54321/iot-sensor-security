from google.cloud import pubsub_v1
import json

def publish_message(project_id, topic_id, message):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    publisher.publish(topic_path, json.dumps(message).encode("utf-8"))
    print(f"Published message to {topic_id}")

if __name__ == "__main__":
    project_id = "iot-sensor-security"
    topic_id = "iot-sensor"
    sample_message = {"sensor_id": "temp-001", "value": 67.8}
    publish_message(project_id, topic_id, sample_message)
