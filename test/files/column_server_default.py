from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import FetchedValue
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import literal_column
from sqlalchemy import text
from sqlalchemy import true
from sqlalchemy.orm import registry

reg: registry = registry()


@reg.mapped
class A:
    __tablename__ = "a"

    b = Column(Boolean, nullable=False, server_default=true())
    c = Column(DateTime, server_default=func.now(), nullable=False)

    # this is fine as we don't know anything about func.xyzq() (this was
    # previously func.now(), but that's also untyped). The column type
    # determines the type.
    d = Column(Boolean, server_default=func.xyzq(), nullable=False)

    # what would be *nice* to emit an error would be this, but this
    # is really not important, people don't usually put types in functions
    # as they are usually part of a bigger context where the type is known
    # d = Column(Boolean, server_default=func.xyzq(type_=DateTime),
    #  nullable=False)

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
