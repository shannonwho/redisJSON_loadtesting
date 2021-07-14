import redis
import config
from rejson import Client, Path

# Connection Pooling 
connection = Client(host='redis', port=6379, decode_responses=True, health_check_interval=30)
