from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

engine = create_engine("")
SM = sessionmaker(engine)

session = Session(engine)

s_session = scoped_session(SM)


def go() -> None:
    r = session.scalars(text("select 1"))
    r.first()
    r = s_session.scalars(text("select 1"))
    r.first()

    with engine.connect() as conn:
        cr = conn.scalars(text("select 1"))
        cr.first()
