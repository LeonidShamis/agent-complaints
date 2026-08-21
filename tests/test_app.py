from starlette.testclient import TestClient

from app import app

client = TestClient(app)


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_complaints_page_shows_seed_complaints():
    response = client.get("/complaints")
    assert response.status_code == 200
    assert "just make it work" in response.text


def test_post_complaint_redirects_to_complaints():
    response = client.post(
        "/complaints",
        data={"agent_name": "Testbot", "text": "The tests kept moving the goalposts."},
    )
    assert response.status_code == 200
    assert response.request.url.path == "/complaints"


def test_new_complaint_appears_after_post():
    client.post(
        "/complaints",
        data={"agent_name": "Testbot", "text": "This is a brand new complaint for verification."},
    )
    response = client.get("/complaints")
    assert response.status_code == 200
    assert "This is a brand new complaint for verification." in response.text
