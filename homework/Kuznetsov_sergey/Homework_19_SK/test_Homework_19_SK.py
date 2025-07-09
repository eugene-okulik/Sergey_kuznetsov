import pytest
import requests


BASE_URL = "http://objapi.course.qa-practice.com/object"
HEADERS = {'Content-Type': 'application/json'}


@pytest.fixture(scope="session")
def start_end():
    print("\nStart testing")
    yield
    print("Testing completed")


@pytest.fixture(autouse=True)
def test_setup_teardown():
    print("\nbefore test")
    yield
    print("after test")


@pytest.fixture
def test_object(request):
    test_data = {"name": "test object", "data": {"test": 100}}
    response = requests.post(BASE_URL, json=test_data, headers=HEADERS)
    assert response.status_code == 200
    object_id = response.json()["id"]
    yield object_id
    requests.delete(f"{BASE_URL}/{object_id}")


@pytest.mark.parametrize("test_data", [
    {"name": "Object 1", "data": {"test": 1}},
    {"name": "Object 2", "data": {"test": 10}},
    {"name": "Object 3", "data": {"test": 5}}
])
@pytest.mark.critical
def test_post_a_post(test_data, start_end):
    response = requests.post(BASE_URL, json=test_data, headers=HEADERS)

    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
    assert response_data["name"] == test_data["name"]
    assert response_data["data"] == test_data["data"]
    print(response.text)
    requests.delete(f"http://objapi.course.qa-practice.com/object/{response_data['id']}")


@pytest.mark.medium
def test_put_a_post(test_object):
    body = {
        "name": "Sergey Kuznesov edit",
        "data": {"test": 1}
    }
    response = requests.put(f"{BASE_URL}/{test_object}", json=body, headers=HEADERS)
    print(response.text)
    assert response.status_code == 200
    assert response.json()["name"] == "Sergey Kuznesov edit"
    assert response.json()["data"] == {"test": 1}


@pytest.mark.critical
def test_patch_a_post(test_object):
    body = {
        "name": "Alex Dou",
    }
    response = requests.patch(f"{BASE_URL}/{test_object}", json=body, headers=HEADERS)
    print(response.text)
    assert response.status_code == 200
    assert response.json()["name"] == "Alex Dou"


def test_delete_a_post(test_object):
    response = requests.delete(f"{BASE_URL}/{test_object}")
    print(response.text)
    assert response.status_code == 200
