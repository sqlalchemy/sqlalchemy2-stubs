from typing import Any

from .base import MySQLDialect as MySQLDialect
from .base import MySQLExecutionContext as MySQLExecutionContext
from .types import TIME as TIME
from ... import util as util
from ...connectors.pyodbc import PyODBCConnector as PyODBCConnector
from ...sql.sqltypes import Time as Time

class _pyodbcTIME(TIME):
    def result_processor(self, dialect: Any, coltype: Any): ...

class MySQLExecutionContext_pyodbc(MySQLExecutionContext):
    def get_lastrowid(self): ...

class MySQLDialect_pyodbc(PyODBCConnector, MySQLDialect):
    colspecs: Any = ...
    supports_unicode_statements: bool = ...
    execution_ctx_cls: Any = ...
    pyodbc_driver_name: str = ...
    def on_connect(self): ...

dialect = MySQLDialect_pyodbc
