from typing import Any
from typing import Optional
from typing import Type
from typing import TypeVar

from .interfaces import LoaderOption
from ..sql.base import Generative

_L = TypeVar("_L", bound=Load)
_LO = TypeVar("_LO", bound=loader_option)

class Load(Generative, LoaderOption):
    path: Any = ...
    context: Any = ...
    local_opts: Any = ...
    is_class_strategy: bool = ...
    def __init__(self, entity: Any) -> None: ...
    @classmethod
    def for_existing_path(cls: Type[_L], path: Any) -> _L: ...
    is_opts_only: bool = ...
    strategy: Any = ...
    propagate_to_loaders: bool = ...
    def process_compile_state(self, compile_state: Any) -> None: ...
    def options(self: _L, *opts: Any) -> _L: ...
    def set_relationship_strategy(
        self: _L, attr: Any, strategy: Any, propagate_to_loaders: bool = ...
    ) -> _L: ...
    def set_column_strategy(
        self: _L,
        attrs: Any,
        strategy: Any,
        opts: Optional[Any] = ...,
        opts_only: bool = ...,
    ) -> _L: ...
    def set_generic_strategy(self: _L, attrs: Any, strategy: Any) -> _L: ...
    def set_class_strategy(self: _L, strategy: Any, opts: Any) -> _L: ...
    def contains_eager(
        loadopt: _L, attr: Any, alias: Optional[Any] = ...
    ) -> _L: ...
    def load_only(loadopt: _L, *attrs: Any) -> _L: ...
    def joinedload(
        loadopt: _L, attr: Any, innerjoin: Optional[bool] = ...
    ) -> _L: ...
    def subqueryload(loadopt: _L, attr: Any) -> _L: ...
    def selectinload(loadopt: _L, attr: Any) -> _L: ...
    def lazyload(loadopt: _L, attr: Any) -> _L: ...
    def immediateload(loadopt: _L, attr: Any) -> _L: ...
    def noload(loadopt: _L, attr: Any) -> _L: ...
    def raiseload(loadopt: _L, attr: Any, sql_only: bool = ...) -> _L: ...
    def defaultload(loadopt: _L, attr: Any) -> _L: ...
    def defer(loadopt: _L, key: str, raiseload: bool = ...) -> _L: ...
    def undefer(loadopt: _L, key: str) -> _L: ...
    def undefer_group(loadopt: _L, name: str) -> _L: ...
    def with_expression(loadopt: _L, key: Any, expression: Any) -> _L: ...
    def selectin_polymorphic(loadopt: _L, classes: Any) -> _L: ...

class _UnboundLoad(Load):
    path: Any = ...
    local_opts: Any = ...
    def __init__(self) -> None: ...

class loader_option:
    def __init__(self) -> None: ...
    name: Any = ...
    def __call__(self: _LO, fn: Any) -> _LO: ...

class _containseager_loader_option(loader_option):
    def fn(self, loadopt: _L, attr: Any, alias: Optional[Any] = ...) -> _L: ...
    def _unbound_fn(
        self, attr: Any, alias: Optional[Any] = ...
    ) -> _UnboundLoad: ...

class _load_only_loader_option(loader_option):
    def fn(self, loadopt: _L, *attrs: Any) -> _L: ...
    def _unbound_fn(self, *attrs: Any) -> _UnboundLoad: ...

class _joinedload_loader_option(loader_option):
    def fn(
        self, loadopt: _L, attr: Any, innerjoin: Optional[bool] = ...
    ) -> _L: ...
    def _unbound_fn(
        self, attr: Any, innerjoin: Optional[bool] = ...
    ) -> _UnboundLoad: ...

class _subqueryload_loader_option(loader_option):
    def fn(self, loadopt: _L, attr: Any) -> _L: ...
    def _unbound_fn(self, attr: Any) -> _UnboundLoad: ...

class _selectinload_loader_option(loader_option):
    def fn(self, loadopt: _L, attr: Any) -> _L: ...
    def _unbound_fn(self, attr: Any) -> _UnboundLoad: ...

class _lazyload_loader_option(loader_option):
    def fn(self, loadopt: _L, attr: Any) -> _L: ...
    def _unbound_fn(self, attr: Any) -> _UnboundLoad: ...

class _immediateload_loader_option(loader_option):
    def fn(self, loadopt: _L, attr: Any) -> _L: ...
    def _unbound_fn(self, attr: Any) -> _UnboundLoad: ...

class _noload_loader_option(loader_option):
    def fn(self, loadopt: _L, attr: Any) -> _L: ...
    def _unbound_fn(self, attr: Any) -> _UnboundLoad: ...

class _raiseload_loader_option(loader_option):
    def fn(self, loadopt: _L, attr: Any, sql_only: bool = ...) -> _L: ...
    def _unbound_fn(self, attr: Any, sql_only: bool = ...) -> _UnboundLoad: ...

class _defaultload_loader_option(loader_option):
    def fn(self, loadopt: _L, attr: Any) -> _L: ...
    def _unbound_fn(self, attr: Any) -> _UnboundLoad: ...

class _defer_loader_option(loader_option):
    def fn(self, loadopt: _L, key: str, raiseload: bool = ...) -> _L: ...
    def _unbound_fn(self, key: str, raiseload: bool = ...) -> _UnboundLoad: ...

class _undefer_loader_option(loader_option):
    def fn(self, loadopt: _L, key: str) -> _L: ...
    def _unbound_fn(self, key: str) -> _UnboundLoad: ...

class _undefer_group_loader_option(loader_option):
    def fn(self, loadopt: _L, name: str) -> _L: ...
    def _unbound_fn(self, name: str) -> _UnboundLoad: ...

class _with_expression_loader_option(loader_option):
    def fn(self, loadopt: _L, key: Any, expression: Any) -> _L: ...
    def _unbound_fn(
        self, loadopt: _L, key: Any, expression: Any
    ) -> _UnboundLoad: ...

class _selectin_polymorphic_loader_option(loader_option):
    def fn(self, loadopt: _L, classes: Any) -> _L: ...
    def _unbound_fn(self, classes: Any) -> _UnboundLoad: ...

contains_eager: _containseager_loader_option
load_only: _load_only_loader_option
joinedload: _joinedload_loader_option
subqueryload: _subqueryload_loader_option
selectinload: _selectinload_loader_option
lazyload: _lazyload_loader_option
immediateload: _immediateload_loader_option
noload: _noload_loader_option
raiseload: _raiseload_loader_option
defaultload: _defaultload_loader_option
defer: _defer_loader_option
undefer: _undefer_loader_option
undefer_group: _undefer_group_loader_option
with_expression: _with_expression_loader_option
selectin_polymorphic: _selectin_polymorphic_loader_option
