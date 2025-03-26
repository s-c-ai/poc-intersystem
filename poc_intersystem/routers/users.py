from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from poc_intersystem import models, schemas
from poc_intersystem.helpers import deps

router = APIRouter(prefix='/users', tags=['users'])


@router.post(
    '/', status_code=HTTPStatus.CREATED, response_model=schemas.UserPublic
)
def create_user(user: schemas.UserInput, session: deps.DBSession):
    db_user = session.scalar(
        select(models.User).where(
            (models.User.username == user.username)
            | (models.User.email == user.email)
        )
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='Username already exists',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT, detail='Email already exists'
            )
    new_user = models.User(**user.model_dump())

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user
