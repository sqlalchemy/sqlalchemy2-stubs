from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
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
