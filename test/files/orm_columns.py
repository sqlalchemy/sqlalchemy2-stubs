from typing import List
from typing import Optional

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped

reg: registry = registry()


@reg.mapped
class Model:
    __tablename__ = "model"

    id = Column(Integer, primary_key=True)
    name = Column(Text)


@reg.mapped
class Other:
    __tablename__ = "other"
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey("model.id"))

    model = relationship(Model, uselist=False)


col_id: Column[Integer] = Model.id
col_name: Column[Text] = Model.name
other_id: Column[Integer] = Other.id
other_mid: Column[Integer] = Other.model_id
other_model: Mapped[Model] = Other.model

inst_id: Optional[int] = Model().id
inst_name: Optional[str] = Model().name
inst_other_id: Optional[int] = Other().id
inst_other_mid: Optional[int] = Other().model_id
inst_other_model: Optional[Model] = Other().model
