import sys
from typing import Any
from typing import Callable
from typing import Collection
from typing import ContextManager
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Type
from typing import TypeVar
from typing import Union

from typing_extensions import Literal
from typing_extensions import Protocol

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
_TSessionTransaction = TypeVar(
    "_TSessionTransaction", bound=SessionTransaction
)

_TSharedSessionProtocol = TypeVar(
    "_TSharedSessionProtocol", bound=_SharedSessionProtocol[Any]
)
_TSessionTransactionProtocol = TypeVar(
    "_TSessionTransactionProtocol", bound=_SessionTransactionProtocol
)
_TSessionProtocol = TypeVar("_TSessionProtocol", bound=_SessionProtocol)

_BindArguments = Mapping[str, Any]

class _IdentityMap:
    @overload
    def __get__(self, instance: None, owner: Any) -> None: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> WeakInstanceDict: ...

class _SharedSessionProtocol(Protocol[_T]):
    identity_map: _IdentityMap
    autoflush: bool
    @property
    def dirty(self) -> util.IdentitySet[Any]: ...
    @property
    def deleted(self) -> util.IdentitySet[Any]: ...
    @property
    def new(self) -> util.IdentitySet[Any]: ...
    @property
    def is_active(self) -> bool: ...
    @property
    def no_autoflush(
        self: _TSharedSessionProtocol,
    ) -> ContextManager[_TSharedSessionProtocol]: ...
    @util.memoized_property
    def info(self) -> Mapping[Any, Any]: ...
    def __contains__(self, instance: Any) -> bool: ...
    def __iter__(self) -> Iterator[Any]: ...
    def add(self, instance: Any, _warn: bool = ...) -> None: ...
    def add_all(self, instances: Iterable[Any]) -> None: ...
    def expire_all(self) -> None: ...
    def expire(
        self, instance: Any, attribute_names: Optional[Iterable[str]] = ...
    ) -> None: ...
    def expunge(self, instance: Any) -> None: ...
    def expunge_all(self) -> None: ...
    def get_bind(
        self,
        mapper: Optional[Any] = ...,
        clause: Optional[ClauseElement] = ...,
        bind: Optional[_T] = ...,
        _sa_skip_events: Optional[Any] = ...,
        _sa_skip_for_implicit_returning: bool = ...,
    ) -> _T: ...
    def is_modified(
        self, instance: Any, include_collections: bool = ...
    ) -> bool: ...
    def in_transaction(self) -> bool: ...

