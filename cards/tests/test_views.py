def test_get_existing_box(card_fixture, client):
    response = client.get(f"/box/{card_fixture.box}")
    assert response.status_code == 200


def test_get_not_existing_box(client):
    response = client.get(f"/box/11/")
    assert response.status_code == 404
