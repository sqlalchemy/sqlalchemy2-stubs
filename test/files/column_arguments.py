from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Sequence
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import registry

reg: registry = registry()


@reg.mapped
class InferredNames:
    __tablename__ = "infered"

    # Instantiated type
    id = Column(Integer(), primary_key=True)

    # Non-instantiated type
    name = Column(String, nullable=False)

    # SchemaItem
    foreign: Mapped[int] = Column(ForeignKey("infered.id"))

    # SchemaItem without type
    foreign1: Mapped[int] = Column(ForeignKey("infered.id"))

    # SchemaItem without type
    foreign2: Mapped[int] = Column(Integer, ForeignKey("infered.id"))

    # sequence
    seq = Column(Integer, Sequence("my_sequence"), primary_key=True)


@reg.mapped
class ExplicitNames:
    __tablename__ = "explicit"

    # Instantiated type
    id = Column("id", Integer(), primary_key=True)

    # Non-instantiated type
    name = Column("name", String, nullable=False)

    # SchemaItem without type
    foreign1: int = Column("foreign", ForeignKey("infered.id"))

    # SchemaItem without type
    foreign2: int = Column("foreign", Integer, ForeignKey("infered.id"))

    # sequence
    seq = Column(Integer, Sequence("my_sequence"), primary_key=True)
