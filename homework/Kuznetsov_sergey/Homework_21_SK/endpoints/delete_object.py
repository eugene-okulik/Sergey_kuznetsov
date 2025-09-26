import requests


class DeleteObject:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    json = None

    def delete_object(self, object_id, headers):
        self.response = requests.delete(
            url=f'{self.url}/{object_id}',
            headers=headers
        )
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None
        return self.response

    def check_status_code_200(self):
        assert self.response.status_code == 200
