from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(1, 2)

    @task(1)
    def load_test(self):
        self.client.get("http://127.0.0.1:8001/")

    @task(1)
    def load_test(self):
        self.client.get("http://127.0.0.1:8001/about")

    @task(1)
    def load_test(self):
        self.client.get("http://127.0.0.1:8001/contacts")
