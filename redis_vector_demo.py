import redis

r = redis.Redis.from_url(
    "rediss://default:deTfaj2RioN4OrvexDQKuZdUmDbaMJXB@redis-17408.c283.us-east-1-4.ec2.redns.redis-cloud.com:17408/0",
    ssl=True
)

print("🔁 Redis ping:", r.ping())
