from typing import Any
from typing import Callable
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import MutableMapping
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Set
from typing import Type
from typing import TypeVar
from typing import Union

from typing_extensions import Literal

from . import functions
from . import roles
from . import sqltypes
from . import type_api
from . import visitors
from .base import DedupeColumnCollection
from .base import DialectKWArgs
from .base import ImmutableColumnCollection
from .base import SchemaEventTarget
from .elements import ClauseElement
from .elements import ColumnClause
from .elements import ColumnElement
from .elements import TextClause
from .events import DDLEvents
from .selectable import TableClause
from .. import util
from ..engine import Connection
from ..engine import Engine
from ..orm import Mapped
from ..util import langhelpers

RETAIN_SCHEMA: langhelpers._symbol
BLANK_SCHEMA: langhelpers._symbol
NULL_UNSPECIFIED: langhelpers._symbol

_T = TypeVar("_T")

_TE = TypeVar("_TE", bound=type_api.TypeEngine[Any])
_TAB = TypeVar("_TAB", bound=Table)
_CO = TypeVar("_CO", bound=Column[Any])
_FK = TypeVar("_FK", bound=ForeignKey)
_FKC = TypeVar("_FKC", bound=ForeignKeyConstraint)
_CT = TypeVar("_CT", bound=Constraint)
_CCC = TypeVar("_CCC", bound=ColumnCollectionConstraint)
_CC = TypeVar("_CC", bound=CheckConstraint)
_IDX = TypeVar("_IDX", bound=Index)
_CP = TypeVar("_CP", bound=Computed)
_ID = TypeVar("_ID", bound=Identity)

_ServerDefaultType = Union[FetchedValue, str, TextClause, ColumnElement[_T]]

class SchemaItem(SchemaEventTarget, visitors.Visitable):
    __visit_name__: str = ...
    create_drop_stringify_dialect: str = ...
    dispatch: DDLEvents
    @util.memoized_property
    def info(self) -> MutableMapping[Any, Any]: ...

class Table(DialectKWArgs, SchemaItem, TableClause):
    __visit_name__: str = ...
    metadata: MetaData = ...
    schema: Optional[str] = ...
    indexes: Set[Index] = ...
    constraints: Set[Constraint] = ...
    foreign_keys: Set[ForeignKey] = ...
    primary_key: PrimaryKeyConstraint = ...
    fullname: str = ...
    implicit_returning: bool = ...
    comment: Optional[str] = ...
    _prefixes: Sequence[str] = ...
    def __new__(cls: Type[_TAB], *args: Any, **kw: Any) -> _TAB: ...
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    @property
    def foreign_key_constraints(self) -> Set[ForeignKeyConstraint]: ...
    @property
    def key(self) -> util.text_type: ...
    @property
    def bind(self) -> Optional[Union[Engine, Connection]]: ...
    def add_is_dependent_on(self, table: Any) -> None: ...
    def append_column(  # type: ignore[override]
        self, column: Any, replace_existing: bool = ...
    ) -> None: ...
    def append_constraint(self, constraint: Any) -> None: ...
    def exists(
        self, bind: Optional[Union[Engine, Connection]] = ...
    ) -> bool: ...
    def create(
        self,
        bind: Optional[Union[Engine, Connection]] = ...,
        checkfirst: bool = ...,
    ) -> None: ...
    def drop(
        self,
        bind: Optional[Union[Engine, Connection]] = ...,
        checkfirst: bool = ...,
    ) -> None: ...
    def tometadata(
        self,
        metadata: MetaData,
        schema: Optional[Union[langhelpers._symbol, util.text_type]] = ...,
        referred_schema_fn: Optional[
            Callable[
                [Table, util.text_type, ForeignKeyConstraint, util.text_type],
                util.text_type,
            ]
        ] = ...,
        name: Optional[util.text_type] = ...,
    ) -> Table: ...
    def to_metadata(
        self,
        metadata: MetaData,
        schema: Optional[Union[langhelpers._symbol, util.text_type]] = ...,
        referred_schema_fn: Optional[
            Callable[
                [Table, util.text_type, ForeignKeyConstraint, util.text_type],
                util.text_type,
            ]
        ] = ...,
        name: Optional[util.text_type] = ...,
    ) -> Table: ...
    @util.memoized_property
    def columns(self) -> ImmutableColumnCollection[Column[Any]]: ...
    @util.memoized_property
    def c(self) -> ImmutableColumnCollection[Column[Any]]: ...
    @property
    def _autoincrement_column(self) -> Optional[Column[Any]]: ...
    @_autoincrement_column.setter
    def _autoincrement_column(self, value: Optional[Column[Any]]) -> None: ...

