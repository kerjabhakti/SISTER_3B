###
# addTask.py :Executing a simple task
###

from celery import Celery

app = Celery('addTask', broker='amqp://guest@localhost//')


@app.task
def add(x, y):
    return x + y


def add1(x, y):
    return x + y
