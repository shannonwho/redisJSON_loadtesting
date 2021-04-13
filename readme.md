# Pre-requisites
python3, pip3, virtualenv, docker, docker-compose

The local deployment needs more than 2GB of memory allocated in Docker preferences (from the system to Docker in general).  Just go into the preferences and make sure there is enough memory.  Otherwise, RS will not be able to create the database. 

cloud deployment: gcp credentials file and environment settings

# Enable a virtual environment (required)
build new virtualenv
```python3 -m venv venv```

activate your virtualenv 
```. venv/bin/activate```

run the docker compose
```docker-compose up .```

**! NOTE ! **
- Update your DB Endpoint and Locust configuration on ./local_conf folder
- If you're connecting to Redis Cloud subscription, make sure you have RedisJSON module enabled. 
- Run the "testOnJSONSet" first to load some data for other test cases.


# Overall architecture:
- REST API Servoces:
  - RedisJSON 1.0 (2.0 is coming soon!)
  - Gunicorn

- Locust Load testing:
  - Group test set
  - Event hook
  - Distributed
  - Spawn rate
  
- Visualization: (this is currently commented out)
  (This is a super-simple solution that allows us to easily visualize how our application performs on user-end as well as resource-wise.)
  - cAdvisor: API container usage monitoring (http://localhost:8080/metrics) 
  - Scrape some customized metrics from Locust.io via Prometheus (http://localhost:8089/metrics)
  - Visualize them all on Grafana (port: 3000) - template for locust is available on ./grafanaTemplate

# The REST API application:
RedisJSON Python Commands reference page: https://github.com/RedisJSON/redisjson-py/blob/master/API.md 

The REST API is based on RedisJSON module for basic JSON Operations:
- GET
  - Get object by key 
  - Get the value of a field by key and field's name
  - Get the sub-document(nested object) by key and field's name
- POST
    - static fields 
    - Randomly assigned JSON with no subdocument(nested obejct) 
- PUT
  - Update a field on the RedisJSON 
  - Append new object/value into an existing JSON object
  - Increase/Multiplying a numeric item in the JSON

Some additional basic APIs based on String and Hash is also available, ready for some comparison testings. 

# The locust Test: 

## Main test cases:

- READ entire JSON objects by key
- READ specific field within a JSON object by key
- READ the list of field name under a field/object by the key
- WRITE simple JSON without array and subdocument 
- WRITE complex JSON with array and subdocument 
- UPDATE a part of JSON objects (multiply/increase)
- APPEND new items into an array of the JSON objects 
- ... pretty much any client side actions you would like to mimic 


## Notes on how Locust do distributed tests:
    In general, in Locust, it’s the master who is in charge of things like spawning new locusts (users), collecting and presenting results, running some preparatory tasks, etc. So, it appears like we need some code that runs on the master and will: get the data from the disk communicate with the workers, to exchange data


## Understand Locust statistics
1. The relationship between Number of users to simulate Vs Hatch Rate (Users Spawned/Second): 
   You define a number of user (locust) you want to spawn, at a given rate. This gives you control of how fast users flood in. For exemple, 100 user at 5 user/sec, it will take 100/5=20 second to reach 100 user.
   Use this command to adjust the number of workers:

        ``` docker-compose up --scale locust_worker=num_of_workers ```

2. The meaning of Median (ms), Average (ms), Content Size(bytes):
   
   Median, average response time of a given api endpoint, over the entire testing time. Content size is the size of the returned data from the endpoint.
   
Note: if you want to generate your own load pattern that's outside of simply adjusting user and spawned/second, you can customize it yourself - https://docs.locust.io/en/stable/generating-custom-load-shape.html#generating-a-custom-load-shape 

More details about stats are also avaialble on '/stats/requests', or refer to the 'LocustPrometheusCollector' function for scrapting those stats out to other timeseries DB

3. You alos have the options to calculate the number of percentile: get_current_response_time_percentile 


## Other components within the Locust tests: 
- Use faker to generate a user info in json:https://faker.readthedocs.io/en/master/ 
- Generate different propotion on each test by assigning the weight, eg. @task ( level of the priority)
- For load testing you might want to make one of the requests execute more often than the others, Locust allows you to do it by defining the weight for each task. 
- Grafana dashboard for more detailed visualization on all statistics 
- Gunicorn to optimize flask app performence 