class Column(DialectKWArgs, SchemaItem, ColumnClause[_TE]):
    __visit_name__: str = ...
    name: str = ...
    inherit_cache: bool = ...
    key: Optional[str] = ...
    primary_key: bool = ...
    nullable: bool = ...
    default: Optional[Any] = ...
    server_default: Optional[_ServerDefaultType[_TE]] = ...
    server_onupdate: Optional[FetchedValue] = ...
    index: Optional[bool] = ...
    unique: Optional[bool] = ...
    system: bool = ...
    doc: Optional[str] = ...
    onupdate: Optional[Any] = ...
    autoincrement: Union[bool, Literal["auto", "ignore_fk"]] = ...
    constraints: Set[Constraint] = ...
    foreign_keys: Set[ForeignKey] = ...
    comment: Optional[str] = ...
    computed: Optional[Computed] = ...
    identity: Optional[Identity] = ...
    @overload
    def __init__(
        self: Column[sqltypes.NullType],
        __name: str,
        *args: SchemaEventTarget,
        autoincrement: Union[bool, Literal["auto", "ignore_fk"]] = ...,
        default: Optional[Any] = ...,
        doc: Optional[str] = ...,
        key: Optional[str] = ...,
        index: Optional[bool] = ...,
        info: MutableMapping[Any, Any] = ...,
        nullable: bool = ...,
        onupdate: Optional[Any] = ...,
        primary_key: bool = ...,
        server_default: Optional[_ServerDefaultType[Any]] = ...,
        server_onupdate: Optional[FetchedValue] = ...,
        quote: Optional[bool] = ...,
        unique: Optional[bool] = ...,
        system: bool = ...,
        comment: Optional[str] = ...,
        **kwargs: Any,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[sqltypes.NullType],
        *args: SchemaEventTarget,
        autoincrement: Union[bool, Literal["auto", "ignore_fk"]] = ...,
        default: Optional[Any] = ...,
        doc: Optional[str] = ...,
        key: Optional[str] = ...,
        index: Optional[bool] = ...,
        info: MutableMapping[Any, Any] = ...,
        nullable: bool = ...,
        onupdate: Optional[Any] = ...,
        primary_key: bool = ...,
        server_default: Optional[_ServerDefaultType[Any]] = ...,
        server_onupdate: Optional[FetchedValue] = ...,
        quote: Optional[bool] = ...,
        unique: Optional[bool] = ...,
        system: bool = ...,
        comment: Optional[str] = ...,
        **kwargs: Any,
    ) -> None: ...
    @overload
    def __init__(
        self,
        __name: str,
        __type: Union[_TE, Type[_TE]],
        *args: SchemaEventTarget,
        autoincrement: Union[bool, Literal["auto", "ignore_fk"]] = ...,
        default: Optional[Any] = ...,
        doc: Optional[str] = ...,
        key: Optional[str] = ...,
        index: Optional[bool] = ...,
        info: MutableMapping[Any, Any] = ...,
        nullable: bool = ...,
        onupdate: Optional[Any] = ...,
        primary_key: bool = ...,
        server_default: Optional[_ServerDefaultType[_TE]] = ...,
        server_onupdate: Optional[FetchedValue] = ...,
        quote: Optional[bool] = ...,
        unique: Optional[bool] = ...,
        system: bool = ...,
        comment: Optional[str] = ...,
        **kwargs: Any,
    ) -> None: ...
    @overload
    def __init__(
        self,
        __type: Union[_TE, Type[_TE]],
        *args: SchemaEventTarget,
        autoincrement: Union[bool, Literal["auto", "ignore_fk"]] = ...,
        default: Optional[Any] = ...,
        doc: Optional[str] = ...,
        key: Optional[str] = ...,
        index: Optional[bool] = ...,
        info: MutableMapping[Any, Any] = ...,
        nullable: bool = ...,
        onupdate: Optional[Any] = ...,
        primary_key: bool = ...,
        server_default: Optional[_ServerDefaultType[_TE]] = ...,
        server_onupdate: Optional[FetchedValue] = ...,
        quote: Optional[bool] = ...,
        unique: Optional[bool] = ...,
        system: bool = ...,
        comment: Optional[str] = ...,
        **kwargs: Any,
    ) -> None: ...
    def references(self, column: Column[Any]) -> bool: ...
    def append_foreign_key(self, fk: ForeignKey) -> None: ...
    def copy(self: _CO, **kw: Any) -> _CO: ...
    # NOTE: his doesn't exist at runtime, it's used when not using the plugin
    # makes the inferred type of orm class attrs Mapped, Any for instance ones
    @overload
    def __get__(self, instance: None, owner: Any) -> Mapped: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> Any: ...

