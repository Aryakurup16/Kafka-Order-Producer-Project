# Kafka Order Producer Project

## 📌 Project Overview

This project demonstrates a **basic Apache Kafka setup using Docker** where a **Python producer sends order data** to a Kafka topic and a **Python consumer reads and displays the stored messages**. The project is useful for beginners learning **Kafka, Docker, and event-driven data pipelines**.

The project stores order events such as **user name, item name, quantity, and order ID** using Kafka.

---

## 🏗️ Architecture

1. **Kafka Broker** – Runs inside Docker
2. **Producer (producer.py)** – Sends order messages to Kafka topic
3. **Consumer (tracker.py)** – Reads and displays order messages
4. **Docker Compose** – Manages Kafka service

---

## 📂 Project Structure

```
StreamStore/
├── docker-compose.yaml
├── producer.py
├── tracker.py
├── myenv/               # Python virtual environment
└── README.md
```

---

## ⚙️ Prerequisites

Make sure you have the following installed:

* Ubuntu / WSL (Linux)
* Python 3.8+
* Docker & Docker Compose
* pip

---

## 🐍 Python Dependencies

Install required Kafka library:

```bash
pip install confluent-kafka
```

---

## 🐳 Kafka Setup Using Docker

Start Kafka using Docker Compose:

```bash
docker compose up -d
```

Kafka will start on:

```text
localhost:9092
```

---

## 🧾 Kafka Topic

The project uses a topic named:

```text
orders
```

(Topic is auto-created if Kafka auto topic creation is enabled)

---

## 🚀 Producer Details (producer.py)

The producer:

* Generates a unique `order_id` using UUID
* Sends order details as JSON
* Uses `order_id` as Kafka message key

### Sample Data Sent

```json
{
  "order_id": "uuid",
  "user": "Uday",
  "item": "mobile",
  "quantity": 5
}
```

### Run Producer

```bash
python producer.py
```

---

## 📥 Consumer Details (tracker.py)

The consumer:

* Subscribes to the `orders` topic
* Reads messages from the beginning
* Prints order details in readable format

### Run Consumer

```bash
python tracker.py
```

### Sample Output

```text
Received Order ID: xxx
User: Uday
Item: mobile
Quantity: 5
```

---

## 🔁 Data Flow

1. Producer sends order event to Kafka
2. Kafka stores the message
3. Consumer reads the stored message
4. Order data is displayed in terminal

---

## 🛑 Stop Kafka

```bash
docker compose down
```

---

## 📝 Key Learning Outcomes

* Kafka Producer and Consumer basics
* Message key and value usage
* Docker-based Kafka setup
* JSON-based message streaming
* Event-driven architecture concept

---

## 📌 Use Cases

* Order tracking systems
* Event streaming
* Real-time data pipelines
* Microservices communication

---

## ✅ Conclusion

This project provides a **clean and beginner-friendly Kafka example** to understand how producers and consumers interact using Docker and Python. It can be extended to real-world data engineering and streaming applications.

---

📦 **Author**: Arya Kurup
📅 **Project Type**: Kafka Learning Project
🚀 **Status**: Working & Ready for Extension
