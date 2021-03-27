from common.testing import delete, get_list, get_one, patch, post

url = "/actors/"
request_b = {"name": "James", "surname": "Jones", "age": 90, "gender": "M"}
patch_b = {"gender": "F"}


def test_get_list(app, actors):
    get_list(app, url)


def test_post(app, actor):
    post(app, url, request_data=request_b)


def test_get_one(app, actor):
    get_one(app, url, faked=actor)


def test_patch(app, actor):
    patch(app, url, faked=actor, patch_data=patch_b)


def test_delete(app, actor):
    delete(app, url, faked=actor)
