import requests


class CreateObject:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    json = None

    def create_object(self, payload, headers):
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )

        self.json = self.response.json()
        return self.response

    def check_status_code_200(self):
        assert self.response.status_code == 200
