from typing import Any
from typing import Optional

from ... import Computed as Computed
from ... import exc as exc
from ... import sql as sql
from ... import util as util
from ...engine import default as default
from ...engine import reflection as reflection
from ...sql import compiler as compiler
from ...sql import expression as expression
from ...sql import sqltypes as sqltypes
from ...sql import visitors as visitors
from ...types import BLOB as BLOB
from ...types import CHAR as CHAR
from ...types import CLOB as CLOB
from ...types import FLOAT as FLOAT
from ...types import INTEGER as INTEGER
from ...types import Integer as Integer
from ...types import NCHAR as NCHAR
from ...types import NVARCHAR as NVARCHAR
from ...types import TIMESTAMP as TIMESTAMP
from ...types import VARCHAR as VARCHAR
from ...util import compat as compat

RESERVED_WORDS: Any
NO_ARG_FNS: Any

class RAW(sqltypes.TypingBinary):
    __visit_name__: str = ...

OracleRaw = RAW

class NCLOB(sqltypes.Text):
    __visit_name__: str = ...

class VARCHAR2(VARCHAR):
    __visit_name__: str = ...

NVARCHAR2 = NVARCHAR

class NUMBER(sqltypes.Numeric, sqltypes.Integer):
    __visit_name__: str = ...
    def __init__(
        self,
        precision: Optional[Any] = ...,
        scale: Optional[Any] = ...,
        asdecimal: Optional[Any] = ...,
    ) -> None: ...
    def adapt(self, impltype: Any): ...

class DOUBLE_PRECISION(sqltypes.Float):
    __visit_name__: str = ...

class BINARY_DOUBLE(sqltypes.Float):
    __visit_name__: str = ...

class BINARY_FLOAT(sqltypes.Float):
    __visit_name__: str = ...

class BFILE(sqltypes.LargeBinary):
    __visit_name__: str = ...

class LONG(sqltypes.Text):
    __visit_name__: str = ...

class DATE(sqltypes.DateTime):
    __visit_name__: str = ...

class INTERVAL(sqltypes.NativeForEmulated, sqltypes._AbstractInterval):
    __visit_name__: str = ...
    day_precision: Any = ...
    second_precision: Any = ...
    def __init__(
        self,
        day_precision: Optional[Any] = ...,
        second_precision: Optional[Any] = ...,
    ) -> None: ...
    def as_generic(self, allow_nulltype: bool = ...): ...

class ROWID(sqltypes.TypeEngine):
    __visit_name__: str = ...

class _OracleBoolean(sqltypes.Boolean):
    def get_dbapi_type(self, dbapi: Any): ...

colspecs: Any
ischema_names: Any

class OracleTypeCompiler(compiler.GenericTypeCompiler):
    def visit_datetime(self, type_: Any, **kw: Any): ...
    def visit_float(self, type_: Any, **kw: Any): ...
    def visit_unicode(self, type_: Any, **kw: Any): ...
    def visit_INTERVAL(self, type_: Any, **kw: Any): ...
    def visit_LONG(self, type_: Any, **kw: Any): ...
    def visit_TIMESTAMP(self, type_: Any, **kw: Any): ...
    def visit_DOUBLE_PRECISION(self, type_: Any, **kw: Any): ...
    def visit_BINARY_DOUBLE(self, type_: Any, **kw: Any): ...
    def visit_BINARY_FLOAT(self, type_: Any, **kw: Any): ...
    def visit_FLOAT(self, type_: Any, **kw: Any): ...
    def visit_NUMBER(self, type_: Any, **kw: Any): ...
    def visit_string(self, type_: Any, **kw: Any): ...
    def visit_VARCHAR2(self, type_: Any, **kw: Any): ...
    def visit_NVARCHAR2(self, type_: Any, **kw: Any): ...
    visit_NVARCHAR: Any = ...
    def visit_VARCHAR(self, type_: Any, **kw: Any): ...
    def visit_text(self, type_: Any, **kw: Any): ...
    def visit_unicode_text(self, type_: Any, **kw: Any): ...
    def visit_large_binary(self, type_: Any, **kw: Any): ...
    def visit_big_integer(self, type_: Any, **kw: Any): ...
    def visit_boolean(self, type_: Any, **kw: Any): ...
    def visit_RAW(self, type_: Any, **kw: Any): ...
    def visit_ROWID(self, type_: Any, **kw: Any): ...

