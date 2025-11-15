import requests

class PetStoreClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    # pets
    def add_pet(self, pet: dict):
        return requests.post(self._url("/pet"), json=pet)

    def get_pet(self, pet_id: int):
        return requests.get(self._url(f"/pet/{pet_id}"))

    def update_pet(self, pet: dict):
        return requests.put(self._url("/pet"), json=pet)

    def delete_pet(self, pet_id: int):
        return requests.delete(self._url(f"/pet/{pet_id}"))

    def find_pets_by_status(self, status: str):
        return requests.get(self._url("/pet/findByStatus"), params={"status": status})

    # store
    def place_order(self, order: dict):
        return requests.post(self._url("/store/order"), json=order)

    def get_order(self, order_id: int):
        return requests.get(self._url(f"/store/order/{order_id}"))

    def delete_order(self, order_id: int):
        return requests.delete(self._url(f"/store/order/{order_id}"))

    # users
    def create_user(self, user: dict):
        return requests.post(self._url("/user"), json=user)

    def get_user(self, username: str):
        return requests.get(self._url(f"/user/{username}"))

    def update_user(self, username: str, user: dict):
        return requests.put(self._url(f"/user/{username}"), json=user)

    def delete_user(self, username: str):
        return requests.delete(self._url(f"/user/{username}"))
