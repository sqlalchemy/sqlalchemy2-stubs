from typing import Any

from . import events as events
from .elements import conv as conv
from .schema import CheckConstraint as CheckConstraint
from .schema import Column as Column
from .schema import Constraint as Constraint
from .schema import ForeignKeyConstraint as ForeignKeyConstraint
from .schema import Index as Index
from .schema import PrimaryKeyConstraint as PrimaryKeyConstraint
from .schema import Table as Table
from .schema import UniqueConstraint as UniqueConstraint
from .. import event as event
from .. import exc as exc

class ConventionDict:
    const: Any = ...
    table: Any = ...
    convention: Any = ...
    def __init__(self, const: Any, table: Any, convention: Any) -> None: ...
    def __getitem__(self, key: Any): ...
