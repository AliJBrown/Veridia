from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import PC


class PCTests(TestCase):
    def setUp(self):
        self.pc_data = {
            "name": "Test PC",
            "race": "human",
            "age": 25,
            "height": 5.8,
            "description": "A test character",
            "occupation": "Adventurer",
            "pc_class": "fighter",
            "strength": 14,
            "dexterity": 12,
            "constitution": 16,
            "wisdom": 10,
            "intelligence": 8,
            "charisma": 13,
            "actions": "Attack, Defend",
            "location": "Kingdom of Testland",
            "notes": "Test notes",
        }

        self.client = APIClient()
        self.pc = PC.objects.create(**self.pc_data)

    def test_pc_model(self):
        self.assertEqual(self.pc.name, "Test PC")
        self.assertEqual(self.pc.race, "human")
        # Add more assertions for other fields

    def test_get_pc_list(self):
        response = self.client.get(reverse("pc-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_pc_detail(self):
        response = self.client.get(reverse("pc-detail", args=[self.pc.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test PC")

    # Add more test methods for POST, PUT, DELETE, etc.
