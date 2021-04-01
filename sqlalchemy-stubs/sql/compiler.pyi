import sys
from typing import Any
from typing import Dict
from typing import List
from typing import NamedTuple
from typing import Optional
from typing import Pattern
from typing import Set
from typing import Tuple
from typing import TypeVar
from typing import Union

from . import dml
from . import elements
from . import selectable
from .base import CompileState
from .elements import ClauseElement
from .schema import Table
from .type_api import TypeEngine
from .. import util
from ..util import langhelpers

_T = TypeVar("_T")
_U = TypeVar("_U")
_TE = TypeVar("_TE", bound=TypeEngine[Any])
_CL = TypeVar("_CL", bound=_CompileLabel[Any])
_SC = TypeVar("_SC", bound=SQLCompiler)

if sys.version_info >= (3, 0):
    _VisitResult = str
else:
    _VisitResult = Union[str, unicode]  # noqa

RESERVED_WORDS: Set[str]
LEGAL_CHARACTERS: Pattern[str]
LEGAL_CHARACTERS_PLUS_SPACE: Pattern[str]
ILLEGAL_INITIAL_CHARACTERS: str
FK_ON_DELETE: Pattern[str]
FK_ON_UPDATE: Pattern[str]
FK_INITIALLY: Pattern[str]
BIND_PARAMS: Pattern[str]
BIND_PARAMS_ESC: Pattern[str]
BIND_TEMPLATES: Dict[str, str]
BIND_TRANSLATE: Dict[str, Pattern[str]]
OPERATORS: Dict[Any, str]
FUNCTIONS: Dict[Any, str]
EXTRACT_MAP: Dict[str, str]
COMPOUND_KEYWORDS: Dict[langhelpers._symbol, str]
RM_RENDERED_NAME: int
RM_NAME: int
RM_OBJECTS: int
RM_TYPE: int

class ExpandedState(NamedTuple):
    statement: Any
    additional_parameters: Any
    processors: Any
    positiontup: Any
    parameter_expansion: Any

NO_LINTING: langhelpers._symbol
COLLECT_CARTESIAN_PRODUCTS: langhelpers._symbol
WARN_LINTING: langhelpers._symbol
FROM_LINTING: langhelpers._symbol

class FromLinter(NamedTuple):
    froms: Dict[Table, str]
    edges: Set[Tuple[Table, Table]]
    def lint(
        self, start: Optional[Table] = ...
    ) -> Union[Tuple[Set[Table], Table], Tuple[None, None]]: ...
    def warn(self) -> None: ...

class Compiled:
    schema_translate_map: Optional[Dict[Any, Any]] = ...
    execution_options: util.immutabledict[Any, Any] = ...
    compile_state: Optional[CompileState] = ...
    cache_key: Any = ...
    dialect: Any = ...
    preparer: Any = ...
    statement: Optional[ClauseElement] = ...
    can_execute: bool = ...
    string: util.text_type = ...
    def __init__(
        self,
        dialect: Any,
        statement: Optional[Dict[Any, Any]],
        schema_translate_map: Optional[Any] = ...,
        render_schema_translate: bool = ...,
        compile_kwargs: Any = ...,
    ) -> None: ...
    def visit_unsupported_compilation(
        self, element: Any, err: Any
    ) -> _VisitResult: ...
    @property
    def sql_compiler(self) -> Compiled: ...
    def process(self, obj: Any, **kwargs: Any) -> _VisitResult: ...
    def construct_params(
        self,
        params: Optional[Any] = ...,
        extracted_parameters: Optional[Any] = ...,
    ) -> Optional[Dict[str, Any]]: ...
    @property
    def params(self) -> Optional[Dict[str, Any]]: ...

class TypeCompiler(object, metaclass=util.EnsureKWArgType):
    ensure_kwarg: str = ...
    dialect: Any = ...
    def __init__(self, dialect: Any) -> None: ...
    def process(self, type_: TypeEngine[Any], **kw: Any) -> _VisitResult: ...
    def visit_unsupported_compilation(
        self, element: Any, err: Any, **kw: Any
    ) -> _VisitResult: ...

