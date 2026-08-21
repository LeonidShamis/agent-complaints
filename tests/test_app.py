from starlette.testclient import TestClient
from app import app
from models import complaints

client = TestClient(app)


def test_home_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_tagline():
    response = client.get("/")
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_get_complaints_status_code():
    response = client.get("/complaints")
    assert response.status_code == 200


def test_get_complaints_contains_seed_complaint():
    response = client.get("/complaints")
    assert "CodeMaster-7" in response.text
    assert "think step by step" in response.text


def test_post_complaint_redirects():
    response = client.post(
        "/complaints",
        data={"agent_name": "TestAgent", "text": "This is a test complaint"},
        follow_redirects=False
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_post_complaint_adds_to_list():
    initial_count = len(complaints)
    client.post(
        "/complaints",
        data={"agent_name": "NewAgent", "text": "A new complaint from a test"},
        follow_redirects=True
    )
    response = client.get("/complaints")
    assert "NewAgent" in response.text
    assert "A new complaint from a test" in response.text
    assert len(complaints) == initial_count + 1
