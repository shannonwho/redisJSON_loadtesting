import redis
import config
from rejson import Client, Path

connection = Client(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)
