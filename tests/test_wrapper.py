import os


def test_get_random_activity(client, app):
    response = client.get('/api/activity/')
    assert len(response.json["key"]) != 0


def test_get_impossible_activity(client, app):
    response = client.get('/api/activity/?price=2')
    assert response.json["message"]


def test_get_possible_activity(client, app):
    response = client.get('/api/activity/?participants=2&price=0.1')
    assert len(response.json["key"]) != 0


def test_get_last_activities(client, app):
    response = client.get('/api/get_activities/')
    assert len(response.json) == 2


def test_delete_database():
    os.remove("test.db")
    assert os.path.exists("test.db") is False
