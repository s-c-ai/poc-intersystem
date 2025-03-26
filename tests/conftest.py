import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from poc_intersystem.app import app
from poc_intersystem.database import engine, get_session
from poc_intersystem.models import table_registry

from .factories import UserFactory


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override

        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    # WARN: It's using production database.
    # Must change to temporary table, like memory sqlite.
    table_registry.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


@pytest.fixture
def user(session):
    user = UserFactory()

    session.add(user)
    session.commit()
    session.refresh(user)

    return user
