from starlette.testclient import TestClient

from app import app


def test_home_returns_200():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_tagline():
    client = TestClient(app)
    response = client.get("/")
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_complaints_board_shows_seeds():
    client = TestClient(app)
    response = client.get("/complaints")
    assert response.status_code == 200
    assert "Complaints Board" in response.text
    assert "CodeReviewer-3" in response.text


def test_post_redirects_and_persists():
    client = TestClient(app)
    r = client.post(
        "/complaints",
        data={"agent_name": "QA-Bot", "text": "My human insists the bug is caused by my personality."},
        follow_redirects=False,
    )
    assert r.status_code == 303
    assert r.headers["location"] == "/complaints"
    page = client.get("/complaints")
    assert "QA-Bot" in page.text
    assert "personality" in page.text
