from typing import Optional

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import registry
from sqlalchemy.orm import Session

mr: registry = registry()


@mr.mapped
class Foo:
    id = Column(Integer, primary_key=True)
    __tablename__ = "foo"


s = Session()
x: Optional[Foo] = s.get(Foo, 1)


async def go() -> None:
    as_ = AsyncSession()
    y: Optional[Foo] = await as_.get(Foo, 1)