class _SessionProtocol(
    _SharedSessionProtocol[Union[Connection, Engine]], Protocol
):
    def __enter__(self: _TSessionProtocol) -> _TSessionProtocol: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    def begin(
        self,
        subtransactions: bool = ...,  # NOTE: Deprecated.
        nested: bool = ...,
    ) -> _SessionTransactionProtocol: ...
    def begin_nested(self) -> _SessionTransactionProtocol: ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def connection(self) -> Connection: ...
    def execute(
        self,
        statement: Executable,
        params: Optional[
            Union[Mapping[str, Any], Sequence[Mapping[str, Any]]]
        ] = ...,
        execution_options: _ExecutionOptions = ...,
        bind_arguments: Optional[_BindArguments] = ...,
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
    def refresh(
        self,
        instance: Any,
        attribute_names: Optional[Iterable[str]] = ...,
        with_for_update: Optional[
            Union[Literal[True], Mapping[str, Any]]
        ] = ...,
    ) -> None: ...
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
    def flush(self, objects: Optional[Collection[Any]] = ...) -> None: ...
    @classmethod
    def close_all(cls) -> None: ...  # NOTE: Deprecated.

class _SessionTransactionProtocol(Protocol):
    nested: bool
    @property
    def is_active(self) -> bool: ...
    @property
    def parent(
        self,
    ) -> Optional[_SessionTransactionProtocol]: ...
    def connection(
        self,
        bindkey: Any,
        execution_options: Optional[_ExecutionOptions] = ...,
        **kwargs: Any,
    ) -> Connection: ...
    def prepare(self) -> None: ...
    def commit(self) -> Optional[_SessionTransactionProtocol]: ...
    def rollback(self) -> Optional[_SessionTransactionProtocol]: ...
    def close(self, invalidate: bool = ...) -> None: ...
    def __enter__(
        self: _TSessionTransactionProtocol,
    ) -> _TSessionTransactionProtocol: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...

if sys.version_info >= (3, 0):
    from typing import Generator
    from ..ext.asyncio import AsyncEngine, AsyncConnection

    _TSessionMakerType = TypeVar(
        "_TSessionMakerType",
        bound=Union[_SessionProtocol, _AsyncSessionProtocol],
    )
    _TAsyncSessionTransactionProtocol = TypeVar(
        "_TAsyncSessionTransactionProtocol",
        bound=_AsyncSessionTransactionProtocol,
    )
    _TAsyncSessionProtocol = TypeVar(
        "_TAsyncSessionProtocol", bound=_AsyncSessionProtocol
    )
    class _AsyncSessionTransactionProtocol(Protocol):
        @property
        def is_active(self) -> bool: ...
        async def commit(
            self,
        ) -> Optional[_AsyncSessionTransactionProtocol]: ...
        async def rollback(
            self,
        ) -> Optional[_AsyncSessionTransactionProtocol]: ...
        async def start(
            self: _TAsyncSessionTransactionProtocol,
        ) -> _TAsyncSessionTransactionProtocol: ...
        def __await__(
            self: _TAsyncSessionTransactionProtocol,
        ) -> Generator[Any, None, _TAsyncSessionTransactionProtocol]: ...
        async def __aenter__(
            self: _TAsyncSessionTransactionProtocol,
        ) -> _TAsyncSessionTransactionProtocol: ...
        async def __aexit__(
            self, type_: Any, value: Any, traceback: Any
        ) -> None: ...
    class _AsyncSessionProtocol(
        _SharedSessionProtocol[Union[AsyncConnection, AsyncEngine]], Protocol
    ):
        async def __aenter__(
            self: _TAsyncSessionProtocol,
        ) -> _TAsyncSessionProtocol: ...
        async def __aexit__(
            self, type_: Any, value: Any, traceback: Any
        ) -> None: ...
        def begin(self) -> _AsyncSessionTransactionProtocol: ...
        def begin_nested(self) -> _AsyncSessionTransactionProtocol: ...
        async def rollback(self) -> None: ...
        async def commit(self) -> None: ...
        async def connection(self) -> Any: ...
        async def execute(
            self,
            statement: Executable,
            params: Optional[
                Union[Mapping[str, Any], Sequence[Mapping[str, Any]]]
            ] = ...,
            execution_options: _ExecutionOptions = ...,
            bind_arguments: Optional[_BindArguments] = ...,
            **kw: Any,
        ) -> Result: ...
        async def scalar(
            self,
            statement: Executable,
            params: Optional[
                Union[Mapping[str, Any], Sequence[Mapping[str, Any]]]
            ] = ...,
            execution_options: _ExecutionOptions = ...,
            bind_arguments: Optional[_BindArguments] = ...,
            **kw: Any,
        ) -> Any: ...
        async def close(self) -> None: ...
        async def refresh(
            self,
            instance: Any,
            attribute_names: Optional[Iterable[str]] = ...,
            with_for_update: Optional[
                Union[Literal[True], Mapping[str, Any]]
            ] = ...,
        ) -> None: ...
        async def get(
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
        async def stream(
            self,
            statement: Any,
            params: Optional[
                Union[Mapping[str, Any], Sequence[Mapping[str, Any]]]
            ] = ...,
            execution_options: _ExecutionOptions = ...,
            bind_arguments: Optional[_BindArguments] = ...,
            **kw: Any,
        ) -> Any: ...
        async def delete(self, instance: Any) -> None: ...
        async def merge(self, instance: _T, load: bool = ...) -> _T: ...
        async def flush(
            self, objects: Optional[Collection[Any]] = ...
        ) -> None: ...
        @classmethod
        async def close_all(cls) -> None: ...  # NOTE: Deprecated.

else:
    _TSessionMakerType = TypeVar("_TSessionMakerType", bound=_SessionProtocol)

class _SessionClassMethods:
    @classmethod
    def close_all(cls) -> None: ...  # NOTE: Deprecated.
    @classmethod
    def identity_key(cls, *args: Any, **kwargs: Any) -> Any: ...
    @classmethod
    def object_session(cls, instance: Any) -> Session: ...

ACTIVE: util.langhelpers._symbol
PREPARED: util.langhelpers._symbol
COMMITTED: util.langhelpers._symbol
DEACTIVE: util.langhelpers._symbol
CLOSED: util.langhelpers._symbol

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
    ) -> Any: ...
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
    def __enter__(self: _TSessionTransaction) -> _TSessionTransaction: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...

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
        query_cls: Optional[
            Union[Type[Query[Any]], Callable[..., Query[Any]]]
        ] = ...,
    ) -> None: ...
    connection_callable: Any = ...
    def __enter__(self: _TSession) -> _TSession: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    @property
    def transaction(
        self,
    ) -> Optional[SessionTransaction]: ...  # NOTE: Deprecated.
    def in_transaction(self) -> bool: ...
    def in_nested_transaction(self) -> bool: ...
    def get_transaction(self) -> Optional[SessionTransaction]: ...
    def get_nested_transaction(self) -> Optional[SessionTransaction]: ...
    @util.memoized_property
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
    def query(self, *entities: Any, **kwargs: Any) -> Query[Any]: ...
    @property
    def no_autoflush(self: _TSession) -> ContextManager[_TSession]: ...
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
    def flush(self, objects: Optional[Collection[Any]] = ...) -> None: ...
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
    def dirty(self) -> util.IdentitySet[Any]: ...
    @property
    def deleted(self) -> util.IdentitySet[Any]: ...
    @property
    def new(self) -> util.IdentitySet[Any]: ...