class ForeignKey(DialectKWArgs, SchemaItem):
    __visit_name__: str = ...
    constraint: Optional[ForeignKeyConstraint] = ...
    parent: Optional[Column[Any]] = ...
    use_alter: bool = ...
    name: Optional[str] = ...
    onupdate: Optional[str] = ...
    ondelete: Optional[str] = ...
    deferrable: Optional[bool] = ...
    initially: Optional[str] = ...
    link_to_name: bool = ...
    match: Optional[str] = ...
    def __init__(
        self,
        column: Union[Column[Any], str],
        _constraint: Optional[ForeignKeyConstraint] = ...,
        use_alter: bool = ...,
        name: Optional[str] = ...,
        onupdate: Optional[str] = ...,
        ondelete: Optional[str] = ...,
        deferrable: Optional[bool] = ...,
        initially: Optional[str] = ...,
        link_to_name: bool = ...,
        match: Optional[str] = ...,
        info: Optional[MutableMapping[Any, Any]] = ...,
        **dialect_kw: Any,
    ) -> None: ...
    def copy(self: _FK, schema: Optional[str] = ...) -> _FK: ...
    @property
    def target_fullname(self) -> str: ...
    def references(self, table: Table) -> bool: ...
    def get_referent(self, table: Table) -> Column[Any]: ...
    @util.memoized_property
    def column(self) -> Column[Any]: ...

class DefaultGenerator(SchemaItem):
    __visit_name__: str = ...
    is_sequence: bool = ...
    is_server_default: bool = ...
    column: Optional[Column[Any]] = ...
    for_update: bool = ...
    def __init__(self, for_update: bool = ...) -> None: ...
    def execute(
        self, bind: Optional[Union[Engine, Connection]] = ...
    ) -> Any: ...
    @property
    def bind(self) -> Optional[Union[Engine, Connection]]: ...

class ColumnDefault(DefaultGenerator):
    arg: Any = ...
    def __init__(self, arg: Any, **kwargs: Any) -> None: ...
    @util.memoized_property
    def is_callable(self) -> bool: ...
    @util.memoized_property
    def is_clause_element(self) -> bool: ...
    @util.memoized_property
    def is_scalar(self) -> bool: ...

