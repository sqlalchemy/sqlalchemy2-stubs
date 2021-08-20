from sqlalchemy import Column, Integer, create_engine, func
from sqlalchemy.orm import Session, declarative_base, sessionmaker

Base = declarative_base()


class Foo(Base):
    __tablename__ = "foo"

    id = Column(Integer(), primary_key=True)
    a = Column(Integer())
    b = Column(Integer())


func.row_number().over(order_by=Foo.a, partition_by=Foo.b.desc())
func.row_number().over(order_by=[Foo.a.desc(), Foo.b.desc()])
func.row_number().over(partition_by=[Foo.a.desc(), Foo.b.desc()])
func.row_number().over(order_by="a", partition_by=("a", "b"))
func.row_number().over(partition_by="a", order_by=("a", "b"))
