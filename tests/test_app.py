from app import app


def test_homepage_shows_initial_development_message():
    app.config["TESTING"] = True
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert "NetMonitor" in response.get_data(as_text=True)
    assert "初期開発段階" in response.get_data(as_text=True)
