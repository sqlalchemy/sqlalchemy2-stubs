from typing import Any
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import Union

from . import attributes as attributes
from . import clsregistry as clsregistry
from . import instrumentation as instrumentation
from . import interfaces as interfaces
from .mapper import Mapper as Mapper
from .. import inspection as inspection
from .. import util as util
from ..sql import ColumnElement
from ..sql.schema import MetaData as MetaData
from ..util import hybridmethod as hybridmethod
from ..util import hybridproperty as hybridproperty

def has_inherited_table(cls): ...

class DeclarativeMeta(type):
    def __init__(
        cls, classname: Any, bases: Any, dict_: Any, **kw: Any
    ) -> None: ...
    def __setattr__(cls, key: Any, value: Any) -> None: ...
    def __delattr__(cls, key: Any) -> None: ...
    metadata: MetaData
    registry: "registry"

def synonym_for(name: Any, map_column: bool = ...): ...

_T = TypeVar("_T")
_Generic_T = Generic[_T]

class declared_attr(interfaces._MappedAttribute, property, Generic[_T]):
    __doc__: Any = ...
    def __init__(self, fget: Any, cascading: bool = ...) -> None: ...
    def __get__(
        desc: Any, self: Any, cls: Any
    ) -> Union[interfaces.MapperProperty, ColumnElement]: ...
    def cascading(cls): ...

class _stateful_declared_attr(declared_attr):
    kw: Any = ...
    def __init__(self, **kw: Any) -> None: ...
    def __call__(self, fn: Any): ...

def declarative_base(
    bind: Optional[Any] = ...,
    metadata: Optional[Any] = ...,
    mapper: Optional[Any] = ...,
    cls: Any = ...,
    name: str = ...,
    constructor: Any = ...,
    class_registry: Optional[Any] = ...,
    metaclass: Any = ...,
): ...

class registry:
    metadata: Any = ...
    constructor: Any = ...
    def __init__(
        self,
        metadata: Optional[Any] = ...,
        class_registry: Optional[Any] = ...,
        constructor: Any = ...,
        _bind: Optional[Any] = ...,
    ) -> None: ...
    @property
    def mappers(self): ...
    def configure(self, cascade: bool = ...) -> None: ...
    def dispose(self, cascade: bool = ...) -> None: ...
    def generate_base(
        self,
        mapper: Optional[Any] = ...,
        cls: Any = ...,
        name: str = ...,
        metaclass: Any = ...,
    ): ...
    def mapped(self, cls: Any): ...
    def as_declarative_base(self, **kw: Any): ...
    def map_declaratively(self, cls: type) -> Mapper: ...
    def map_imperatively(
        self, class_: Any, local_table: Optional[Any] = ..., **kw: Any
    ): ...

def as_declarative(**kw: Any): ...
