from typing import Any
from typing import Optional

from .. import event as event
from .. import exc as exc
from .. import log as log
from .. import util as util

reset_rollback: Any
reset_commit: Any
reset_none: Any

class _ConnDialect:
    is_async: bool = ...
    def do_rollback(self, dbapi_connection: Any) -> None: ...
    def do_commit(self, dbapi_connection: Any) -> None: ...
    def do_close(self, dbapi_connection: Any) -> None: ...
    def do_ping(self, dbapi_connection: Any) -> None: ...

class Pool(log.Identified):
    logging_name: Any = ...
    echo: Any = ...
    def __init__(
        self,
        creator: Any,
        recycle: int = ...,
        echo: Optional[Any] = ...,
        logging_name: Optional[Any] = ...,
        reset_on_return: bool = ...,
        events: Optional[Any] = ...,
        dialect: Optional[Any] = ...,
        pre_ping: bool = ...,
        _dispatch: Optional[Any] = ...,
    ) -> None: ...
    def recreate(self) -> None: ...
    def dispose(self) -> None: ...
    def connect(self): ...
    def status(self) -> None: ...

class _ConnectionRecord:
    finalize_callback: Any = ...
    def __init__(self, pool: Any, connect: bool = ...) -> None: ...
    fresh: bool = ...
    fairy_ref: Any = ...
    starttime: Any = ...
    connection: Any = ...
    @util.memoized_property
    def info(self): ...
    @util.memoized_property
    def record_info(self): ...
    @classmethod
    def checkout(cls, pool: Any): ...
    def checkin(self, _fairy_was_created: bool = ...) -> None: ...
    @property
    def in_use(self): ...
    @property
    def last_connect_time(self): ...
    def close(self) -> None: ...
    def invalidate(self, e: Optional[Any] = ..., soft: bool = ...) -> None: ...
    def get_connection(self): ...

class _ConnectionFairy:
    connection: Any = ...
    def __init__(
        self, dbapi_connection: Any, connection_record: Any, echo: Any
    ) -> None: ...
    @property
    def is_valid(self): ...
    @util.memoized_property
    def info(self): ...
    @property
    def record_info(self): ...
    def invalidate(self, e: Optional[Any] = ..., soft: bool = ...) -> None: ...
    def cursor(self, *args: Any, **kwargs: Any): ...
    def __getattr__(self, key: Any): ...
    def detach(self) -> None: ...
    def close(self) -> None: ...
