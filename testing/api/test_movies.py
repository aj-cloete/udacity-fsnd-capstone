from common.testing import delete, get_list, get_one, patch, post

url = "/movies/"
request_b = {"title": "The Lion King", "release_date": "1994-06-05"}
patch_b = {"title": "The Tiger King"}


def test_get_list(app, movies):
    get_list(app, url)


def test_post(app, movie):
    post(app, url, request_data=request_b)


def test_get_one(app, movie):
    get_one(app, url, faked=movie)


def test_patch(app, movie):
    patch(app, url, faked=movie, patch_data=patch_b)


def test_delete(app, movie):
    delete(app, url, faked=movie)


#
# def test_get_list(app):
#     response = app.test_client().get(url)
#     assert response.status_code == 200
#     assert isinstance(response.json, list)
#
#
# def test_post(app):
#     request_body = {"title": "The Lion King", "release_date": "1994-06-05"}
#     response = app.test_client().post(url, json=request_body)
#     assert response.status_code == 200
#     assert isinstance(response.json, dict)
#     uuid = response.json.get("uuid")
#     for k, v in request_body.items():
#         assert response.json.get(k) == v
#
#
# def test_get_one(app, movie):
#     uuid = movie.uuid
#     response = app.test_client().get(f"{url}{uuid}")
#     assert response.status_code == 200
#     assert isinstance(response.json, dict)
#
#
# def test_patch(app, movie):
#     request_body = {"title": "The Tiger King"}
#     uuid = movie.uuid
#     response = app.test_client().patch(f"{url}{uuid}", json=request_body)
#     print([response.__dict__[k] for k in response.__dict__])
#     assert response.status_code == 200
#     assert isinstance(response.json, dict)
#     for k, v in request_body.items():
#         assert response.json.get(k) == v
#
#
# def test_delete(app, movie):
#     uuid = movie.uuid
#     response = app.test_client().delete(f"{url}{uuid}")
#     assert response.status_code == 200
#     assert isinstance(response.json, str)
#     response2 = app.test_client().get(f"{url}{uuid}")
#     assert response2.json == {}
