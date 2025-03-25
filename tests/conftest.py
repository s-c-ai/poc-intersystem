import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from poc_intersystem.app import app
from poc_intersystem.database import engine
from poc_intersystem.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    # WARN: It's using production database.
    # Must change to temporary table, like memory sqlite.
    table_registry.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
