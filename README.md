# Microservice Log Aggregator

A distributed system designed to simulate real-world log collection across multiple services. This project demonstrates the transition from monolithic scripts to a decoupled, event-driven architecture.

## 🚀 Key Features
* **Event-Driven Architecture:** Uses **RabbitMQ** as a message broker to decouple the log producer from the consumer.
* **Asynchronous Processing:** Logs are generated and queued without blocking the main application flow.
* **Data Persistence:** A dedicated Consumer service processes incoming JSON payloads and archives them into a **SQLite** database.
* **Containerised Infrastructure:** RabbitMQ is deployed via **Docker**, ensuring a consistent and portable environment.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Messaging:** RabbitMQ (pika)
* **DevOps:** Docker
* **Database:** SQLite / SQLAlchemy
* **Environment:** Virtual Environments (venv)

## Key Skills
* How to manage inter-service communication using the **Publisher/Subscriber** pattern.
* Handling **binary data serialisation** and JSON parsing between independent services.
* Configuring and managing **Docker containers** for backend infrastructure.