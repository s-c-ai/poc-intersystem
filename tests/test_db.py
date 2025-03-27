from sqlalchemy import select

from poc_intersystem.models import RawConsume, User

from .factories import ConsumeFactory


def test_create_user(session, faker):
    username = faker.user_name()
    new_user = User(
        username=username,
        password=faker.password(),
        email=faker.email(),
    )

    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == username))

    assert user.username == username


def test_create_raw_consume(session):
    consume = ConsumeFactory()
    session.add(consume)
    session.commit()

    consume_db = session.scalar(
        select(RawConsume).where(RawConsume.regiao == consume.regiao)
    )

    assert consume_db.regiao == consume.regiao
