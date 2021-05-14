from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.orm import registry
from sqlalchemy.sql import ColumnElement

mapper_registry: registry = registry()


@mapper_registry.mapped
class A:
    __tablename__ = "a"
    id = Column(Integer, primary_key=True)


neg: "ColumnElement[Boolean]" = -A.id

desc = A.id.desc()
asc = A.id.asc()
any_ = A.id.any_()
all_ = A.id.all_()
nulls_first = A.id.nulls_first()
nulls_last = A.id.nulls_last()
collate = A.id.collate("somelang")
distinct = A.id.distinct()
