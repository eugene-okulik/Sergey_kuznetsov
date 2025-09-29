import requests
from base_endpoint import BaseEndpoint


class PatchObject(BaseEndpoint):

    def patch_object(self, payload, headers, object_id):
        self.response = requests.patch(
            url=f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    def check_name(self, expected_name):
        assert self.json["name"] == expected_name
