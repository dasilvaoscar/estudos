from fastapi.testclient import TestClient
from asgi import app


def test_index():
  client = TestClient(app)
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hello World"}
  
def test_create_user():
  client = TestClient(app)
  response = client.post("/users", json={'username': 'test', 'password': 'test'})
  assert response.status_code == 200

def test_create_user_fail():
  client = TestClient(app)
  response = client.post("/users", json={'password': 'test'})
  assert response.status_code == 422