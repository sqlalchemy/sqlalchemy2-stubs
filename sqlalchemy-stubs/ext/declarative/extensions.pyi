from typing import Any

from ... import inspection as inspection
from ... import util as util
from ...orm import registry as registry
from ...orm import relationships as relationships
from ...orm.util import polymorphic_union as polymorphic_union
from ...schema import Table as Table
from ...util import OrderedDict as OrderedDict

def instrument_declarative(cls, cls_registry: Any, metadata: Any): ...

class ConcreteBase:
    @classmethod
    def __declare_first__(cls) -> None: ...

class AbstractConcreteBase(ConcreteBase):
    __no_table__: bool = ...
    @classmethod
    def __declare_first__(cls) -> None: ...

class DeferredReflection:
    @classmethod
    def prepare(cls, engine: Any) -> None: ...
