# from
# https://kb.objectrocket.com/redis/create-a-simple-task-queue-with-flask-and-redis-1467
from flask import Flask, request
import redis
from rq import Queue
import time

app = Flask(__name__)
r = redis.Redis()
q = Queue(connection=r)

def task_in_background(t):  
    delay = 1  
    print("Running Task")  
    print("Simulates the {delay} seconds")  

    time.sleep(delay)  
    print(len(t))  
    print("Completed Task")  

    return len(t)

@app.route("/task")  
def add_task():  
    if request.args.get("t"):  
        job= que.enqueue(task_in_background, request.args.get("t"))  
        q_len = len(q)  
        return f"The task {job.id} is added into the task queue at {job.enqueued_at}. {q_len} task in the queue"  
  return "Task Queue with Flask"  
 
if __name__ == "__main__":  
    app.run()
