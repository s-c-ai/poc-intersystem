import pytest
from fastapi.testclient import TestClient
from poc_intersystem.app import app


@pytest.fixture
def client():
    return TestClient(app)