class IdentityOptions:
    start: Optional[int] = ...
    increment: Optional[int] = ...
    minvalue: Optional[int] = ...
    maxvalue: Optional[int] = ...
    nominvalue: Optional[bool] = ...
    nomaxvalue: Optional[bool] = ...
    cycle: Optional[bool] = ...
    cache: Optional[int] = ...
    order: Optional[bool] = ...
    def __init__(
        self,
        start: Optional[int] = ...,
        increment: Optional[int] = ...,
        minvalue: Optional[int] = ...,
        maxvalue: Optional[int] = ...,
        nominvalue: Optional[bool] = ...,
        nomaxvalue: Optional[bool] = ...,
        cycle: Optional[bool] = ...,
        cache: Optional[int] = ...,
        order: Optional[bool] = ...,
    ) -> None: ...

class Sequence(
    IdentityOptions,
    roles.StatementRole,
    DefaultGenerator,
    Generic[_TE],
):
    __visit_name__: str = ...
    is_sequence: bool = ...
    name: str = ...
    optional: bool = ...
    schema: Optional[Union[str, langhelpers._symbol]] = ...
    metadata: Optional[MetaData] = ...
    data_type: Optional[_TE] = ...
    @overload
    def __init__(
        self: Sequence[sqltypes.Integer],
        name: str,
        start: Optional[int] = ...,
        increment: Optional[int] = ...,
        minvalue: Optional[int] = ...,
        maxvalue: Optional[int] = ...,
        nominvalue: Optional[bool] = ...,
        nomaxvalue: Optional[bool] = ...,
        cycle: Optional[bool] = ...,
        schema: Optional[str] = ...,
        cache: Optional[int] = ...,
        order: Optional[bool] = ...,
        data_type: None = ...,
        optional: bool = ...,
        quote: Optional[bool] = ...,
        metadata: Optional[MetaData] = ...,
        quote_schema: Optional[bool] = ...,
        for_update: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        start: int,
        increment: Optional[int],
        minvalue: Optional[int],
        maxvalue: Optional[int],
        nominvalue: Optional[bool],
        nomaxvalue: Optional[bool],
        cycle: Optional[bool],
        schema: Optional[str],
        cache: Optional[int],
        order: Optional[bool],
        data_type: Union[_TE, Type[_TE]],
        optional: bool = ...,
        quote: Optional[bool] = ...,
        metadata: Optional[MetaData] = ...,
        quote_schema: Optional[bool] = ...,
        for_update: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        *,
        start: Optional[int] = ...,
        increment: Optional[int] = ...,
        minvalue: Optional[int] = ...,
        maxvalue: Optional[int] = ...,
        nominvalue: Optional[bool] = ...,
        nomaxvalue: Optional[bool] = ...,
        cycle: Optional[bool] = ...,
        schema: Optional[str] = ...,
        cache: Optional[int] = ...,
        order: Optional[bool] = ...,
        data_type: Union[_TE, Type[_TE]],
        optional: bool = ...,
        quote: Optional[bool] = ...,
        metadata: Optional[MetaData] = ...,
        quote_schema: Optional[bool] = ...,
        for_update: bool = ...,
    ) -> None: ...
    @util.memoized_property
    def is_callable(self) -> bool: ...
    @util.memoized_property
    def is_clause_element(self) -> bool: ...
    def next_value(self) -> functions.next_value[_TE]: ...
    @property
    def bind(self) -> Optional[Union[Engine, Connection]]: ...
    def create(
        self,
        bind: Optional[Union[Engine, Connection]] = ...,
        checkfirst: bool = ...,
    ) -> None: ...
    def drop(
        self,
        bind: Optional[Union[Engine, Connection]] = ...,
        checkfirst: bool = ...,
    ) -> None: ...

class FetchedValue(SchemaEventTarget):
    is_server_default: bool = ...
    reflected: bool = ...
    has_argument: bool = ...
    is_clause_element: bool = ...
    for_update: bool = ...
    def __init__(self, for_update: bool = ...) -> None: ...

class DefaultClause(FetchedValue):
    has_argument: bool = ...
    arg: Any = ...
    reflected: bool = ...
    def __init__(
        self, arg: Any, for_update: bool = ..., _reflected: bool = ...
    ) -> None: ...