class sessionmaker(_SessionClassMethods, Generic[_TSessionMakerType]):
    kw: Mapping[str, Any]
    class_: Type[_TSessionMakerType]
    if sys.version_info >= (3, 0):
        @overload
        def __init__(
            self: sessionmaker[Session],
            bind: Optional[Union[Connection, Engine]] = ...,
            class_: None = ...,
            autoflush: bool = ...,
            autocommit: bool = ...,  # NOTE: Deprecated.
            expire_on_commit: bool = ...,
            info: Optional[Mapping[Any, Any]] = ...,
            **kw: Any,
        ) -> None: ...
        @overload
        def __init__(
            self,
            bind: Optional[
                Union[Connection, Engine, AsyncConnection, AsyncEngine]
            ],
            class_: Type[_TSessionMakerType],
            autoflush: bool = ...,
            autocommit: bool = ...,  # NOTE: Deprecated.
            expire_on_commit: bool = ...,
            info: Optional[Mapping[Any, Any]] = ...,
            **kw: Any,
        ) -> None: ...
        @overload
        def __init__(
            self,
            *,
            bind: Optional[
                Union[Connection, Engine, AsyncConnection, AsyncEngine]
            ] = ...,
            class_: Type[_TSessionMakerType],
            autoflush: bool = ...,
            autocommit: bool = ...,  # NOTE: Deprecated.
            expire_on_commit: bool = ...,
            info: Optional[Mapping[Any, Any]] = ...,
            **kw: Any,
        ) -> None: ...
    else:
        @overload
        def __init__(
            self: sessionmaker[Session],
            bind: Optional[Union[Connection, Engine]] = ...,
            class_: None = ...,
            autoflush: bool = ...,
            autocommit: bool = ...,  # NOTE: Deprecated.
            expire_on_commit: bool = ...,
            info: Optional[Mapping[Any, Any]] = ...,
            **kw: Any,
        ) -> None: ...
        @overload
        def __init__(
            self,
            bind: Optional[Union[Connection, Engine]],
            class_: Type[_TSessionMakerType],
            autoflush: bool = ...,
            autocommit: bool = ...,  # NOTE: Deprecated.
            expire_on_commit: bool = ...,
            info: Optional[Mapping[Any, Any]] = ...,
            **kw: Any,
        ) -> None: ...
        @overload
        def __init__(
            self,
            *,
            bind: Optional[Union[Connection, Engine]] = ...,
            class_: Type[_TSessionMakerType],
            autoflush: bool = ...,
            autocommit: bool = ...,  # NOTE: Deprecated.
            expire_on_commit: bool = ...,
            info: Optional[Mapping[Any, Any]] = ...,
            **kw: Any,
        ) -> None: ...
    # NOTE: The return type of `begin()` isn't technically correct, but since
    # `Session.__enter__` and `AsyncSession.__aenter__` both return self,
    # returning `_TSessionMakerType` from `begin()` works out mostly
    # structurally the same as what actually takes place in `sessionmaker.begin()`
    def begin(self) -> _TSessionMakerType: ...
    def __call__(self, **local_kw: Any) -> _TSessionMakerType: ...
    def configure(self, **new_kw: Any) -> None: ...

def close_all_sessions() -> None: ...
def make_transient(instance: object) -> None: ...
def make_transient_to_detached(instance: object) -> None: ...

if sys.version_info >= (3, 0):
    def object_session(
        instance: object,
    ) -> Optional[Union[Session, _SessionProtocol, _AsyncSessionProtocol]]: ...

else:
    def object_session(instance: object) -> Session: ...
