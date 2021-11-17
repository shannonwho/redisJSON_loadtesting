import redis
import config
# Removed due to library deprefrom rejson import Client, Path

# Connection Pooling 
connection = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, password=config.REDIS_PASSWORD, decode_responses=True, health_check_interval=30)
