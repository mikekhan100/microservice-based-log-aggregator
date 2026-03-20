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

# --- Connection Setup ---
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

# Ensure the queue exists
channel.queue_declare(queue='log_queue')

# Tell RabbitMQ which function to call when a message is received
channel.basic_consume(queue='log_queue',
                        on_message_callback=process_log, 
                        auto_ack=True)

print(" [*] Waiting for logs. To exit press CTRL+C")
channel.start_consuming()
