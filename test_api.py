from app import app


def test_valid_login():
    client = app.test_client()

    response = client.post(
        "/login",
        json={
            "username": "venkatesh",
            "password": "12345"
        }
    )

    assert response.status_code == 200
    assert response.json["status"] == "success"


def test_invalid_login():
    client = app.test_client()

    response = client.post(
        "/login",
        json={
            "username": "venkatesh",
            "password": "wrong"
        }
    )

    assert response.status_code == 401
    assert response.json["status"] == "failed"
