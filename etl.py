import os, json
import psycopg2
from confluent_kafka import Consumer
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

KAFKA_BROKER = os.getenv("KAFKA_BROKER")
POSTGRES_URL = os.getenv("POSTGRES_URL")

conn = psycopg2.connect(POSTGRES_URL)
conn.autocommit = True

cur = conn.cursor()

conf = {
    "bootstrap.servers" : KAFKA_BROKER,
    "group.id": "etl-consumer",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(conf)

consumer.subscribe(["payments-topic"])

print("ETL running. Await messages")

try:
    while True:
        msg = consumer.poll(1.0)
        
        if msg is None:
            continue
        if msg.error():
            print("Error", msg.error())
            continue
        
        raw = msg.value().decode("utf-8")
        data = json.loads(raw)
        
        payment_id = data["paymentId"]
        payment_date =   datetime.fromisoformat(data["paymentDate"])  
        payment_amount = data["amount"]
        payment_method = data["method"]
        
        cur.execute(
                """
                INSERT INTO payments (payment_id, payment_date, amount, method)
                VALUES (%s,%s,%s,%s)
                ON CONFLICT (payment_id) DO NOTHING    
                """,
                (payment_id, payment_date, payment_amount, payment_method)
                ) 
                
                    
        
        print(f"Payment saved {payment_id}")

except KeyboardInterrupt:
    pass

finally:
    consumer.close()
    cur.close()
    conn.close()