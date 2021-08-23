from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import FetchedValue
from sqlalchemy import Integer
from sqlalchemy import literal_column
from sqlalchemy import text
from sqlalchemy import true
from sqlalchemy.orm import registry
from sqlalchemy.sql import functions as func

reg: registry = registry()


@reg.mapped
class A:
    __tablename__ = "a"

    b = Column(Boolean, nullable=False, server_default=true())
    c = Column(DateTime, server_default=func.now(), nullable=False)

    # EXPECTED_MYPY: Cannot infer type argument 1 of "Column"
    d = Column(Boolean, server_default=func.now(), nullable=False)

    e = Column(DateTime, server_default="now()")
    f = Column(DateTime, server_default=text("now()"))
    g = Column(DateTime, server_default=FetchedValue())
    h = Column(Boolean, server_default=literal_column("false", Boolean))

    # overload 1: (__name: str, *args, ...)
    overload1: int = Column(
        "name", server_default=FetchedValue(), nullable=False
    )
    # overload 2: (*args, ...)
    Column(server_default="now()", nullable=False)
    # overload 3: (__name: str, __type: _TE, *args, ...)
    overload3 = Column(
        "name", Integer, server_default=text("now()"), nullable=False
    )
    # overload 4: (__type: _TE, *args, ...)
    overload4 = Column(
        Integer, server_default=literal_column("42", Integer), nullable=False
    )
