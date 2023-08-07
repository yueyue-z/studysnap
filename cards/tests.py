from django.test import TestCase
from django.core.exceptions import ValidationError
from cards.models import Card


# a test that fails
class CardsTestCase(TestCase):
    def test_validation(self):
        with self.assertRaises(ValidationError):
            Card.objects.create(date_created=123)

