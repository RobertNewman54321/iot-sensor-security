### Table: sensor_readings
| Field | Type | Description |
|-------|------|--------------|
| sensor_id | STRING | Unique ID for the sensor |
| timestamp | TIMESTAMP | UTC timestamp of reading |
| type | STRING | Sensor type (e.g., temperature) |
| value | FLOAT | Sensor reading value |
| unit | STRING | Measurement unit |

### Table: anomalies
| Field | Type | Description |
|-------|------|--------------|
| alert | STRING | Description of triggered alert |
| value | FLOAT | Sensor value that triggered alert |
| timestamp | TIMESTAMP | Time alert occurred |
