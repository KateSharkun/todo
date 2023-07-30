import pytest
import main


@pytest.fixture()
def app():
    with main.app.app_context():
        app = main.app
        app.config.update({
            "TESTING": True,
        })
        yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_index(client):
    response = client.get('/')
    assert b'Hi' in response.data








