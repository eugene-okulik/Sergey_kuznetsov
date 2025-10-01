class BaseEndpoint:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    json = None

    def __init__(self):
        self.response = None

    def check_status_code_200(self):
        assert self.response.status_code in (200, 204)

    def check_name(self, expected_name):
        assert self.json["name"] == expected_name
