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

Update your configuration for Redis: it's located in ./local_conf folder


# Overall architecture:
- REST API Servoces:
  - RedisJSON 1.0
  - Gunicorn

- Locust Load testing:
  - Group test set
  - Event hook
  - Distributed
  - Spawn rate
  
- Visualization: (This is a super-simple solution that allows us to easily visualize how our application performs on user-end as well as resource-wise.)
  - cAdvisor: API container usage monitoring (http://localhost:8080/metrics) 
  - Scrape some customized metrics from Locust.io via Prometheus (http://localhost:8089/metrics)
  - Visualize them all on Grafana (port: 3000)

# The REST API application:

The REST API is based on RedisJSON module for basic JSON Operations:
- GET
  - Get object by key 
  - Get the value of a field by key and field's name
  - Get the sub-document(nested object) by key and field's name
- POST
  - Small size object (200-300Bytes)
    - static fields 
    - Randomly assigned JSON with no subdocument(nested obejct) 
  - Big size object (1000-2000bytes)
    - Static fields
    - Nested JSON with array and subdocument
- PUT
  - Update a field on the RedisJSON 
  - Append new object/value into an existing JSON object
  - Increase/Multiplying a numeric item in the JSON


# The locust Test: 

## Main test cases:

- READ entire JSON objects by key
- READ specific field within a JSON object by key
- READ the list of field name under a field/object by the key
- WRITE simple JSON without array and subdocument 
- WRITE complex JSON with array and subdocument 
- UPDATE a part of JSON objects (multiply/increase)
- APPEND new items into an array of the JSON objects 
- ... 


## Notes on how Locust do distributed tests:
In general, in Locust, it’s the master who is in charge of things like spawning new locusts (users), collecting and presenting results, running some preparatory tasks, etc. So, it appears like we need some code that runs on the master and will:
get the data from the disk
communicate with the workers, to exchange data


## Understand Locust statistics
1. The relationship between Number of users to simulate Vs Hatch Rate (Users Spawned/Second): 
   You define a number of user (locust) you want to spawn, at a given rate. This gives you control of how fast users flood in. For exemple, 100 user at 5 user/sec, it will take 100/5=20 second to reach 100 user.
   Use this command to adjust the number of workers:

        ``` docker-compose up --scale locust_worker=num_of_workers ```

2. The meaning of Median (ms), Average (ms), Content Size(bytes):
   
   Median, average response time of a given api endpoint, over the entire testing time. Content size is the size of the returned data from the endpoint.
   
Note: if you want to generate your own load pattern that's outside of simply adjusting user and spawned/second, you can customize it yourself - https://docs.locust.io/en/stable/generating-custom-load-shape.html#generating-a-custom-load-shape 

More details about stats are also avaialble on '/stats/requests'

3. You have the options to calculate the number of percentile 

get_current_response_time_percentile 
## Other components within the Locust tests: 
- Use faker to generate a user info in json:https://faker.readthedocs.io/en/master/ 
- Generate different propotion on each test by assigning the weight, eg. @task ( level of the priority)
- For load testing you might want to make one of the requests execute more often than the others, Locust allows you to do it by defining the weight for each task. 
- Grafana dashboard for more detailed visualization on all statistics 
