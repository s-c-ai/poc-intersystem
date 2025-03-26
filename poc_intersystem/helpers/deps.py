from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from poc_intersystem.database import get_session

DBSession = Annotated[Session, Depends(get_session)]
