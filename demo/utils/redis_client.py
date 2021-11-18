import redis
import config
from redis.commands.json.path import Path
from redis import exceptions
from redis.commands.json.decoders import unstring, decode_list

# Removed due to library deprefrom rejson import Client, Path

# Connection Pooling 
connection = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, password=config.REDIS_PASSWORD, decode_responses=True, health_check_interval=30)
