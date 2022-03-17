import pytest
from app import app

@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    # 得到测试客户端
    client = app.test_client()

    def teardown():
        app.config['TESTING'] = False
    # 执行回收函数
    request.addfinalizer(teardown)

    return client
