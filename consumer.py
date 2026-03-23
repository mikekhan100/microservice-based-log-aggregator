import pika
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# --- DATABASE SETUP ---
# 1. Define the 'Engine' (the connection to the file)
engine = create_engine('sqlite:///logs.db')

# 2. Define the 'Base' (the blueprint for the tables)
Base = declarative_base()

# 3. Define the 'Table' (the structure of the logs)
class LogEntry(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    level = Column(String)
    service = Column(String)
    message = Column(String)
    received_at = Column(DateTime, default=datetime.utcnow)

# 4. Call create_all on the metadata
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def save_to_db(data):
    """Helper function to save the log dictionary to SQLite"""
    session = Session()
    try:
        new_log = LogEntry(
            timestamp=data.get("timestamp"),
            level=data.get("level"),
            service=data.get("service"),
            message=data.get("message")
        )
        session.add(new_log)
        session.commit()
    except Exception as e:
        print(f" Error saving to DB: {e}")
        session.rollback()
    finally:
        session.close()

# --- RABBITMQ CALLBACK ---
def process_log(ch, method, properties, body):
    # Decode the binary message from RabbitMQ
    log_data = json.loads(body.decode())
    
    # Save it to the database
    save_to_db(log_data)
    
    print(f" [db] Saved log from {log_data.get('service')}")

# --- CONNECTION SETUP ---
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='log_queue')

# Tell RabbitMQ to use the 'process_log' function
channel.basic_consume(queue='log_queue', on_message_callback=process_log, auto_ack=True)

print(" [*] Consumer started. Saving logs to logs.db. Press CTRL+C to exit.")
channel.start_consuming()