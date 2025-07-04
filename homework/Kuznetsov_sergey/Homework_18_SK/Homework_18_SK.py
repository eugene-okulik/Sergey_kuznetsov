import requests

def new_post():
    body = {
        "name": "Sergey Kuznetsov",
        "data": {"test": 0}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://objapi.course.qa-practice.com/object",
                             json = body,
                             headers=headers)

    return response.json()["id"]

def put_a_post():
    post_id = new_post()
    body = {
        "name": "Sergey Kuznesov edit",
        "data": {"test": 1}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"http://objapi.course.qa-practice.com/object/{post_id}",
                             json = body,
                             headers=headers)
    print(response.text)

put_a_post()

def patch_a_post():
    post_id = new_post()
    body = {
        "name": "Alex Dou",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f"http://objapi.course.qa-practice.com/object/{post_id}",
                             json = body,
                             headers=headers)
    print(response.text)

patch_a_post()

def delete_a_post():
    post_id = new_post()
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{post_id}")
    print(response.text)


delete_a_post()
