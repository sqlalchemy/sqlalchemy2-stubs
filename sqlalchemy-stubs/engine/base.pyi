from typing import Any
from typing import List
from typing import MutableMapping
from typing import Optional
from typing import TypeVar
from typing import Union

from typing_extensions import Literal
from typing_extensions import Protocol

from .cursor import CursorResult
from .interfaces import TypingDBAPIConnection as _DBAPIConnection
from .interfaces import TypingDBAPICursor as _DBAPICursor
from .interfaces import Connectable as Connectable
from .interfaces import Dialect
from .interfaces import ExceptionContext
from .interfaces import ExecutionContext
from .result import ScalarResult
from .url import URL
from .. import log
from .._typing import TypingExecuteOptions as _ExecuteOptions
from .._typing import TypingExecuteParams as _ExecuteParams
from ..exc import StatementError
from ..pool import Pool
from ..pool.base import TypingConnectionFairy as _ConnectionFairy

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)
_TConnection = TypeVar("_TConnection", bound=Connection)
_TTransaction = TypeVar("_TTransaction", bound=Transaction)
_TEngine = TypeVar("_TEngine", bound=Engine)

class _ConnectionCallable(Protocol[_T_contra, _T_co]):
    def __call__(
        self, __connection: _T_contra, *args: Any, **kwargs: Any
    ) -> _T_co: ...

class _ConnectionTypingCommon:
    @property
    def closed(self) -> bool: ...
    @property
    def invalidated(self) -> bool: ...
    dialect: Dialect = ...
    @property
    def default_isolation_level(self) -> Any: ...

class Connection(_ConnectionTypingCommon, Connectable):
    engine: Engine = ...
    should_close_with_result: bool = ...
    dispatch: Any = ...
    def __init__(
        self,
        engine: Engine,
        connection: Optional[_DBAPIConnection] = ...,
        close_with_result: bool = ...,
        _branch_from: Optional[Any] = ...,
        _execution_options: Optional[_ExecuteOptions] = ...,
        _dispatch: Optional[Any] = ...,
        _has_events: Optional[Any] = ...,
    ) -> None: ...
    def schema_for_object(self, obj: Any) -> str: ...
    def __enter__(self: _TConnection) -> _TConnection: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    def execution_options(self: _TConnection, **opt: Any) -> _TConnection: ...
    def get_execution_options(self) -> _ExecuteOptions: ...
    @property
    def connection(self) -> _ConnectionFairy: ...
    def get_isolation_level(self) -> Any: ...
    @property
    def info(self) -> MutableMapping[Any, Any]: ...
    def connect(self: _TConnection, close_with_result: bool = ...) -> _TConnection: ...  # type: ignore[override]
    def invalidate(self, exception: Optional[Any] = ...) -> None: ...
    def detach(self) -> None: ...
    def begin(self) -> Transaction: ...
    def begin_nested(self) -> NestedTransaction: ...
    def begin_twophase(
        self, xid: Optional[str] = ...
    ) -> TwoPhaseTransaction: ...
    def recover_twophase(self) -> None: ...
    def rollback_prepared(self, xid: str, recover: bool = ...) -> None: ...
    def commit_prepared(self, xid: str, recover: bool = ...) -> None: ...
    def in_transaction(self) -> bool: ...
    def in_nested_transaction(self) -> bool: ...
    def get_transaction(self) -> Optional[Transaction]: ...
    def get_nested_transaction(self) -> Optional[NestedTransaction]: ...
    def close(self) -> None: ...
    def scalar(
        self, object_: Any, *multiparams: Any, **params: Any
    ) -> Any: ...
    def scalars(
        self, statement: Any, *multiparams: Any, **params: Any
    ) -> ScalarResult: ...
    def execute(self, statement: Any, *multiparams: Any, **params: Any) -> CursorResult: ...  # type: ignore[override]
    def exec_driver_sql(
        self,
        statement: str,
        parameters: Optional[_ExecuteParams] = ...,
        execution_options: Optional[_ExecuteOptions] = ...,
    ) -> CursorResult: ...
    def transaction(
        self: _TConnection,
        callable_: _ConnectionCallable[_TConnection, _T],
        *args: Any,
        **kwargs: Any,
    ) -> _T: ...
    def run_callable(
        self: _TConnection,
        callable_: _ConnectionCallable[_TConnection, _T],
        *args: Any,
        **kwargs: Any,
    ) -> _T: ...

