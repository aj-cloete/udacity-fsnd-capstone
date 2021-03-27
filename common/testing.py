from factory.alchemy import SQLAlchemyModelFactory

from database.db import Session


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = "commit"

    _original_params = {}


def get_list(app, url):
    response = app.test_client().get(url)
    assert response.status_code == 200
    assert isinstance(response.json, list)


def post(app, url, request_data):
    response = app.test_client().post(url, json=request_data)
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    for k, v in request_data.items():
        assert response.json.get(k) == v


def get_one(app, url, faked):
    response = app.test_client().get(f"{url}{faked.uuid}")
    assert response.status_code == 200
    assert isinstance(response.json, dict)


def patch(app, url, faked, patch_data):
    response = app.test_client().patch(f"{url}{faked.uuid}", json=patch_data)
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    for k, v in patch_data.items():
        assert response.json.get(k) == v


def delete(app, url, faked):
    response = app.test_client().delete(f"{url}{faked.uuid}")
    assert response.status_code == 200
    assert isinstance(response.json, str)
    response2 = app.test_client().get(f"{url}{faked.uuid}")
    assert response2.json == {}
