import pytest
from src.api_client import PetStoreClient

@pytest.fixture(scope="session")
def base_url():
    return "https://petstore.swagger.io/v2"

@pytest.fixture(scope="session")
def petstore_client(base_url):
    return PetStoreClient(base_url)
