headers = {'Content-Type': 'application/json'}


def test_object(create_object_endpoint):
    test_data = {"name": "test object", "data": {"test": 100}}
    create_object_endpoint.create_object(test_data, headers)
    create_object_endpoint.check_status_code_200()


def test_update_object(create_object_precondition, update_object_endpoint):
    body = {"name": "Sergey Kuznesov edit", "data": {"test": 1}}
    update_object_endpoint.update_object(body, headers, create_object_precondition)
    update_object_endpoint.check_status_code_200()
    update_object_endpoint.check_name("Sergey Kuznesov edit")
    update_object_endpoint.check_data({"test": 1})


def test_patch_object(create_object_precondition, patch_object_endpoint):
    body = {"name": "Alex Dou"}
    patch_object_endpoint.patch_object(body, headers, create_object_precondition)
    patch_object_endpoint.check_status_code_200()
    patch_object_endpoint.check_name("Alex Dou")


def test_delete_object(create_object_precondition, delete_object_endpoint):
    delete_object_endpoint.delete_object(create_object_precondition, headers)
    delete_object_endpoint.check_status_code_200()
