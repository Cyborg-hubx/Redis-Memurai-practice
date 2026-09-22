import redis
import json

client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
)

product = {
    "product_id": 15,
    "name": "Mechanical Keyboard",
    "price": 501.17,
    "stock": 20
}

# Convert dict → JSON string
product_json = json.dumps(product)

client.set(
    "product:15",
    product_json,
    ex=30
)

cached_data = client.get("product:15")




cached_product = json.loads(cached_data)

print(cached_product)
print(type(cached_product))
print(cached_product["name"])





print(cached_data)
print(type(cached_data))