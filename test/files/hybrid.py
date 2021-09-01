from typing import Optional

import sqlalchemy as sa
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import registry

R: registry = registry()


@R.mapped
class SomeModel:
    __tablename__ = "some_model"
    a = sa.Column(sa.Float, primary_key=True)
    b = sa.Column(sa.Integer, primary_key=True)

    @hybrid_property
    def hp(self) -> float:
        return abs(self.a) / 2 if self.a else 0

    @hp.setter  # type:ignore[no-redef]
    def hp(self, value: float) -> None:
        self.a = value * 2

    @hp.deleter  # type:ignore[no-redef]
    def hp(self):
        self.a = None

    @hp.expression  # type:ignore[no-redef]
    def hp(cls) -> sa.sql.ColumnElement[sa.Float]:
        return sa.func.abs(cls.a) / 2

    def oget(self) -> float:
        return self.b + 42 if self.b else -1

    def oexp(cls) -> sa.sql.ColumnElement[sa.Integer]:
        return cls.a + 42

    other = hybrid_property(oget, expr=oexp)


obj = SomeModel()
hp: Optional[float] = obj.hp
other: Optional[int] = obj.other
hp_asc: sa.sql.ColumnElement[sa.Float] = SomeModel.hp.asc()
other_desc: sa.sql.ColumnElement[sa.Integer] = SomeModel.other.desc()
