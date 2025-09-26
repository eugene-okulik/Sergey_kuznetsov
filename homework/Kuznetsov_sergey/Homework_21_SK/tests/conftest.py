import pytest
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
def create_object_precondition(create_object_endpoint):
    body = {"name": "test object", "data": {"test": 100}}
    create_object_endpoint.create_object(body, BASE_HEADERS)
    object_id = create_object_endpoint.json["id"]
    return object_id


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()
