from django_rq import job
import time


@job('default', timeout=1000)
def do_something():
    time.sleep(100)
