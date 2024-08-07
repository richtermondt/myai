def test_app_exists(app):
    assert app is not None


def test_app_is_testing(app):
    assert app.config['TESTING']


def test_database_initialization(client):
    response = client.get('/')
    assert response.status_code == 200


def test_secret_key(app):
    assert app.config['SECRET_KEY'] == 'test_secret_key'
