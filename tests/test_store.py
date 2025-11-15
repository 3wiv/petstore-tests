import pytest
from src.data_generators import generate_order, generate_pet

pytestmark = pytest.mark.store

def test_place_get_delete_order(petstore_client):
    # Создание питомца для заказа
    pet = generate_pet()
    petstore_client.add_pet(pet)

    order = generate_order()
    order["petId"] = pet["id"]

    place_resp = petstore_client.place_order(order)
    assert place_resp.status_code == 200
    placed = place_resp.json()
    assert placed["id"] == order["id"]
    assert placed["petId"] == order["petId"]

    get_resp = petstore_client.get_order(order["id"])
    assert get_resp.status_code == 200
    got_order = get_resp.json()
    assert got_order["id"] == order["id"]

    delete_resp = petstore_client.delete_order(order["id"])
    assert delete_resp.status_code in (200, 404)

    get_deleted_resp = petstore_client.get_order(order["id"])
    assert get_deleted_resp.status_code == 404
