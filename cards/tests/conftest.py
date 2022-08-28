import pytest
from cards.models import Card


@pytest.fixture
def card_fixture(db):
    return Card.objects.create(question="house", answer="dom", box=1)
