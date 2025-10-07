import os, json, base64
from cloudevents.http import CloudEvent
import functions_framework
from google.cloud import pubsub_v1

# Threshold rules
THRESHOLDS = {
    "temperature": {"max": 80.0},
    "vibration": {"max": 12.0},
    "pressure": {"max": 300.0},
}

ALERT_TOPIC = os.getenv("ALERT_TOPIC", "")  # optional fan-out topic

def _parse(cloud_event: CloudEvent):
    raw = base64.b64decode(cloud_event.data["message"]["data"]).decode("utf-8")
    try:
        return json.loads(raw)
    except Exception:
        return {"value": raw}

def _is_anomaly(msg):
    t = str(msg.get("type", "")).lower()
    try:
        v = float(msg.get("value"))
    except Exception:
        return False, "non-numeric"
    rule = THRESHOLDS.get(t, {})
    if "max" in rule and v > rule["max"]:
        return True, f"{v}>{rule['max']}"
    return False, ""

@functions_framework.cloud_event
def subscribe(cloud_event: CloudEvent):
    msg = _parse(cloud_event)
    abnormal, reason = _is_anomaly(msg)
    if abnormal:
        print(f"⚠️ Anomaly detected: {msg} → {reason}")
        if ALERT_TOPIC:
            pub = pubsub_v1.PublisherClient()
            from google.auth import default
            project_id = default()[1]
            topic = pub.topic_path(project_id, ALERT_TOPIC)
            pub.publish(topic, json.dumps({**msg, "alert": True, "reason": reason}).encode("utf-8"))
    else:
        print(f"✅ Normal reading: {msg}")
