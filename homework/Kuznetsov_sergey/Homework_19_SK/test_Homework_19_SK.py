import pytest
import requests


@pytest.fixture(params=[
    {"name": "Object 1", "data": {"test": 1}},
    {"name": "Object 2", "data": {"test": 10}},
    {"name": "Object 3", "data": {"test": 5}}
])


def new_post(request):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        "http://objapi.course.qa-practice.com/object",
        json=request.param,
        headers=headers)

    post_id = response.json()["id"]
    print(post_id)
    yield post_id
    requests.delete(f"http://objapi.course.qa-practice.com/object/{post_id}")


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


@pytest.mark.medium
def test_put_a_post(new_post, start_end):
    body = {
        "name": "Sergey Kuznesov edit",
        "data": {"test": 1}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{new_post}",
        json=body,
        headers=headers)
    print(response.text)
    assert response.status_code == 200
    assert response.json()["name"] == "Sergey Kuznesov edit"
    assert response.json()["data"] == {"test": 1}


@pytest.mark.critical
def test_patch_a_post(new_post):
    body = {
        "name": "Alex Dou",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{new_post}",
        json=body,
        headers=headers)
    print(response.text)
    assert response.status_code == 200
    assert response.json()["name"] == "Alex Dou"


def test_delete_a_post(new_post):
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{new_post}")
    print(response.text)
    assert response.status_code == 200
