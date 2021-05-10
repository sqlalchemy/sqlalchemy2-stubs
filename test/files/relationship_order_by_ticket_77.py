from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

mapper_registry: registry = registry()

e = create_engine("sqlite:///")


@mapper_registry.mapped
class A:
    __tablename__ = "a"
    id = Column(Integer, primary_key=True)
    b_id = Column(Integer, ForeignKey("b.id"))
    number = Column(Integer, primary_key=True)
    number2 = Column(Integer, primary_key=True)


@mapper_registry.mapped
class B:
    __tablename__ = "b"
    id = Column(Integer, primary_key=True)

    # Omit order_by
    a1: Mapped[A] = relationship("A", uselist=True)

    # All kinds of order_by
    a2: Mapped[A] = relationship("A", uselist=True, order_by=(A.id, A.number))
    a3: Mapped[A] = relationship("A", uselist=True, order_by=[A.id, A.number])
    a4: Mapped[A] = relationship("A", uselist=True, order_by=A.id)
    a5: Mapped[A] = relationship("A", uselist=True, order_by=A.__table__.c.id)
    a6: Mapped[A] = relationship("A", uselist=True, order_by="A.number")

    # Same kinds but lambda'd
    a7: Mapped[A] = relationship(
        "A", uselist=True, order_by=lambda: (A.id, A.number)
    )
    a8: Mapped[A] = relationship(
        "A", uselist=True, order_by=lambda: [A.id, A.number]
    )
    a9: Mapped[A] = relationship("A", uselist=True, order_by=lambda: A.id)


mapper_registry.metadata.drop_all(e)
mapper_registry.metadata.create_all(e)

with Session(e) as s:
    s.execute(select(B).options(joinedload(B.a1)))
    s.execute(select(B).options(joinedload(B.a2)))
    s.execute(select(B).options(joinedload(B.a3)))
    s.execute(select(B).options(joinedload(B.a4)))
    s.execute(select(B).options(joinedload(B.a5)))
    s.execute(select(B).options(joinedload(B.a7)))
    s.execute(select(B).options(joinedload(B.a8)))
    s.execute(select(B).options(joinedload(B.a9)))
