from fastapi.testclient import TestClient
from main import app

'''
Unit tests for the university student data API.
'''

client = TestClient(app)


def test_students_get():
    response = client.get("/students")
    assert response.status_code == 200

def test_student_by_id_get():
    response = client.get("/students/s1")
    assert response.status_code == 200
    assert response.json()["student_id"] == "S12345"

def test_student_not_found():
    response = client.get("/students/s999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"

def test_home_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["name"] == "University API"
    assert response.json()["version"] == "1.0.0"