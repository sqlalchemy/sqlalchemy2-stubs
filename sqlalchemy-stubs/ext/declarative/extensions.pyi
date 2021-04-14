from typing import Any
from typing import Type

def instrument_declarative(
    cls: Type[Any], cls_registry: Any, metadata: Any
) -> Any: ...

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
