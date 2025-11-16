import pytest
from src.data_generators import generate_pet

pytestmark = pytest.mark.pet


def test_create_pet(petstore_client):

    # Проверка создание питомца (POST /pet).
    pet = generate_pet(status="available")

    response = petstore_client.add_pet(pet)
    assert response.status_code == 200

    body = response.json()
    assert body["id"] == pet["id"]
    assert body["name"] == pet["name"]
    assert body["status"] == pet["status"]


def test_get_existing_pet(petstore_client):

    # Проверяем получение существующего питомца (GET /pet/{petId}).
    # Подготовка данных через POST, основная проверка GET.

    pet = generate_pet(status="available")
    create_resp = petstore_client.add_pet(pet)
    assert create_resp.status_code == 200

    get_resp = petstore_client.get_pet(pet["id"])
    assert get_resp.status_code == 200

    body = get_resp.json()
    assert body["id"] == pet["id"]
    assert body["name"] == pet["name"]
    assert body["status"] == pet["status"]


def test_update_pet_status(petstore_client):

    # Проверяем обновление питомца (PUT /pet).

    pet = generate_pet(status="available")
    create_resp = petstore_client.add_pet(pet)
    assert create_resp.status_code == 200

    updated_pet = dict(pet)
    updated_pet["status"] = "sold"

    update_resp = petstore_client.update_pet(updated_pet)
    assert update_resp.status_code == 200

    get_resp = petstore_client.get_pet(pet["id"])
    assert get_resp.status_code == 200
    body = get_resp.json()
    assert body["status"] == "sold"


def test_delete_pet(petstore_client):

    # Проверка удаление питомца (DELETE /pet/{petId}).

    pet = generate_pet(status="available")
    create_resp = petstore_client.add_pet(pet)
    assert create_resp.status_code == 200

    delete_resp = petstore_client.delete_pet(pet["id"])
    assert delete_resp.status_code in (200, 404)

    get_resp = petstore_client.get_pet(pet["id"])
    assert get_resp.status_code == 404

@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_pets_by_status(petstore_client, status):
    resp = petstore_client.find_pets_by_status(status)
    assert resp.status_code == 200
    pets = resp.json()
    for pet in pets:
        assert pet["status"] == status
