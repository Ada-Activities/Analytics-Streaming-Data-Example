import json
import time
import random
import boto3
import uuid

# Requires the aws cli client to have been installed and an active login session
# run
#
# aws login
#
# to login or or refresh your session

STREAM_NAME = "stationery-streaming-events"  # adjust for your created stream
REGION = "us-west-2"  # adjust to match your setup

PRODUCTS = [
    {"product_id": "P001", "product_name": "Ballpoint Pen", "category": "pens", "price": 1.99},
    {"product_id": "P002", "product_name": "Fountain Pen", "category": "pens", "price": 24.99},
    {"product_id": "P003", "product_name": "Spiral Notebook", "category": "notebooks", "price": 4.99},
    {"product_id": "P004", "product_name": "Leather Journal", "category": "notebooks", "price": 18.99},
    {"product_id": "P005", "product_name": "Sticky Notes (Pack)", "category": "office", "price": 3.49},
    {"product_id": "P006", "product_name": "Highlighter Set", "category": "markers", "price": 6.99},
    {"product_id": "P007", "product_name": "Mechanical Pencil", "category": "pencils", "price": 5.49},
    {"product_id": "P008", "product_name": "Washi Tape", "category": "craft", "price": 2.99},
]

STORES = ["store-001", "store-002", "store-003", "online"]

EVENT_TYPES = ["item_viewed", "item_added_to_cart", "purchase_completed", "item_returned"]

def generate_event():
    product = random.choice(PRODUCTS)
    quantity = random.randint(1, 4)
    return {
        "event_id": str(uuid.uuid4()),
        "event_type": random.choice(EVENT_TYPES),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "store_id": random.choice(STORES),
        "customer_id": f"cust-{random.randint(1000, 9999)}",
        "product_id": product["product_id"],
        "product_name": product["product_name"],
        "category": product["category"],
        "unit_price": product["price"],
        "quantity": quantity,
        "total_value": round(product["price"] * quantity, 2)
    }

def send_events(stream_name, region, count=100, delay=0.2):
    client = boto3.client("kinesis", region_name=region)
    print(f"Sending events to stream: {stream_name}\n")

    for i in range(count):
        event = generate_event()
        response = client.put_record(
            StreamName=stream_name,
            Data=json.dumps(event),
            PartitionKey=event["store_id"]
        )
        print(f"[{i+1}/{count}] {event['event_type']} | {event['product_name']} "
              f"| {event['store_id']} | ${event['total_value']}")
        time.sleep(delay)

    print("\nDone. Waiting for Firehose to flush to S3 (~5s buffer)...")

if __name__ == "__main__":
    send_events(STREAM_NAME, REGION, count=100, delay=0.2)