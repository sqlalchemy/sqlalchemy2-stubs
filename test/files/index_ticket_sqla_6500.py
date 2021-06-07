from sqlalchemy import Column
from sqlalchemy import Index
from sqlalchemy import Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base


Base = declarative_base()

test_table = Table(
    "test_table",
    Base.metadata,
    Column("i", UUID(as_uuid=True), nullable=False, primary_key=True),
    Column("x", UUID(as_uuid=True), index=True),
    Column("y", UUID(as_uuid=True), index=True),
    Index(
        "ix_xy_unique",
        "x",
        "y",
        unique=True,
    ),
)
