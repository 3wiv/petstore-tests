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
