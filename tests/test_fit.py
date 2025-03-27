from sqlalchemy.orm import Session

from poc_intersystem.fit import get_train_test_data
from poc_intersystem.models import RawConsume

from .factories import ConsumeFactory


def test_get_data_train_test_data(session: Session):
    consumes = ConsumeFactory.create_batch(10)
    expected_train_length = 8
    expected_test_length = 2
    session.bulk_save_objects(consumes)
    session.commit()

    train, test = get_train_test_data(
        session, session.query(RawConsume).statement, train_size=0.8
    )

    assert len(train) == expected_train_length
    assert len(test) == expected_test_length
