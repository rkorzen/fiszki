from cards.models import Card


# @pytest.mark.django_db
class TestsModelCard:
    def test_move_method(self, card_fixture):
        assert card_fixture.box == 1
        card_fixture.move(solved=True)
        assert card_fixture.box == 2

    def test_move_method_with_false_in_solved(self, db):
        c = Card.objects.create(question="house", answer="dom", box=4)
        assert c.box == 4
        c.move(solved=False)
        assert c.box == 1

    def test_str(self, card_fixture):
        assert str(card_fixture) == "house"
