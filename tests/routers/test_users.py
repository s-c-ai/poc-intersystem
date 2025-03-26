from http import HTTPStatus


def test_create_user(client, faker):
    username = faker.user_name()
    email = faker.email()

    response = client.post(
        '/users/',
        json={
            'username': username,
            'email': email,
            'password': faker.password(),
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {'id': 1, 'username': username, 'email': email}


def test_create_existant_username_must_raises(client, faker, user):
    response = client.post(
        '/users/',
        json={
            'username': user.username,
            'email': faker.email(),
            'password': faker.password(),
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Username already exists'}


def test_create_existant_email_must_raises(client, faker, user):
    response = client.post(
        '/users/',
        json={
            'username': faker.user_name(),
            'email': user.email,
            'password': faker.password(),
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Email already exists'}
