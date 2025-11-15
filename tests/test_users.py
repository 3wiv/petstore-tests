import pytest
from src.data_generators import generate_user

pytestmark = pytest.mark.user

def test_create_get_update_delete_user(petstore_client):
    user = generate_user()

    # CREATE
    create_resp = petstore_client.create_user(user)
    assert create_resp.status_code in (200, 201)

    # GET
    get_resp = petstore_client.get_user(user["username"])
    assert get_resp.status_code == 200
    fetched = get_resp.json()
    assert fetched["username"] == user["username"]

    # UPDATE
    updated_user = dict(user)
    updated_user["firstName"] = "Updated"
    update_resp = petstore_client.update_user(user["username"], updated_user)
    assert update_resp.status_code == 200

    get_updated_resp = petstore_client.get_user(user["username"])
    assert get_updated_resp.status_code == 200
    assert get_updated_resp.json()["firstName"] == "Updated"

    # DELETE
    delete_resp = petstore_client.delete_user(user["username"])
    assert delete_resp.status_code in (200, 404)

    get_deleted_resp = petstore_client.get_user(user["username"])
    assert get_deleted_resp.status_code == 404
