from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_similarity(self):
        self.client.post("/api/similarity", json={
            "prompt1": "Make a list of employees at my company",
            "prompt2": "Make a list of employees at my company please",
            "metric": "cosine"
        })