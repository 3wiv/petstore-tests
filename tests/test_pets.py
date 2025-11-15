import pytest
from src.data_generators import generate_pet

pytestmark = pytest.mark.pet

def test_create_get_update_delete_pet(petstore_client):
    # CREATE
    pet = generate_pet(status="available")
    create_resp = petstore_client.add_pet(pet)
    assert create_resp.status_code == 200
    created = create_resp.json()
    assert created["id"] == pet["id"]
    assert created["name"] == pet["name"]

    # GET
    get_resp = petstore_client.get_pet(pet["id"])
    assert get_resp.status_code == 200
    fetched = get_resp.json()
    assert fetched["id"] == pet["id"]
    assert fetched["name"] == pet["name"]
    assert fetched["status"] == "available"

    # UPDATE
    pet_updated = dict(pet)
    pet_updated["status"] = "sold"
    update_resp = petstore_client.update_pet(pet_updated)
    assert update_resp.status_code == 200

    get_updated_resp = petstore_client.get_pet(pet["id"])
    assert get_updated_resp.status_code == 200
    assert get_updated_resp.json()["status"] == "sold"

    # DELETE
    delete_resp = petstore_client.delete_pet(pet["id"])
    assert delete_resp.status_code in (200, 404)  # Из-за нестабильности petstore.swagger.io используются два значения в ожидании ответа.

    # Проверка, существования pet
    get_deleted_resp = petstore_client.get_pet(pet["id"])
    assert get_deleted_resp.status_code == 404

@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_pets_by_status(petstore_client, status):
    resp = petstore_client.find_pets_by_status(status)
    assert resp.status_code == 200
    pets = resp.json()
    # Ответ может быть пустым, но если есть элементы статус должен совпадать
    for pet in pets:
        assert pet["status"] == status