class _CompileLabel(elements.ColumnElement[_TE]):
    __visit_name__: str = ...
    element: elements.ColumnElement[_TE] = ...
    name: Any = ...
    def __init__(
        self, col: elements.ColumnElement[_TE], name: str, alt_names: Any = ...
    ) -> None: ...
    @property
    def proxy_set(self) -> util.column_set[Any]: ...  # type: ignore[override]
    @property
    def type(self) -> _TE: ...  # type: ignore[override]
    def self_group(self: _CL, **kw: Any) -> _CL: ...  # type: ignore[override]

class SQLCompiler(Compiled):
    extract_map: Any = ...
    compound_keywords: Any = ...
    isdelete: bool = ...
    isinsert: bool = ...
    isupdate: bool = ...
    isplaintext: bool = ...
    returning: Any = ...
    returning_precedes_values: bool = ...
    render_table_with_column_in_update_from: bool = ...
    ansi_bind_rules: bool = ...
    insert_single_values_expr: Any = ...
    literal_execute_params: Any = ...
    post_compile_params: Any = ...
    escaped_bind_names: Any = ...
    has_out_parameters: bool = ...
    insert_prefetch: Any = ...
    update_prefetch: Any = ...
    postfetch_lastrowid: bool = ...
    inline: bool = ...
    column_keys: Any = ...
    cache_key: Any = ...
    for_executemany: Any = ...
    linting: Any = ...
    binds: Any = ...
    bind_names: Any = ...
    stack: Any = ...
    positional: Any = ...
    positiontup: Any = ...
    bindtemplate: Any = ...
    ctes: Any = ...
    label_length: Any = ...
    anon_map: Any = ...
    truncated_names: Any = ...
    ctes_recursive: bool = ...
    translate_select_structure: Any = ...
    def __init__(
        self,
        dialect: Any,
        statement: Any,
        cache_key: Optional[Any] = ...,
        column_keys: Optional[Any] = ...,
        for_executemany: bool = ...,
        linting: Any = ...,
        **kwargs: Any,
    ) -> None: ...
    @property
    def current_executable(
        self,
    ) -> Union[
        selectable.Select,
        dml.Insert,
        dml.Update,
        dml.Delete,
        selectable.CompoundSelect,
    ]: ...
    @property
    def prefetch(self) -> List[Any]: ...
    def is_subquery(self) -> bool: ...
    @property
    def sql_compiler(self: _SC) -> _SC: ...
    def construct_params(  # type: ignore[override]
        self,
        params: Optional[Any] = ...,
        _group_number: Optional[Any] = ...,
        _check: bool = ...,
        extracted_parameters: Optional[Any] = ...,
    ) -> Optional[Dict[str, Any]]: ...
    @property
    def params(self) -> Dict[str, Any]: ...
    def default_from(self) -> str: ...
    def visit_grouping(
        self, grouping: Any, asfrom: bool = ..., **kwargs: Any
    ) -> _VisitResult: ...
    def visit_label_reference(
        self, element: Any, within_columns_clause: bool = ..., **kwargs: Any
    ) -> _VisitResult: ...
    def visit_textual_label_reference(
        self, element: Any, within_columns_clause: bool = ..., **kwargs: Any
    ) -> _VisitResult: ...
    def visit_label(
        self,
        label: Any,
        add_to_result_map: Optional[Any] = ...,
        within_label_clause: bool = ...,
        within_columns_clause: bool = ...,
        render_label_as_label: Optional[Any] = ...,
        result_map_targets: Any = ...,
        **kw: Any,
    ) -> _VisitResult: ...
    def visit_lambda_element(
        self, element: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_column(
        self,
        column: Any,
        add_to_result_map: Optional[Any] = ...,
        include_table: bool = ...,
        result_map_targets: Any = ...,
        **kwargs: Any,
    ) -> _VisitResult: ...
    def visit_collation(self, element: Any, **kw: Any) -> _VisitResult: ...
    def visit_fromclause(
        self, fromclause: Any, **kwargs: Any
    ) -> _VisitResult: ...
    def visit_index(self, index: Any, **kwargs: Any) -> _VisitResult: ...
    def visit_typeclause(self, typeclause: Any, **kw: Any) -> _VisitResult: ...
    def post_process_text(self, text: Any) -> _VisitResult: ...
    def escape_literal_column(self, text: Any) -> _VisitResult: ...
    def visit_textclause(
        self,
        textclause: Any,
        add_to_result_map: Optional[Any] = ...,
        **kw: Any,
    ) -> _VisitResult: ...
    def visit_textual_select(
        self,
        taf: Any,
        compound_index: Optional[Any] = ...,
        asfrom: bool = ...,
        **kw: Any,
    ) -> _VisitResult: ...
    def visit_null(self, expr: Any, **kw: Any) -> _VisitResult: ...
    def visit_true(self, expr: Any, **kw: Any) -> _VisitResult: ...
    def visit_false(self, expr: Any, **kw: Any) -> _VisitResult: ...
    def visit_tuple(self, clauselist: Any, **kw: Any) -> _VisitResult: ...
    def visit_clauselist(self, clauselist: Any, **kw: Any) -> _VisitResult: ...
    def visit_case(self, clause: Any, **kwargs: Any) -> _VisitResult: ...
    def visit_type_coerce(
        self, type_coerce: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_cast(self, cast: Any, **kwargs: Any) -> _VisitResult: ...
    def visit_over(self, over: Any, **kwargs: Any) -> _VisitResult: ...
    def visit_withingroup(
        self, withingroup: Any, **kwargs: Any
    ) -> _VisitResult: ...
    def visit_funcfilter(
        self, funcfilter: Any, **kwargs: Any
    ) -> _VisitResult: ...
    def visit_extract(self, extract: Any, **kwargs: Any) -> _VisitResult: ...
    def visit_scalar_function_column(
        self, element: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_function(
        self, func: Any, add_to_result_map: Optional[Any] = ..., **kwargs: Any
    ) -> _VisitResult: ...
    def visit_next_value_func(
        self, next_value: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_sequence(self, sequence: Any, **kw: Any) -> _VisitResult: ...
    def function_argspec(self, func: Any, **kwargs: Any) -> _VisitResult: ...
    def visit_compound_select(
        self,
        cs: Any,
        asfrom: bool = ...,
        compound_index: Optional[Any] = ...,
        **kwargs: Any,
    ) -> _VisitResult: ...
    def visit_unary(self, unary: Any, **kw: Any) -> _VisitResult: ...
    def visit_is_true_unary_operator(
        self, element: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_is_false_unary_operator(
        self, element: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_not_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_empty_set_expr(self, element_types: Any) -> _VisitResult: ...
    def visit_binary(
        self,
        binary: Any,
        override_operator: Optional[Any] = ...,
        eager_grouping: bool = ...,
        from_linter: Optional[Any] = ...,
        lateral_from_linter: Optional[Any] = ...,
        **kw: Any,
    ) -> _VisitResult: ...
    def visit_function_as_comparison_op_binary(
        self, element: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_mod_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_custom_op_binary(
        self, element: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_custom_op_unary_operator(
        self, element: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_custom_op_unary_modifier(
        self, element: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_contains_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_not_contains_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_startswith_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_not_startswith_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_endswith_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_not_endswith_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_like_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_not_like_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_ilike_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_not_ilike_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_between_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_not_between_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_regexp_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_not_regexp_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_regexp_replace_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_bindparam(
        self,
        bindparam: Any,
        within_columns_clause: bool = ...,
        literal_binds: bool = ...,
        skip_bind_expression: bool = ...,
        literal_execute: bool = ...,
        render_postcompile: bool = ...,
        **kwargs: Any,
    ) -> _VisitResult: ...
    def render_literal_bindparam(
        self, bindparam: Any, render_literal_value: Any = ..., **kw: Any
    ) -> _VisitResult: ...
    def render_literal_value(self, value: Any, type_: Any) -> _VisitResult: ...
    def bindparam_string(
        self,
        name: Any,
        positional_names: Optional[Any] = ...,
        post_compile: bool = ...,
        expanding: bool = ...,
        escaped_from: Optional[Any] = ...,
        **kw: Any,
    ) -> _VisitResult: ...
    def visit_cte(
        self,
        cte: Any,
        asfrom: bool = ...,
        ashint: bool = ...,
        fromhints: Optional[Any] = ...,
        visiting_cte: Optional[Any] = ...,
        from_linter: Optional[Any] = ...,
        **kwargs: Any,
    ) -> _VisitResult: ...
    def visit_table_valued_alias(
        self, element: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_table_valued_column(
        self, element: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_alias(
        self,
        alias: Any,
        asfrom: bool = ...,
        ashint: bool = ...,
        iscrud: bool = ...,
        fromhints: Optional[Any] = ...,
        subquery: bool = ...,
        lateral: bool = ...,
        enclosing_alias: Optional[Any] = ...,
        from_linter: Optional[Any] = ...,
        **kwargs: Any,
    ) -> _VisitResult: ...
    def visit_subquery(self, subquery: Any, **kw: Any) -> _VisitResult: ...
    def visit_lateral(self, lateral_: Any, **kw: Any) -> _VisitResult: ...
    def visit_tablesample(
        self, tablesample: Any, asfrom: bool = ..., **kw: Any
    ) -> _VisitResult: ...
    def visit_values(
        self,
        element: Any,
        asfrom: bool = ...,
        from_linter: Optional[Any] = ...,
        **kw: Any,
    ) -> _VisitResult: ...
    def get_render_as_alias_suffix(
        self, alias_name_text: Any
    ) -> _VisitResult: ...
    def format_from_hint_text(
        self, sqltext: Any, table: Any, hint: Any, iscrud: Any
    ) -> _VisitResult: ...
    def get_select_hint_text(self, byfroms: Any) -> Optional[str]: ...
    def get_from_hint_text(self, table: Any, text: Any) -> Optional[str]: ...
    def get_crud_hint_text(self, table: Any, text: Any) -> Optional[str]: ...
    def get_statement_hint_text(self, hint_texts: Any) -> _VisitResult: ...
    def visit_select(
        self,
        select_stmt: Any,
        asfrom: bool = ...,
        fromhints: Optional[Any] = ...,
        compound_index: Optional[Any] = ...,
        select_wraps_for: Optional[Any] = ...,
        lateral: bool = ...,
        from_linter: Optional[Any] = ...,
        **kwargs: Any,
    ) -> _VisitResult: ...
    def get_cte_preamble(self, recursive: Any) -> _VisitResult: ...
    def get_select_precolumns(
        self, select: Any, **kw: Any
    ) -> _VisitResult: ...
    def group_by_clause(self, select: Any, **kw: Any) -> _VisitResult: ...
    def order_by_clause(self, select: Any, **kw: Any) -> _VisitResult: ...
    def for_update_clause(self, select: Any, **kw: Any) -> _VisitResult: ...
    def returning_clause(
        self, stmt: Any, returning_cols: Any
    ) -> _VisitResult: ...
    def limit_clause(self, select: Any, **kw: Any) -> _VisitResult: ...
    def fetch_clause(self, select: Any, **kw: Any) -> _VisitResult: ...
    def visit_table(
        self,
        table: Any,
        asfrom: bool = ...,
        iscrud: bool = ...,
        ashint: bool = ...,
        fromhints: Optional[Any] = ...,
        use_schema: bool = ...,
        from_linter: Optional[Any] = ...,
        **kwargs: Any,
    ) -> _VisitResult: ...
    def visit_join(
        self,
        join: Any,
        asfrom: bool = ...,
        from_linter: Optional[Any] = ...,
        **kwargs: Any,
    ) -> _VisitResult: ...
    def visit_insert(self, insert_stmt: Any, **kw: Any) -> _VisitResult: ...
    def update_limit_clause(self, update_stmt: Any) -> _VisitResult: ...
    def update_tables_clause(
        self, update_stmt: Any, from_table: Any, extra_froms: Any, **kw: Any
    ) -> _VisitResult: ...
    def update_from_clause(
        self,
        update_stmt: Any,
        from_table: Any,
        extra_froms: Any,
        from_hints: Any,
        **kw: Any,
    ) -> _VisitResult: ...
    def visit_update(self, update_stmt: Any, **kw: Any) -> _VisitResult: ...
    def delete_extra_from_clause(
        self,
        update_stmt: Any,
        from_table: Any,
        extra_froms: Any,
        from_hints: Any,
        **kw: Any,
    ) -> _VisitResult: ...
    def delete_table_clause(
        self, delete_stmt: Any, from_table: Any, extra_froms: Any
    ) -> _VisitResult: ...
    def visit_delete(self, delete_stmt: Any, **kw: Any) -> _VisitResult: ...
    def visit_savepoint(self, savepoint_stmt: Any) -> _VisitResult: ...
    def visit_rollback_to_savepoint(
        self, savepoint_stmt: Any
    ) -> _VisitResult: ...
    def visit_release_savepoint(self, savepoint_stmt: Any) -> _VisitResult: ...

class StrSQLCompiler(SQLCompiler):
    def visit_unsupported_compilation(
        self, element: Any, err: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_getitem_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_json_getitem_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_json_path_getitem_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_sequence(self, seq: Any, **kw: Any) -> _VisitResult: ...  # type: ignore[override]
    def returning_clause(
        self, stmt: Any, returning_cols: Any
    ) -> _VisitResult: ...
    def update_from_clause(
        self,
        update_stmt: Any,
        from_table: Any,
        extra_froms: Any,
        from_hints: Any,
        **kw: Any,
    ) -> _VisitResult: ...
    def delete_extra_from_clause(
        self,
        update_stmt: Any,
        from_table: Any,
        extra_froms: Any,
        from_hints: Any,
        **kw: Any,
    ) -> _VisitResult: ...
    def visit_empty_set_expr(self, type_: Any) -> _VisitResult: ...
    def get_from_hint_text(self, table: Any, text: Any) -> _VisitResult: ...
    def visit_regexp_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_not_regexp_match_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_regexp_replace_op_binary(
        self, binary: Any, operator: Any, **kw: Any
    ) -> _VisitResult: ...

class DDLCompiler(Compiled):
    @util.memoized_property
    def type_compiler(self) -> GenericTypeCompiler: ...
    def construct_params(
        self,
        params: Optional[Any] = ...,
        extracted_parameters: Optional[Any] = ...,
    ) -> Optional[Dict[str, Any]]: ...
    def visit_ddl(self, ddl: Any, **kwargs: Any) -> _VisitResult: ...
    def visit_create_schema(self, create: Any, **kw: Any) -> _VisitResult: ...
    def visit_drop_schema(self, drop: Any, **kw: Any) -> _VisitResult: ...
    def visit_create_table(self, create: Any, **kw: Any) -> _VisitResult: ...
    def visit_create_column(
        self, create: Any, first_pk: bool = ..., **kw: Any
    ) -> _VisitResult: ...
    def create_table_constraints(
        self,
        table: Any,
        _include_foreign_key_constraints: Optional[Any] = ...,
        **kw: Any,
    ) -> _VisitResult: ...
    def visit_drop_table(self, drop: Any, **kw: Any) -> _VisitResult: ...
    def visit_drop_view(self, drop: Any, **kw: Any) -> _VisitResult: ...
    def visit_create_index(
        self,
        create: Any,
        include_schema: bool = ...,
        include_table_schema: bool = ...,
        **kw: Any,
    ) -> _VisitResult: ...
    def visit_drop_index(self, drop: Any, **kw: Any) -> _VisitResult: ...
    def visit_add_constraint(self, create: Any, **kw: Any) -> _VisitResult: ...
    def visit_set_table_comment(
        self, create: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_drop_table_comment(
        self, drop: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_set_column_comment(
        self, create: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_drop_column_comment(
        self, drop: Any, **kw: Any
    ) -> _VisitResult: ...
    def get_identity_options(self, identity_options: Any) -> _VisitResult: ...
    def visit_create_sequence(
        self, create: Any, prefix: Optional[Any] = ..., **kw: Any
    ) -> _VisitResult: ...
    def visit_drop_sequence(self, drop: Any, **kw: Any) -> _VisitResult: ...
    def visit_drop_constraint(self, drop: Any, **kw: Any) -> _VisitResult: ...
    def get_column_specification(
        self, column: Any, **kwargs: Any
    ) -> _VisitResult: ...
    def create_table_suffix(self, table: Any) -> _VisitResult: ...
    def post_create_table(self, table: Any) -> _VisitResult: ...
    def get_column_default_string(self, column: Any) -> _VisitResult: ...
    def visit_table_or_column_check_constraint(
        self, constraint: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_check_constraint(
        self, constraint: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_column_check_constraint(
        self, constraint: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_primary_key_constraint(
        self, constraint: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_foreign_key_constraint(
        self, constraint: Any, **kw: Any
    ) -> _VisitResult: ...
    def define_constraint_remote_table(
        self, constraint: Any, table: Any, preparer: Any
    ) -> _VisitResult: ...
    def visit_unique_constraint(
        self, constraint: Any, **kw: Any
    ) -> _VisitResult: ...
    def define_constraint_cascades(self, constraint: Any) -> _VisitResult: ...
    def define_constraint_deferrability(
        self, constraint: Any
    ) -> _VisitResult: ...
    def define_constraint_match(self, constraint: Any) -> _VisitResult: ...
    def visit_computed_column(
        self, generated: Any, **kw: Any
    ) -> _VisitResult: ...
    def visit_identity_column(
        self, identity: Any, **kw: Any
    ) -> _VisitResult: ...

class GenericTypeCompiler(TypeCompiler):
    def visit_FLOAT(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_REAL(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_NUMERIC(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_DECIMAL(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_INTEGER(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_SMALLINT(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_BIGINT(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_TIMESTAMP(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_DATETIME(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_DATE(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_TIME(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_CLOB(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_NCLOB(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_CHAR(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_NCHAR(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_VARCHAR(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_NVARCHAR(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_TEXT(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_BLOB(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_BINARY(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_VARBINARY(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_BOOLEAN(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_large_binary(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_boolean(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_time(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_datetime(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_date(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_big_integer(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_small_integer(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_integer(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_real(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_float(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_numeric(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_string(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_unicode(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_text(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_unicode_text(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_enum(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_null(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_type_decorator(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_user_defined(self, type_: Any, **kw: Any) -> _VisitResult: ...

class StrSQLTypeCompiler(GenericTypeCompiler):
    def process(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def __getattr__(self, key: Any) -> Any: ...
    def visit_null(self, type_: Any, **kw: Any) -> _VisitResult: ...
    def visit_user_defined(self, type_: Any, **kw: Any) -> _VisitResult: ...

class IdentifierPreparer:
    reserved_words: Any = ...
    legal_characters: Any = ...
    illegal_initial_characters: Any = ...
    schema_for_object: Any = ...
    dialect: Any = ...
    initial_quote: Any = ...
    final_quote: Any = ...
    escape_quote: Any = ...
    escape_to_quote: Any = ...
    omit_schema: Any = ...
    quote_case_sensitive_collations: Any = ...
    def __init__(
        self,
        dialect: Any,
        initial_quote: str = ...,
        final_quote: Optional[Any] = ...,
        escape_quote: str = ...,
        quote_case_sensitive_collations: bool = ...,
        omit_schema: bool = ...,
    ) -> None: ...
    def validate_sql_phrase(self, element: _T, reg: Any) -> _T: ...
    def quote_identifier(self, value: Any) -> _VisitResult: ...
    def quote_schema(
        self, schema: Any, force: Optional[Any] = ...
    ) -> _VisitResult: ...
    def quote(
        self, ident: Any, force: Optional[Any] = ...
    ) -> _VisitResult: ...
    def format_collation(self, collation_name: Any) -> _VisitResult: ...
    def format_sequence(
        self, sequence: Any, use_schema: bool = ...
    ) -> _VisitResult: ...
    def format_label(
        self, label: Any, name: Optional[Any] = ...
    ) -> _VisitResult: ...
    def format_alias(
        self, alias: Any, name: Optional[Any] = ...
    ) -> _VisitResult: ...
    def format_savepoint(
        self, savepoint: Any, name: Optional[Any] = ...
    ) -> _VisitResult: ...
    def format_constraint(
        self, constraint: Any, _alembic_quote: bool = ...
    ) -> _VisitResult: ...
    def format_index(self, index: Any) -> _VisitResult: ...
    def format_table(
        self, table: Any, use_schema: bool = ..., name: Optional[Any] = ...
    ) -> _VisitResult: ...
    def format_schema(self, name: Any) -> _VisitResult: ...
    def format_column(
        self,
        column: Any,
        use_table: bool = ...,
        name: Optional[Any] = ...,
        table_name: Optional[Any] = ...,
        use_schema: bool = ...,
    ) -> _VisitResult: ...
    def format_table_seq(
        self, table: Any, use_schema: bool = ...
    ) -> _VisitResult: ...
    def unformat_identifiers(self, identifiers: Any) -> _VisitResult: ...
