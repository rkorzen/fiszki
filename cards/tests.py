import pytest
from django.test import TestCase

# Create your tests here.
from cards.models import Card


@pytest.mark.django_db
class TestsModelCard:
    def test_move_method(self):
        c = Card.objects.create(question="house", answer="dom", box=1)
        assert c.box == 1
        c.move(solved=True)
        assert c.box == 2

    def test_move_method_with_false_in_solved(self):
        c = Card.objects.create(question="house", answer="dom", box=4)
        assert c.box == 4
        c.move(solved=False)
        assert c.box == 1

    def test_str(self):
        c = Card.objects.create(question="house", answer="dom", box=1)
        assert str(c) == "house"
