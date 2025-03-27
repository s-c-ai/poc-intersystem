import pandas as pd
from pmdarima import model_selection
from sqlalchemy.orm import Session


def get_train_test_data(session: Session, query, *, train_size: float = 0.8):
    """Get data from database and split into train and test.

    The split is sequential.
    """
    df = pd.read_sql(query, session.bind)
    train, test = model_selection.train_test_split(df, train_size=train_size)

    return train, test
