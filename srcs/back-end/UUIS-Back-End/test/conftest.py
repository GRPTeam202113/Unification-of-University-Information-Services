import pytest
from app import app

@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()

    def teardown():
        app.config['TESTING'] = False
    request.addfinalizer(teardown)

    return client
