import pika
import json

def process_log(ch, method, properties, body):
    """
    Callback function that runs when a message is received from RabbitMQ
    """
    # 1. Decode the binary message into a string, then a dictionary
    log_data = json.loads(body.decode())

    # 2. Extract the data
    timestamp = log_data.get("timestamp")
    level = log_data.get("level")
    service = log_data.get("service")
    message = log_data.get("message")

    # 3. Create a structured log entry (for demonstration, it is printed)
    print(f"[{timestamp}] {level} from {service}: {message}")