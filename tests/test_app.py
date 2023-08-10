# tests.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response =  self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        #TODO add more tests relating to the home page

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # Testing post request
        response = self.client.post("/api/timeline_post", data={"name":"John Doe", "email":"john@example.com", "content":"Hello world, I'm John!"})
        assert response.status_code == 200
        
        # Checking for new post in timeline
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        post = json["timeline_posts"][0]
        assert post["name"] == "John Doe"
        assert post["email"] == "john@example.com"
        assert post["content"] == "Hello world, I'm John!"

        # Testing page structure
        response = self.client.get("/timeline")
        html = response.get_data(as_text=True)
        assert "<title>Timeline</title>" in html
        assert '<form action="/read-form" method="post">' in html
        assert "<h2>Existing timeline posts</h2>" in html

    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={"email":"john@example.com", "content":"Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html
        
        response = self.client.post("/api/timeline_post", data={"name":"John Doe", "email": "john@example.com", "content":""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        response = self.client.post("/api/timeline_post", data={"name":"John Doe", "email":"not-an-email", "content":"Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
