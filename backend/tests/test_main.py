import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestCreateUser(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_user_success(self):
        print("test_create_user_success")
        response = self.client.post(
            "/users/",
            json={
                "username": "newuser",
                "password": "newpassword",
                "email": "newuser@example.com"
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["username"], "newuser")
        self.assertEqual(response.json()["email"], "newuser@example.com")

    def test_create_user_duplicate_username(self):
        print("test_create_user_duplicate_username")
        response = self.client.post(
            "/users/",
            json={
                "username": "testuser",
                "password": "testpassword",
                "email": "testuser@example.com"
            }
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "Username already registered")

if __name__ == "__main__":
    unittest.main()