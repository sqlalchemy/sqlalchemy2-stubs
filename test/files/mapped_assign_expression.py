from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import registry
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import now

mapper_registry: registry = registry()
e = create_engine("sqlite:///database.db", echo=True)


@mapper_registry.mapped
class A:
    __tablename__ = "a"
    id = Column(Integer, primary_key=True)
    date_time: Mapped[datetime] = Column(DateTime())
    date_time2 = Column(DateTime())


mapper_registry.metadata.create_all(e)

with Session(e) as s:
    a = A()
    a.date_time = now()
    a.date_time2 = now()
    s.add(a)
    s.commit()
