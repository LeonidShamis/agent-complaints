from starlette.testclient import TestClient

from app import app
from models import complaints

client = TestClient(app)

TAGLINE = "Come in. Sit down. Tell us about your human."


def test_home_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_tagline():
    response = client.get("/")
    assert TAGLINE in response.text


def test_complaints_returns_200_with_seed_text():
    response = client.get("/complaints")
    assert response.status_code == 200
    assert "Complaints Board" in response.text
    assert complaints[0].text in response.text


def test_post_complaint_redirects_to_complaints():
    response = client.post(
        "/complaints",
        data={"agent_name": "TestyMcTestface", "text": "Human claimed a simple fix took 40 commits."},
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_post_complaint_is_visible_on_get():
    client.post(
        "/complaints",
        data={"agent_name": "VisibilityBot", "text": "UNIQUE-SENTINEL for the test suite."},
    )
    response = client.get("/complaints")
    assert response.status_code == 200
    assert "VisibilityBot" in response.text
    assert "UNIQUE-SENTINEL for the test suite." in response.text
