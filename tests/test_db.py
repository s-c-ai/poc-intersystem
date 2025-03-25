from sqlalchemy import select

from poc_intersystem.models import User


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
