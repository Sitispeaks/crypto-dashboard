# crypto-dashboard
## Realtime crypto-dashboard made with celery, redis and websockets.
This app fetches data peiodically from external APIs using Celery Workers.

How Celery works, and why you need Redis (or RabbitMQ):

1. Celery provides workers. A worker is a function that executes our tasks. A Task is a function that we define in our Django Project.
2. And Django somehow should pass our tasks (that we defined), to these workers... 
3. And usually brokers are used to do it.
4. A broker - is a task queue that stores our tasks. It's a data structure.
5. After the Broker gets a task from a Django app, it puts the task in a queue... and then it starts to pass these tasks to workers.
6. After a worker completes its task it will put the result in a so called Results Backend. And then we can fetch these results from a Django app. Usually the same broker is used to store the results.

<b>After getting the data, it is then sent to frontend via socket connection using django-channels.Thats why we don't have to refresh the browser to get data.</b>

# UI
![updated_dasboard](https://user-images.githubusercontent.com/60188244/130830842-0fa5be21-e281-4efe-a7b2-a29916b61d95.png)


<!-- # DEMO -->

<!-- https://user-images.githubusercontent.com/60188244/130129556-66800d53-1dc5-4107-af40-f61ff5ff6160.mp4 -->



### Install redis
https://github.com/tporadowski/redis/releases

### Or you can use redis images in docker for the same
 ```docker pull redislabs/redis```
