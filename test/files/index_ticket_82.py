from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Index
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Model(Base):

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)

    __tablename__ = "model"
    __table_args__ = (Index("created_at_idx", created_at.desc()),)
