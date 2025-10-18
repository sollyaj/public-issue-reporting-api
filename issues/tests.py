from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Issue

User = get_user_model()

class IssueTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.url = reverse('issue-list-create')

    def test_create_issue(self):
        data = {
            "title": "Pothole on Main Street",
            "description": "Large pothole near the market",
            "category": "road",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_issues(self):
        Issue.objects.create(
            title="Broken streetlight",
            description="Light not working for 2 weeks",
            category="electricity",
            reported_by=self.user
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

