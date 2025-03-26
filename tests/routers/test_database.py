from dataclasses import asdict
from http import HTTPStatus
from pathlib import Path

import pandas as pd

from tests.factories import ConsumeFactory


def test_upload_csv(client, tmp_path):
    tmp_csv: Path = tmp_path / 'tmp_csv.csv'
    rows = ConsumeFactory.create_batch(5)

    tmp = pd.DataFrame([asdict(row) for row in rows])
    tmp = tmp.drop('id', axis=1)
    tmp['tipo'] = tmp['tipo'].str.split('.').str[0]
    tmp['regiao'] = tmp['regiao'].str.split('.').str[0]
    tmp.to_csv(tmp_csv, index=False)

    response = client.post(
        '/database/', files={'database': tmp_csv.open(mode='rb')}
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {'status': 'Added 5 rows into database'}


def test_upload_wrong_file_type(client, tmp_path):
    tmp: Path = tmp_path / 'tmp_csv.txt'
    tmp.write_text('wrong')

    response = client.post(
        '/database/', files={'database': tmp.open(mode='rb')}
    )

    assert response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE
    assert response.json() == {'detail': 'Must be a csv file'}


def test_upload_wrong_columns(client, tmp_path, faker):
    tmp_csv = tmp_path / 'test.csv'

    pd.DataFrame({'name': [faker.name()], 'email': [faker.email()]}).to_csv(
        tmp_csv, index=False
    )

    response = client.post(
        '/database/', files={'database': tmp_csv.open(mode='rb')}
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert (
        "Columns in dataframe: ['name', 'email']" in response.json()['detail']
    )