class OracleCompiler(compiler.SQLCompiler):
    compound_keywords: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def visit_mod_binary(self, binary: Any, operator: Any, **kw: Any): ...
    def visit_now_func(self, fn: Any, **kw: Any): ...
    def visit_char_length_func(self, fn: Any, **kw: Any): ...
    def visit_match_op_binary(self, binary: Any, operator: Any, **kw: Any): ...
    def visit_true(self, expr: Any, **kw: Any): ...
    def visit_false(self, expr: Any, **kw: Any): ...
    def get_cte_preamble(self, recursive: Any): ...
    def get_select_hint_text(self, byfroms: Any): ...
    def function_argspec(self, fn: Any, **kw: Any): ...
    def visit_function(self, func: Any, **kw: Any): ...
    def visit_table_valued_column(self, element: Any, **kw: Any): ...
    def default_from(self): ...
    def visit_join(
        self, join: Any, from_linter: Optional[Any] = ..., **kwargs: Any
    ): ...
    def visit_outer_join_column(self, vc: Any, **kw: Any): ...
    def visit_sequence(self, seq: Any, **kw: Any): ...
    def get_render_as_alias_suffix(self, alias_name_text: Any): ...
    has_out_parameters: bool = ...
    def returning_clause(self, stmt: Any, returning_cols: Any): ...
    def translate_select_structure(self, select_stmt: Any, **kwargs: Any): ...
    def limit_clause(self, select: Any, **kw: Any): ...
    def visit_empty_set_expr(self, type_: Any): ...
    def for_update_clause(self, select: Any, **kw: Any): ...
    def visit_is_distinct_from_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_is_not_distinct_from_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_regexp_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_not_regexp_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...
    def visit_regexp_replace_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ): ...

class OracleDDLCompiler(compiler.DDLCompiler):
    def define_constraint_cascades(self, constraint: Any): ...
    def visit_drop_table_comment(self, drop: Any): ...
    def visit_create_index(self, create: Any): ...
    def post_create_table(self, table: Any): ...
    def get_identity_options(self, identity_options: Any): ...
    def visit_computed_column(self, generated: Any): ...
    def visit_identity_column(self, identity: Any, **kw: Any): ...

class OracleIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words: Any = ...
    illegal_initial_characters: Any = ...
    def format_savepoint(self, savepoint: Any): ...

class OracleExecutionContext(default.DefaultExecutionContext):
    def fire_sequence(self, seq: Any, type_: Any): ...

class OracleDialect(default.DefaultDialect):
    name: str = ...
    supports_alter: bool = ...
    supports_unicode_statements: bool = ...
    supports_unicode_binds: bool = ...
    max_identifier_length: int = ...
    supports_simple_order_by_label: bool = ...
    cte_follows_insert: bool = ...
    supports_sequences: bool = ...
    sequences_optional: bool = ...
    postfetch_lastrowid: bool = ...
    default_paramstyle: str = ...
    colspecs: Any = ...
    ischema_names: Any = ...
    requires_name_normalize: bool = ...
    supports_comments: bool = ...
    supports_default_values: bool = ...
    supports_empty_insert: bool = ...
    statement_compiler: Any = ...
    ddl_compiler: Any = ...
    type_compiler: Any = ...
    preparer: Any = ...
    execution_ctx_cls: Any = ...
    reflection_options: Any = ...
    construct_arguments: Any = ...
    use_ansi: Any = ...
    optimize_limits: Any = ...
    exclude_tablespaces: Any = ...
    def __init__(
        self,
        use_ansi: bool = ...,
        optimize_limits: bool = ...,
        use_binds_for_limits: Optional[Any] = ...,
        use_nchar_for_unicode: bool = ...,
        exclude_tablespaces: Any = ...,
        **kwargs: Any,
    ) -> None: ...
    implicit_returning: Any = ...
    def initialize(self, connection: Any) -> None: ...
    def do_release_savepoint(self, connection: Any, name: Any) -> None: ...
    def get_isolation_level(self, connection: Any) -> None: ...
    def get_default_isolation_level(self, dbapi_conn: Any): ...
    def set_isolation_level(self, connection: Any, level: Any) -> None: ...
    def has_table(
        self, connection: Any, table_name: Any, schema: Optional[Any] = ...
    ): ...
    def has_sequence(
        self, connection: Any, sequence_name: Any, schema: Optional[Any] = ...
    ): ...
    def get_schema_names(self, connection: Any, **kw: Any): ...
    def get_table_names(
        self, connection: Any, schema: Optional[Any] = ..., **kw: Any
    ): ...
    def get_temp_table_names(self, connection: Any, **kw: Any): ...
    def get_view_names(
        self, connection: Any, schema: Optional[Any] = ..., **kw: Any
    ): ...
    def get_sequence_names(
        self, connection: Any, schema: Optional[Any] = ..., **kw: Any
    ): ...
    def get_table_options(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def get_columns(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def get_table_comment(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        resolve_synonyms: bool = ...,
        dblink: str = ...,
        **kw: Any,
    ): ...
    def get_indexes(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        resolve_synonyms: bool = ...,
        dblink: str = ...,
        **kw: Any,
    ): ...
    def get_pk_constraint(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def get_foreign_keys(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def get_unique_constraints(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        **kw: Any,
    ): ...
    def get_view_definition(
        self,
        connection: Any,
        view_name: Any,
        schema: Optional[Any] = ...,
        resolve_synonyms: bool = ...,
        dblink: str = ...,
        **kw: Any,
    ): ...
    def get_check_constraints(
        self,
        connection: Any,
        table_name: Any,
        schema: Optional[Any] = ...,
        include_all: bool = ...,
        **kw: Any,
    ): ...

class _OuterJoinColumn(sql.ClauseElement):
    __visit_name__: str = ...
    column: Any = ...
    def __init__(self, column: Any) -> None: ...
