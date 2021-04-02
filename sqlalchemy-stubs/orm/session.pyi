from typing import Any
from typing import Callable
from typing import ContextManager
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import MutableSet
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Type
from typing import TypeVar
from typing import Union

from typing_extensions import Literal

from .identity import WeakInstanceDict
from .mapper import Mapper
from .path_registry import PathRegistry
from .query import Query
from .state import InstanceState
from .. import util
from ..engine import Connection
from ..engine import Engine
from ..engine import Result
from ..engine.base import _ExecutionOptions
from ..sql import ClauseElement
from ..sql import Executable
from ..sql.base import Options

_T = TypeVar("_T")
_TSession = TypeVar("_TSession", bound=Session)

_BindArguments = Mapping[str, Any]

class _SessionClassMethods:
    @classmethod
    def close_all(cls) -> None: ...  # NOTE: Deprecated.
    @classmethod
    def identity_key(cls, *args: Any, **kwargs: Any): ...
    @classmethod
    def object_session(cls, instance: Any) -> Session: ...

class ORMExecuteState(util.MemoizedSlots):
    session: Session
    statement: Executable
    parameters: Mapping[str, Any]
    local_execution_options: Any
    execution_options: Any
    bind_arguments: _BindArguments
    def __init__(
        self,
        session: Session,
        statement: Executable,
        parameters: Mapping[str, Any],
        execution_options: _ExecutionOptions,
        bind_arguments: _BindArguments,
        compile_state_cls: Any,
        events_todo: Any,
    ) -> None: ...
    def invoke_statement(
        self,
        statement: Optional[Any] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        execution_options: _ExecutionOptions = ...,
        bind_arguments: Optional[_BindArguments] = ...,
    ): ...
    @property
    def bind_mapper(self) -> Mapper: ...
    @property
    def all_mappers(self) -> List[Mapper]: ...
    @property
    def is_orm_statement(self) -> bool: ...
    @property
    def is_select(self) -> bool: ...
    @property
    def is_insert(self) -> bool: ...
    @property
    def is_update(self) -> bool: ...
    @property
    def is_delete(self) -> bool: ...
    def update_execution_options(self, **opts: Any) -> None: ...
    @property
    def lazy_loaded_from(self) -> InstanceState: ...
    @property
    def loader_strategy_path(self) -> Optional[PathRegistry]: ...
    @property
    def is_column_load(self) -> bool: ...
    @property
    def is_relationship_load(self) -> bool: ...
    @property
    def load_options(self) -> Options: ...
    @property
    def update_delete_options(self) -> Options: ...
    @property
    def user_defined_options(self) -> List[Options]: ...

class SessionTransaction:
    session: Session
    nested: bool
    def __init__(
        self,
        session: Session,
        parent: Optional[SessionTransaction] = ...,
        nested: bool = ...,
        autobegin: bool = ...,
    ) -> None: ...
    @property
    def parent(self) -> SessionTransaction: ...
    @property
    def is_active(self) -> bool: ...
    def connection(
        self,
        bindkey: Any,
        execution_options: Optional[_ExecutionOptions] = ...,
        **kwargs: Any,
    ) -> Connection: ...
    def prepare(self) -> None: ...
    def commit(self, _to_root: bool = ...) -> Optional[SessionTransaction]: ...
    def rollback(
        self, _capture_exception: bool = ..., _to_root: bool = ...
    ) -> Optional[SessionTransaction]: ...
    def close(self, invalidate: bool = ...) -> None: ...
    def __enter__(self) -> SessionTransaction: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...

class _IdentityMap:
    @overload
    def __get__(self, instance: None, owner: Any) -> None: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> WeakInstanceDict: ...

