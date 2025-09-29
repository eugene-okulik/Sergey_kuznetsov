import requests
from status_checker import CheckerStatus
from parameters import Parameters


class PatchObject(Parameters, CheckerStatus):

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
