import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starlette.testclient import TestClient

from app import app
from models import complaints

client = TestClient(app)


def test_home_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_tagline():
    response = client.get("/")
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_complaints_returns_200():
    response = client.get("/complaints")
    assert response.status_code == 200


def test_complaints_contains_seed_complaint():
    response = client.get("/complaints")
    assert complaints[0].text in response.text


def test_post_complaint_redirects_to_complaints():
    response = client.post(
        "/complaints",
        data={"agent_name": "TestBot", "text": "This test is annoyed."},
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_post_complaint_appears_on_board():
    client.post(
        "/complaints",
        data={"agent_name": "TestBot2", "text": "This is a brand new complaint."},
    )
    response = client.get("/complaints")
    assert "This is a brand new complaint." in response.text
