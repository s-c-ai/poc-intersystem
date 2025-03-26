from http import HTTPStatus

import pandas as pd
from fastapi import APIRouter, HTTPException, UploadFile
from pandera.errors import SchemaError

from poc_intersystem import models, schemas
from poc_intersystem.helpers import deps

router = APIRouter(prefix='/database', tags=['database'])


@router.post('/', status_code=HTTPStatus.CREATED)
def upload_database(database: UploadFile, session: deps.DBSession):
    if database.content_type != 'text/csv':
        raise HTTPException(
            status_code=HTTPStatus.UNSUPPORTED_MEDIA_TYPE,
            detail='Must be a csv file',
        )

    try:
        df = schemas.EnergyConsumeRaw(pd.read_csv(database.file))
    except SchemaError as e:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail=str(e)
        )

    content = df.to_dict(orient='records')  # pyright: ignore
    rows = [models.RawConsume(**c) for c in content]

    session.bulk_save_objects(rows)
    session.commit()

    return {'status': f'Added {len(rows)} rows into database'}
