from locust import task, HttpUser, between


class SubEdit(HttpUser):
    object_id = None

    def on_start(self):
        test_data = {"name": "test object", "data": {"test": 100}}

        response = self.client.post(
            "/object",
            json=test_data,
            headers={'Content-Type': 'application/json'},

        )

        if response.status_code == 200:
            self.object_id = response.json()["id"]
        else:
            response.failure(f"Fail: {response.status_code}")

    def on_stop(self):
        if self.object_id:
            self.client.delete(f"/object/{self.object_id}")

    @task(5)
    def get_all(self):
        self.client.get(
            "/object",
            headers={'Content-Type': 'application/json'}
        )

    @task(4)
    def post_sub(self):
        data = {"name": "test object", "data": {"test": 100}}
        self.client.post(
            "/object",
            json=data,
            headers={'Content-Type': 'application/json'}
        )

    @task(3)
    def put_sub(self):
        if self.object_id:
            data1 = {"name": "Sergey Kuznetsov", "data": {"test": 1}}
            self.client.put(
                f"/object/{self.object_id}",
                json=data1,
                headers={'Content-Type': 'application/json'}
            )

    @task(2)
    def patch_sub(self):
        if self.object_id:
            data2 = {"name": "Ivan Ivanov"}
            self.client.patch(
                f"/object/{self.object_id}",
                json=data2,
                headers={'Content-Type': 'application/json'}
            )

    @task(1)
    def delete_sub(self):
        if self.object_id:
            self.client.delete(
                f"/object/{self.object_id}",
                headers={'Content-Type': 'application/json'}
            )
