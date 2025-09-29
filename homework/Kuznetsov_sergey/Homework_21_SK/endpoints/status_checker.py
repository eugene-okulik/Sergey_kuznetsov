class CheckerStatus:

    def __init__(self):
        self.response = None

    def check_status_code_200(self):
        assert self.response.status_code == 200
