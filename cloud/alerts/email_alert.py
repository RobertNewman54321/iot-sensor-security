import os, json, base64, sendgrid
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
TO_EMAIL = os.getenv("ALERT_EMAIL")
FROM_EMAIL = "iot-alerts@iot-sensor-security.com"

def pubsub_alert(event, context):
    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
    message_data = json.loads(base64.b64decode(event["data"]).decode("utf-8"))
    msg = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject="IoT Sensor Alert",
        html_content=f"<strong>{message_data['alert']}</strong><br>{json.dumps(message_data['data'])}"
    )
    sg.send(msg)
    print("Email alert sent.")
