from django.test import TestCase
from django.urls import reverse

from animals.models import Animal


class AnimalsTestCase(TestCase):
    fixtures = [
        "animal_foods.fixture.json",
        "animal_kinds.fixture.json",
        "animals.fixture.json",
    ]

    def test_list_animals(self):
        response = self.client.get(
            reverse("animals:list"),
        )

        self.assertEqual(response.status_code, 200)

        animals_list = Animal.objects.order_by("id").all()
        animals_in_context = response.context["animals"]
        self.assertEqual(len(animals_list), len(animals_in_context))
        for a1, a2 in zip(animals_list, animals_in_context):
            self.assertEqual(a1.pk, a2.pk)

    def test_animals_list_anon_access(self):
        response = self.client.get(
            reverse("animals:list"),
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["user"].is_anonymous)