class Constraint(DialectKWArgs, SchemaItem):
    __visit_name__: str = ...
    name: Optional[str] = ...
    deferrable: Optional[bool] = ...
    initially: Optional[str] = ...
    parent: Optional[Table] = ...
    def __init__(
        self,
        name: Optional[str] = ...,
        deferrable: Optional[bool] = ...,
        initially: Optional[str] = ...,
        _create_rule: Optional[Any] = ...,
        info: Optional[MutableMapping[Any, Any]] = ...,
        _type_bound: bool = ...,
        **dialect_kw: Any,
    ) -> None: ...
    @property
    def table(self) -> Table: ...
    def copy(self: _CT, **kw: Any) -> _CT: ...

class ColumnCollectionMixin:
    columns: DedupeColumnCollection[Column[Any]] = ...
    def __init__(
        self, *columns: Union[str, Column[Any]], **kw: Any
    ) -> None: ...

class ColumnCollectionConstraint(ColumnCollectionMixin, Constraint):
    def __init__(
        self, *columns: Union[str, Column[Any]], **kw: Any
    ) -> None: ...
    def __contains__(self, x: Any) -> bool: ...
    def copy(
        self: _CCC, target_table: Optional[Table] = ..., **kw: Any
    ) -> _CCC: ...
    def contains_column(self, col: Column[Any]) -> bool: ...
    def __iter__(self) -> Iterator[Column[Any]]: ...
    def __len__(self) -> int: ...

class CheckConstraint(ColumnCollectionConstraint):
    __visit_name__: str = ...
    sqltext: ClauseElement = ...
    def __init__(
        self,
        sqltext: Union[str, ClauseElement],
        name: Optional[str] = ...,
        deferrable: Optional[bool] = ...,
        initially: Optional[str] = ...,
        table: Optional[Table] = ...,
        info: Optional[MutableMapping[Any, Any]] = ...,
        _create_rule: Optional[Any] = ...,
        _autoattach: bool = ...,
        _type_bound: bool = ...,
        **kw: Any,
    ) -> None: ...
    @property
    def is_column_level(self) -> bool: ...
    def copy(
        self: _CC, target_table: Optional[Table] = ..., **kw: Any
    ) -> _CC: ...

class ForeignKeyConstraint(ColumnCollectionConstraint):
    __visit_name__: str = ...
    onupdate: Optional[str] = ...
    ondelete: Optional[str] = ...
    link_to_name: bool = ...
    use_alter: bool = ...
    match: Optional[str] = ...
    elements: List[ForeignKey] = ...
    def __init__(
        self,
        columns: Iterable[Union[str, Column[Any]]],
        refcolumns: Iterable[Union[str, Column[Any]]],
        name: Optional[str] = ...,
        onupdate: Optional[str] = ...,
        ondelete: Optional[str] = ...,
        deferrable: Optional[bool] = ...,
        initially: Optional[str] = ...,
        use_alter: bool = ...,
        link_to_name: bool = ...,
        match: Optional[str] = ...,
        table: Optional[Table] = ...,
        info: Optional[MutableMapping[Any, Any]] = ...,
        **dialect_kw: Any,
    ) -> None: ...
    @property
    def referred_table(self) -> Table: ...
    @property
    def column_keys(self) -> List[str]: ...
    def copy(  # type: ignore[override]
        self: _FKC,
        schema: Optional[str] = ...,
        target_table: Optional[Table] = ...,
        **kw: Any,
    ) -> _FKC: ...

class PrimaryKeyConstraint(ColumnCollectionConstraint):
    __visit_name__: str = ...
    def __init__(
        self, *columns: Union[str, Column[Any]], **kw: Any
    ) -> None: ...
    @property
    def columns_autoinc_first(self) -> List[Column[Any]]: ...

class UniqueConstraint(ColumnCollectionConstraint):
    __visit_name__: str = ...

