from typing import Any
from typing import Optional

from .base import ENUM as ENUM
from .base import INTERVAL as INTERVAL
from .base import PGCompiler as PGCompiler
from .base import PGDialect as PGDialect
from .base import PGExecutionContext as PGExecutionContext
from .base import PGIdentifierPreparer as PGIdentifierPreparer
from .base import UUID as UUID
from .json import JSON as JSON
from .json import JSONB as JSONB
from .json import JSONPathType as JSONPathType
from ... import exc as exc
from ... import processors as processors
from ... import types as sqltypes
from ... import util as util
from ...sql.elements import quoted_name as quoted_name

class _PGNumeric(sqltypes.Numeric):
    def result_processor(self, dialect: Any, coltype: Any): ...

class _PGNumericNoBind(_PGNumeric):
    def bind_processor(self, dialect: Any) -> None: ...

class _PGJSON(JSON):
    def result_processor(self, dialect: Any, coltype: Any) -> None: ...
    def get_dbapi_type(self, dbapi: Any): ...

class _PGJSONB(JSONB):
    def result_processor(self, dialect: Any, coltype: Any) -> None: ...
    def get_dbapi_type(self, dbapi: Any): ...

class _PGJSONIndexType(sqltypes.JSON.JSONIndexType):
    def get_dbapi_type(self, dbapi: Any) -> None: ...

class _PGJSONIntIndexType(sqltypes.JSON.JSONIntIndexType):
    def get_dbapi_type(self, dbapi: Any): ...

class _PGJSONStrIndexType(sqltypes.JSON.JSONStrIndexType):
    def get_dbapi_type(self, dbapi: Any): ...

class _PGJSONPathType(JSONPathType):
    def get_dbapi_type(self, dbapi: Any): ...

class _PGUUID(UUID):
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class _PGEnum(ENUM):
    def get_dbapi_type(self, dbapi: Any): ...

class _PGInterval(INTERVAL):
    def get_dbapi_type(self, dbapi: Any): ...
    @classmethod
    def adapt_emulated_to_native(cls, interval: Any, **kw: Any): ...

class _PGTimeStamp(sqltypes.DateTime):
    def get_dbapi_type(self, dbapi: Any): ...

class _PGTime(sqltypes.Time):
    def get_dbapi_type(self, dbapi: Any): ...

class _PGInteger(sqltypes.Integer):
    def get_dbapi_type(self, dbapi: Any): ...

class _PGSmallInteger(sqltypes.SmallInteger):
    def get_dbapi_type(self, dbapi: Any): ...

class _PGNullType(sqltypes.NullType):
    def get_dbapi_type(self, dbapi: Any): ...

class _PGBigInteger(sqltypes.BigInteger):
    def get_dbapi_type(self, dbapi: Any): ...

class _PGBoolean(sqltypes.Boolean):
    def get_dbapi_type(self, dbapi: Any): ...

class PGExecutionContext_pg8000(PGExecutionContext):
    def pre_exec(self) -> None: ...

class PGCompiler_pg8000(PGCompiler):
    def visit_mod_binary(self, binary: Any, operator: Any, **kw: Any): ...

class PGIdentifierPreparer_pg8000(PGIdentifierPreparer):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class PGDialect_pg8000(PGDialect):
    driver: str = ...
    supports_unicode_statements: bool = ...
    supports_unicode_binds: bool = ...
    default_paramstyle: str = ...
    supports_sane_multi_rowcount: bool = ...
    execution_ctx_cls: Any = ...
    statement_compiler: Any = ...
    preparer: Any = ...
    use_setinputsizes: bool = ...
    description_encoding: Any = ...
    colspecs: Any = ...
    client_encoding: Any = ...
    def __init__(
        self, client_encoding: Optional[Any] = ..., **kwargs: Any
    ) -> None: ...
    @classmethod
    def dbapi(cls): ...
    def create_connect_args(self, url: Any): ...
    def is_disconnect(self, e: Any, connection: Any, cursor: Any): ...
    def set_isolation_level(self, connection: Any, level: Any) -> None: ...
    def set_readonly(self, connection: Any, value: Any) -> None: ...
    def get_readonly(self, connection: Any): ...
    def set_deferrable(self, connection: Any, value: Any) -> None: ...
    def get_deferrable(self, connection: Any): ...
    def set_client_encoding(
        self, connection: Any, client_encoding: Any
    ) -> None: ...
    def do_set_input_sizes(
        self, cursor: Any, list_of_tuples: Any, context: Any
    ) -> None: ...
    def do_begin_twophase(self, connection: Any, xid: Any) -> None: ...
    def do_prepare_twophase(self, connection: Any, xid: Any) -> None: ...
    def do_rollback_twophase(
        self,
        connection: Any,
        xid: Any,
        is_prepared: bool = ...,
        recover: bool = ...,
    ) -> None: ...
    def do_commit_twophase(
        self,
        connection: Any,
        xid: Any,
        is_prepared: bool = ...,
        recover: bool = ...,
    ) -> None: ...
    def do_recover_twophase(self, connection: Any): ...
    def on_connect(self): ...

dialect = PGDialect_pg8000
