import requests


class UpdateObject:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    json = None

    def update_object(self, payload, headers, object_id):
        self.response = requests.put(
            url=f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    def check_status_code_200(self):
        assert self.response.status_code == 200

    def check_name(self, expected_name):
        assert self.json["name"] == expected_name

    def check_data(self, expected_data):
        assert self.json["data"] == expected_data
