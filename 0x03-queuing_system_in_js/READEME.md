# Queuing System in JS

This project explores the implementation of a queuing system in JavaScript using Redis and Kue. It covers various aspects of interacting with a Redis server, managing job queues, and building a basic Express.js application to handle requests.

## Learning Objectives

* How to run a Redis server
* How to perform basic operations with the Redis client
* How to use a Redis client with Node.js
* How to store hash values in Redis
* How to handle asynchronous operations with Redis
* How to use Kue as a queue system
* How to build an Express.js app interacting with a Redis server and queue

## Requirements

* Ubuntu 18.04
* Node 12.x
* Redis 5.0.7

## Files

* **0-redis_client.js:** Connects to a Redis server and logs the connection status.
* **1-redis_op.js:** Performs basic Redis operations (set and get).
* **2-redis_op_async.js:** Uses async/await for Redis operations.
* **4-redis_advanced_op.js:** Stores and retrieves hash values in Redis.
* **5-subscriber.js:** Subscribes to a Redis channel and listens for messages.
* **5-publisher.js:** Publishes messages to a Redis channel.
* **6-job_creator.js:** Creates jobs and adds them to a Kue queue.
* **6-job_processor.js:** Processes jobs from a Kue queue.
* **7-job_creator.js:** Creates jobs with progress tracking.
* **7-job_processor.js:** Processes jobs with error handling and progress tracking.
* **8-job.js:** Defines a function for creating jobs with progress and error handling.
* **8-job.test.js:** Contains tests for the job creation function.
* **9-stock.js:** Implements a product reservation API with Redis.
* **100-seat.js:** Implements a seat reservation API with Redis and Kue.

## How to Run

1.  Install Redis.
2.  Start the Redis server.
3.  Run the desired script using `npm run dev <script_name>`.
4.  For scripts with publishers and subscribers or job creators and processors, run each script in a separate terminal.

## Author

Collin Morudi
