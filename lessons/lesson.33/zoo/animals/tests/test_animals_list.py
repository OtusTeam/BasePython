from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse_lazy

from animals.models import Animal


class AnimalsListTestCase(TestCase):
    fixtures = [
        "animal_foods.fixture.json",
        "animal_kinds.fixture.json",
        "animals.fixture.json",
    ]

    url = reverse_lazy("animals:index")

    def test_list_animals(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        animals = (
            Animal
            .objects
            .select_related("kind")
            .prefetch_related("food")
            .filter(archived=False)
            .order_by("pk")
            .all()
        )
        animals_in_context = response.context["animals"]
        self.assertEqual(len(animals), len(animals_in_context))
        for a1, a2 in zip(animals, animals_in_context):
            self.assertEqual(a1.pk, a2.pk)

    def test_anon_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context["user"].is_anonymous)
