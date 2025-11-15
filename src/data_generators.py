import random
import string
from typing import Dict

def random_string(prefix: str = "", length: int = 8) -> str:
    letters = string.ascii_lowercase
    return prefix + "".join(random.choice(letters) for _ in range(length))

def generate_pet(status: str = "available") -> Dict:
    return {
        "id": random.randint(1, 10**9),
        "name": random_string("pet_"),
        "status": status
    }

def generate_order() -> Dict:
    return {
        "id": random.randint(1, 10**9),
        "petId": random.randint(1, 10**9),
        "quantity": 1,
        "shipDate": "2025-01-01T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }

def generate_user() -> Dict:
    username = random_string("user_")
    return {
        "id": random.randint(1, 10**9),
        "username": username,
        "firstName": "Test",
        "lastName": "User",
        "email": f"{username}@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1
    }
