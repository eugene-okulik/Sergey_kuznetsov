import requests
from status_checker import CheckerStatus
from parameters import Parameters


class CreateObject(Parameters, CheckerStatus):

    def create_object(self, payload, headers):
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )

        self.json = self.response.json()
        return self.response

    def delete_object(self, object_id, headers):
        url = f"{self.url}/{object_id}"
        response = requests.delete(url, headers=headers)
        assert self.response.status_code == 200
        return response
