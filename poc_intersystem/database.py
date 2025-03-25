from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from poc_intersystem.helpers.settings import settings

engine = create_engine(settings.DATABASE_URL)


def get_session():  # pragma: nocover
    with Session(engine) as session:
        yield session
