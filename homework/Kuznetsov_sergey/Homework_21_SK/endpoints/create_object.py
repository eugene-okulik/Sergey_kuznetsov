import requests
from base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):

    def create_object(self, payload, headers):
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )

        self.json = self.response.json()
        return self.response