class Index(DialectKWArgs, ColumnCollectionMixin, SchemaItem):
    __visit_name__: str = ...
    table: Optional[Table] = ...
    name: str = ...
    unique: bool = ...
    expressions: List[Column[Any]] = ...
    def __init__(
        self,
        name: str,
        *expressions: Union[str, roles.DDLConstraintColumnRole],
        **kw: Any,
    ) -> None: ...
    @property
    def bind(self) -> Optional[Union[Engine, Connection]]: ...
    def create(
        self: _IDX,
        bind: Optional[Union[Engine, Connection]] = ...,
        checkfirst: bool = ...,
    ) -> _IDX: ...
    def drop(
        self,
        bind: Optional[Union[Engine, Connection]] = ...,
        checkfirst: bool = ...,
    ) -> None: ...

DEFAULT_NAMING_CONVENTION: util.immutabledict[str, str]

class MetaData(SchemaItem):
    __visit_name__: str = ...
    tables: util.FacadeDict[str, Table] = ...
    schema: Optional[str] = ...
    naming_convention: Dict[Any, Any] = ...
    bind: Optional[Union[Engine, Connection]] = ...
    def __init__(
        self,
        bind: Optional[Union[Engine, Connection]] = ...,
        schema: Optional[str] = ...,
        quote_schema: Optional[bool] = ...,
        naming_convention: Optional[Dict[str, str]] = ...,
        info: Optional[MutableMapping[Any, Any]] = ...,
    ) -> None: ...
    def __contains__(self, table_or_key: Any) -> bool: ...
    def is_bound(self) -> bool: ...
    def clear(self) -> None: ...
    def remove(self, table: Table) -> None: ...
    @property
    def sorted_tables(self) -> List[Table]: ...
    def reflect(
        self,
        bind: Optional[Union[Engine, Connection]] = ...,
        schema: Optional[Any] = ...,
        views: bool = ...,
        only: Optional[Any] = ...,
        extend_existing: bool = ...,
        autoload_replace: bool = ...,
        resolve_fks: bool = ...,
        **dialect_kwargs: Any,
    ) -> None: ...
    def create_all(
        self,
        bind: Optional[Union[Engine, Connection]] = ...,
        tables: Optional[List[Table]] = ...,
        checkfirst: bool = ...,
    ) -> None: ...
    def drop_all(
        self,
        bind: Optional[Union[Engine, Connection]] = ...,
        tables: Optional[List[Table]] = ...,
        checkfirst: bool = ...,
    ) -> None: ...

class ThreadLocalMetaData(MetaData):
    __visit_name__: str = ...
    context: util.threading.local = ...
    bind: Optional[Union[Engine, Connection]] = ...
    def __init__(self) -> None: ...
    def is_bound(self) -> bool: ...
    def dispose(self) -> None: ...

class Computed(FetchedValue, SchemaItem):
    __visit_name__: str = ...
    sqltext: ClauseElement = ...
    persisted: Optional[bool] = ...
    column: Optional[Column[Any]] = ...
    def __init__(
        self,
        sqltext: Union[str, ClauseElement],
        persisted: Optional[bool] = ...,
    ) -> None: ...
    def copy(
        self: _CP, target_table: Optional[Table] = ..., **kw: Any
    ) -> _CP: ...

class Identity(IdentityOptions, FetchedValue, SchemaItem):
    __visit_name__: str = ...
    always: bool = ...
    on_null: Optional[bool] = ...
    column: Optional[Column[Any]] = ...
    def __init__(
        self,
        always: bool = ...,
        on_null: Optional[bool] = ...,
        start: Optional[int] = ...,
        increment: Optional[int] = ...,
        minvalue: Optional[int] = ...,
        maxvalue: Optional[int] = ...,
        nominvalue: Optional[bool] = ...,
        nomaxvalue: Optional[bool] = ...,
        cycle: Optional[bool] = ...,
        cache: Optional[int] = ...,
        order: Optional[bool] = ...,
    ) -> None: ...
    def copy(self: _ID, **kw: Any) -> _ID: ...

def _get_table_key(name: str, schema: Optional[str]) -> str: ...
