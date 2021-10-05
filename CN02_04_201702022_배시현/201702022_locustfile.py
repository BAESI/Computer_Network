import time
from locust import HttpUser, task, between, TaskSet

class QuickstartUser(HttpUser):
    wait_time = between(5,15)


    @task
    def Mytask(self):
        response = self.client.get("/")

