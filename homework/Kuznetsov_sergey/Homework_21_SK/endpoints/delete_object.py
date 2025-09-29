import requests
from base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    def delete_object(self, object_id, headers):
        self.response = requests.delete(
            url=f'{self.url}/{object_id}',
            headers=headers
        )
        return self.response
