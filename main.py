import redis
import json
from fake_database import inventory

client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
)

def get_inventory(inventory_id: int):

    cache_key = f"inventory:{inventory_id}"

    # 1. Check Redis
    cached_inventory = client.get(cache_key)

    if cached_inventory:
        print("CACHE HIT")
        return json.loads(cached_inventory)

    print("CACHE MISS")

    # 2. Get data from the database
    item = inventory.get(inventory_id)

    if item is None:
        return None

    # 3. Store database result in Redis
    client.set(
        cache_key,
        json.dumps(item),
        ex=30
    )

    # 4. Return database result
    return item


def stock_out(inventory_id: int, quantity: int):

    item = inventory.get(inventory_id)

    if item is None:
        return None

    if item["quantity"] < quantity:
        return None

    item["quantity"] -= quantity

    return item