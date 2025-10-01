import pytest
import requests
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.patch_object import PatchObject
from endpoints.update_object import UpdateObject

BASE_HEADERS = {"Content-Type": "application/json"}


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def create_object_precondition(request, create_object_endpoint, delete_object_endpoint):
    body = {"name": "test object", "data": {"test": 100}}
    create_object_endpoint.create_object(body, BASE_HEADERS)
    object_id = create_object_endpoint.json["id"]

    yield object_id

    if request.node.name != "test_delete_object":
        delete_object_endpoint.delete_object(object_id, BASE_HEADERS)
        assert delete_object_endpoint.response.status_code in (200, 204)


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()
