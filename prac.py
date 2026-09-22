import redis
import time

client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
)

client.set("fuck", "John", ex=15)

print("Immediately:", client.get("fuck"))
print("TTL:", client.ttl("fuck"))

time.sleep(16)

print("After 16 seconds:", client.get("fuck"))
print("TTL:", client.ttl("fuck"))