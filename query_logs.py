from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Import the class you already defined in consumer.py
from consumer import LogEntry

# 1. Connect to the SQLite database
engine = create_engine('sqlite:///logs.db')
Session = sessionmaker(bind=engine)
session = Session()

print("\n--- DATABASE QUERY REPORT ---")

# 2. Total Count
total_logs = session.query(LogEntry).count()
print(f"Total logs archived: {total_logs}")

# 3. Filtered Query: Let's find all the 'ERROR' logs
errors = session.query(LogEntry).filter(LogEntry.level == "ERROR").all()

print(f"Total Errors found: {len(errors)}")
print("-" * 30)

# 4. Display the most recent 5 errors
for log in errors[-5:]:
    print(f"[{log.timestamp}] SERVICE: {log.service} | MSG: {log.message}")

print("-" * 30)

session.close()