class ExceptionContextImpl(ExceptionContext):
    engine: Engine = ...
    connection: Connection = ...
    sqlalchemy_exception: Optional[StatementError] = ...
    original_exception: BaseException = ...
    execution_context: Optional[ExecutionContext] = ...
    statement: Optional[str] = ...
    parameters: Optional[Any] = ...
    is_disconnect: bool = ...
    invalidate_pool_on_disconnect: bool = ...
    def __init__(
        self,
        exception: BaseException,
        sqlalchemy_exception: Optional[StatementError],
        engine: Engine,
        connection: Optional[Connection],
        cursor: Optional[_DBAPICursor],
        statement: Optional[str],
        parameters: Optional[Any],
        context: Optional[ExecutionContext],
        is_disconnect: bool,
        invalidate_pool_on_disconnect: bool,
    ) -> None: ...

class Transaction:
    def __init__(self, connection: Connection) -> None: ...
    @property
    def is_valid(self) -> bool: ...
    def close(self) -> None: ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def __enter__(self: _TTransaction) -> _TTransaction: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...

class MarkerTransaction(Transaction):
    connection: Connection = ...
    def __init__(self, connection: Connection) -> None: ...
    @property
    def is_active(self) -> bool: ...

class RootTransaction(Transaction):
    connection: Connection = ...
    is_active: bool = ...
    def __init__(self, connection: Connection) -> None: ...

class NestedTransaction(Transaction):
    connection: Connection = ...
    is_active: bool = ...
    def __init__(self, connection: Connection) -> None: ...

class TwoPhaseTransaction(RootTransaction):
    xid: str = ...
    def __init__(self, connection: Connection, xid: str) -> None: ...
    def prepare(self) -> None: ...

class _EngineTypingCommon:
    pool: Pool = ...
    url: URL = ...
    dialect: Dialect = ...
    logging_name: Optional[str] = ...
    echo: Optional[Union[bool, Literal["debug"]]] = ...
    hide_parameters: bool = ...
    @property
    def name(self) -> str: ...
    @property
    def driver(self) -> str: ...
    def clear_compiled_cache(self) -> None: ...
    def update_execution_options(self, **opt: Any) -> None: ...
    def get_execution_options(self) -> _ExecuteOptions: ...

class Engine(_EngineTypingCommon, Connectable, log.Identified):
    @property
    def engine(self: _TEngine) -> _TEngine: ...
    hide_parameters: bool = ...
    def __init__(
        self,
        pool: Pool,
        dialect: Dialect,
        url: URL,
        logging_name: Optional[str] = ...,
        echo: Optional[Union[bool, Literal["debug"]]] = ...,
        query_cache_size: int = ...,
        execution_options: Optional[_ExecuteOptions] = ...,
        hide_parameters: bool = ...,
    ) -> None: ...
    def execution_options(self, **opt: Any) -> OptionEngine: ...
    def dispose(self) -> None: ...
    class _trans_ctx:
        conn: Connection = ...
        transaction: Transaction = ...
        close_with_result: bool = ...
        def __init__(
            self,
            conn: Connection,
            transaction: Transaction,
            close_with_result: bool,
        ) -> None: ...
        def __enter__(self) -> Connection: ...
        def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    def begin(self, close_with_result: bool = ...) -> _trans_ctx: ...
    def transaction(
        self,
        callable_: _ConnectionCallable[_TConnection, _T],
        *args: Any,
        **kwargs: Any,
    ) -> _T: ...
    def run_callable(
        self,
        callable_: _ConnectionCallable[_TConnection, _T],
        *args: Any,
        **kwargs: Any,
    ) -> _T: ...
    def execute(  # type: ignore[override]
        self, statement: Any, *multiparams: Any, **params: Any
    ) -> CursorResult: ...
    def scalar(  # type: ignore[override]
        self, statement: Any, *multiparams: Any, **params: Any
    ) -> Any: ...
    def connect(self, close_with_result: bool = ...) -> Connection: ...  # type: ignore[override]
    def table_names(
        self,
        schema: Optional[str] = ...,
        connection: Optional[Connection] = ...,
    ) -> List[str]: ...
    def has_table(
        self, table_name: str, schema: Optional[str] = ...
    ) -> bool: ...
    def raw_connection(
        self, _connection: Optional[Connection] = ...
    ) -> _DBAPIConnection: ...

class OptionEngineMixin:
    url: URL = ...
    dialect: Dialect = ...
    logging_name: Optional[str] = ...
    echo: Optional[Union[bool, Literal["debug"]]] = ...
    hide_parameters: bool = ...
    dispatch: Any = ...
    pool: Pool = ...
    def __init__(
        self, proxied: Engine, execution_options: _ExecuteOptions
    ) -> None: ...

class OptionEngine(OptionEngineMixin, Engine): ...

TypingConnectionTypingCommon=_ConnectionTypingCommon
TypingEngineTypingCommon=_EngineTypingCommon