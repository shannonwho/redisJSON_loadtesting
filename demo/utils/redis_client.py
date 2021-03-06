import redis
import config
from rejson import Client, Path

# Connection Pooling 
connection = Client(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True, health_check_interval=30)