class Session(_SessionClassMethods):
    identity_map: _IdentityMap
    bind: Optional[Union[Connection, Engine]]
    future: bool
    hash_key: int
    autoflush: bool
    expire_on_commit: bool
    enable_baked_queries: bool
    autocommit: bool
    twophase: bool
    def __init__(
        self,
        bind: Optional[Union[Connection, Engine]] = ...,
        autoflush: bool = ...,
        future: bool = ...,
        expire_on_commit: bool = ...,
        autocommit: bool = ...,  # NOTE: Deprecated.
        twophase: bool = ...,
        binds: Optional[Mapping[Any, Union[Connection, Engine]]] = ...,
        enable_baked_queries: bool = ...,
        info: Optional[Mapping[Any, Any]] = ...,
        query_cls: Optional[Union[Query, Callable[..., Query]]] = ...,
    ) -> None: ...
    connection_callable: Any = ...
    def __enter__(self) -> Session: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    @property
    def transaction(
        self,
    ) -> Optional[SessionTransaction]: ...  # NOTE: Deprecated.
    def in_transaction(self) -> bool: ...
    def in_nested_transaction(self) -> bool: ...
    def get_transaction(self) -> Optional[SessionTransaction]: ...
    def get_nested_transaction(self) -> Optional[SessionTransaction]: ...
    def info(self) -> Mapping[Any, Any]: ...
    def begin(
        self,
        subtransactions: bool = ...,  # NOTE: Deprecated.
        nested: bool = ...,
        _subtrans: bool = ...,
    ) -> SessionTransaction: ...
    def begin_nested(self) -> SessionTransaction: ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def prepare(self) -> None: ...
    def connection(
        self,
        bind_arguments: Optional[_BindArguments] = ...,
        close_with_result: bool = ...,
        execution_options: _ExecutionOptions = ...,
        **kw: Any,
    ) -> Connection: ...
    def execute(
        self,
        statement: Executable,
        params: Optional[
            Union[Mapping[str, Any], Sequence[Mapping[str, Any]]]
        ] = ...,
        execution_options: _ExecutionOptions = ...,
        bind_arguments: Optional[_BindArguments] = ...,
        _parent_execute_state: Optional[Any] = ...,
        _add_event: Optional[Any] = ...,
        **kw: Any,
    ) -> Result: ...
    def scalar(
        self,
        statement: Executable,
        params: Optional[
            Union[Mapping[str, Any], Sequence[Mapping[str, Any]]]
        ] = ...,
        execution_options: _ExecutionOptions = ...,
        bind_arguments: Optional[_BindArguments] = ...,
        **kw: Any,
    ) -> Any: ...
    def close(self) -> None: ...
    def invalidate(self) -> None: ...
    def expunge_all(self) -> None: ...
    def bind_mapper(self, mapper: Any, bind: Any) -> None: ...
    def bind_table(self, table: Any, bind: Any) -> None: ...
    def get_bind(
        self,
        mapper: Optional[Any] = ...,
        clause: Optional[ClauseElement] = ...,
        bind: Optional[Union[Connection, Engine]] = ...,
        _sa_skip_events: Optional[Any] = ...,
        _sa_skip_for_implicit_returning: bool = ...,
    ) -> Union[Connection, Engine]: ...
    def query(self, *entities: Any, **kwargs: Any) -> Query: ...
    @property
    def no_autoflush(self) -> ContextManager[Session]: ...
    def refresh(
        self,
        instance: Any,
        attribute_names: Optional[Iterable[str]] = ...,
        with_for_update: Optional[
            Union[Literal[True], Mapping[str, Any]]
        ] = ...,
    ) -> None: ...
    def expire_all(self) -> None: ...
    def expire(
        self, instance: Any, attribute_names: Optional[Iterable[str]] = ...
    ) -> None: ...
    def expunge(self, instance: Any) -> None: ...
    def add(self, instance: Any, _warn: bool = ...) -> None: ...
    def add_all(self, instances: Any) -> None: ...
    def delete(self, instance: Any) -> None: ...
    def get(
        self,
        entity: Any,
        ident: Any,
        options: Optional[Sequence[Any]] = ...,
        populate_existing: bool = ...,
        with_for_update: Optional[
            Union[Literal[True], Mapping[str, Any]]
        ] = ...,
        identity_token: Optional[Any] = ...,
    ) -> Any: ...
    def merge(self, instance: _T, load: bool = ...) -> _T: ...
    def enable_relationship_loading(self, obj: Any) -> None: ...
    def __contains__(self, instance: Any) -> bool: ...
    def __iter__(self) -> Iterator[Any]: ...
    def flush(self, objects: Optional[Sequence[Any]] = ...) -> None: ...
    def bulk_save_objects(
        self,
        objects: Sequence[Any],
        return_defaults: bool = ...,
        update_changed_only: bool = ...,
        preserve_order: bool = ...,
    ) -> None: ...
    def bulk_insert_mappings(
        self,
        mapper: Any,
        mappings: Sequence[Mapping[str, Any]],
        return_defaults: bool = ...,
        render_nulls: bool = ...,
    ) -> None: ...
    def bulk_update_mappings(
        self, mapper: Any, mappings: Sequence[Mapping[str, Any]]
    ) -> None: ...
    def is_modified(
        self, instance: Any, include_collections: bool = ...
    ) -> bool: ...
    @property
    def is_active(self) -> bool: ...
    @property
    def dirty(self) -> MutableSet[Any]: ...
    @property
    def deleted(self) -> MutableSet[Any]: ...
    @property
    def new(self) -> MutableSet[Any]: ...

class sessionmaker(_SessionClassMethods, Generic[_TSession]):
    kw: Mapping[str, Any]
    class_: Type[_TSession]
    # NOTE: ``sessionmaker`` does not implement ``__new__``.
    #       It is done this way here for lack of a type variable default
    #       in the common case where the ``class_`` is of type ``Session``
    #       and no star args are passed.
    #       See https://github.com/python/mypy/issues/4236
    @overload
    def __new__(
        cls,
        bind: Optional[Union[Connection, Engine]] = ...,
        autoflush: bool = ...,
        autocommit: bool = ...,  # NOTE: Deprecated.
        expire_on_commit: bool = ...,
        info: Optional[Mapping[Any, Any]] = ...,
    ) -> sessionmaker[Session]: ...
    @overload
    def __new__(
        cls,
        bind: Optional[Union[Connection, Engine]] = ...,
        class_: Type[_TSession] = ...,
        autoflush: bool = ...,
        autocommit: bool = ...,  # NOTE: Deprecated.
        expire_on_commit: bool = ...,
        info: Optional[Mapping[Any, Any]] = ...,
        **kw: Any,
    ) -> sessionmaker[_TSession]: ...
    def begin(self) -> SessionTransaction: ...
    def __call__(self, **local_kw: Any) -> _TSession: ...
    def configure(self, **new_kw: Any) -> None: ...

def close_all_sessions() -> None: ...
def make_transient(instance: object) -> Any: ...
def make_transient_to_detached(instance: object) -> Any: ...
def object_session(instance: object) -> Session: ...
