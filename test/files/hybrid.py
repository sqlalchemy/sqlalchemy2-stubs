import sqlalchemy as sa
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import registry

R: registry = registry()


@R.mapped
class SomeModel:
    __tablename__ = "some_model"
    a = sa.Column(sa.Float, primary_key=True)

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
    def hp(cls) -> sa.sql.ClauseElement:
        return sa.func.abs(cls.a) / 2


obj = SomeModel()
obj.hp
