from typing import AbstractSet
from typing import Any
from typing import Callable
from typing import Literal
from typing import Mapping
from typing import MutableMapping
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from sqlalchemy.sql.elements import ColumnElement
from .attributes import Mapped as Mapped
from .relationships import _OrderByArgument
from ..sql import schema
from ..sql import sqltypes
from ..sql.schema import _ServerDefaultType
from ..sql.schema import FetchedValue
from ..sql.schema import SchemaEventTarget

_T = TypeVar("_T")

_BackrefResult = Tuple[str, Mapping[str, Any]]

class MappedColumn(Mapped[_T]):
    def __init__(self, expr: _T) -> None: ...
    def operate(self, op: Any, *other: Any, **kwargs: Any): ...
    def reverse_operate(self, op: Any, other: Any, **kwargs: Any): ...

@overload
def column(
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
) -> Mapped[Any]: ...
@overload
def column(
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
) -> Mapped[Any]: ...
@overload
def column(
    __name: str,
    _type: Union[sqltypes.TypeEngine[_T], Type[sqltypes.TypeEngine[_T]]],
    *args: SchemaEventTarget,
    autoincrement: Union[bool, Literal["auto", "ignore_fk"]] = ...,
    default: Optional[Any] = ...,
    doc: Optional[str] = ...,
    key: Optional[str] = ...,
    index: Optional[bool] = ...,
    info: MutableMapping[Any, Any] = ...,
    nullable: Literal[False],
    onupdate: Optional[Any] = ...,
    primary_key: bool = ...,
    server_default: Optional[_ServerDefaultType[schema._TE]] = ...,
    server_onupdate: Optional[FetchedValue] = ...,
    quote: Optional[bool] = ...,
    unique: Optional[bool] = ...,
    system: bool = ...,
    comment: Optional[str] = ...,
    **kwargs: Any,
) -> Mapped[_T]: ...
@overload
def column(
    _type: Union[sqltypes.TypeEngine[_T], Type[sqltypes.TypeEngine[_T]]],
    *args: SchemaEventTarget,
    autoincrement: Union[bool, Literal["auto", "ignore_fk"]] = ...,
    default: Optional[Any] = ...,
    doc: Optional[str] = ...,
    key: Optional[str] = ...,
    index: Optional[bool] = ...,
    info: MutableMapping[Any, Any] = ...,
    nullable: Literal[False],
    onupdate: Optional[Any] = ...,
    primary_key: bool = ...,
    server_default: Optional[_ServerDefaultType[schema._TE]] = ...,
    server_onupdate: Optional[FetchedValue] = ...,
    quote: Optional[bool] = ...,
    unique: Optional[bool] = ...,
    system: bool = ...,
    comment: Optional[str] = ...,
    **kwargs: Any,
) -> Mapped[_T]: ...
@overload
def column(
    __name: str,
    _type: Union[sqltypes.TypeEngine[_T], Type[sqltypes.TypeEngine[_T]]],
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
    server_default: Optional[_ServerDefaultType[schema._TE]] = ...,
    server_onupdate: Optional[FetchedValue] = ...,
    quote: Optional[bool] = ...,
    unique: Optional[bool] = ...,
    system: bool = ...,
    comment: Optional[str] = ...,
    **kwargs: Any,
) -> Mapped[Optional[_T]]: ...
@overload
def column(
    _type: Union[sqltypes.TypeEngine[_T], Type[sqltypes.TypeEngine[_T]]],
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
    server_default: Optional[_ServerDefaultType[schema._TE]] = ...,
    server_onupdate: Optional[FetchedValue] = ...,
    quote: Optional[bool] = ...,
    unique: Optional[bool] = ...,
    system: bool = ...,
    comment: Optional[str] = ...,
    **kwargs: Any,
) -> Mapped[Optional[_T]]: ...
def column_property(
    expr: ColumnElement[sqltypes.TypeEngine[_T]],
    *addl: ColumnElement[Any],
    **kw: Any,
) -> Mapped[_T]: ...
def composite(cls: _T, *arg: Any, **kw: Any) -> Mapped[_T]: ...
def deferred(
    expr: ColumnElement[sqltypes.TypeEngine[_T]],
    *addl: ColumnElement[Any],
    **kw: Any,
) -> Mapped[_T]: ...
def query_expression(
    typ: sqltypes.TypeEngine[_T], default_expr: Any = ...
) -> Mapped[_T]: ...
def synonym(*arg, **kw) -> Any: ...
def related(
    entity: Optional[_T] = ...,
    secondary: Optional[Any] = ...,
    primaryjoin: Optional[Any] = ...,
    secondaryjoin: Optional[Any] = ...,
    foreign_keys: Optional[Any] = ...,
    uselist: Optional[bool] = ...,
    order_by: _OrderByArgument = ...,
    backref: Union[str, _BackrefResult] = ...,
    back_populates: str = ...,
    overlaps: Union[AbstractSet[str], str] = ...,
    post_update: bool = ...,
    cascade: Union[Literal[False], Sequence[str]] = ...,
    viewonly: bool = ...,
    lazy: str = ...,
    collection_class: Optional[Union[Type[Any], Callable[[], Any]]] = ...,
    passive_deletes: Union[bool, Literal["all"]] = ...,
    passive_updates: bool = ...,
    remote_side: Optional[Any] = ...,
    enable_typechecks: bool = ...,  # NOTE: not documented
    join_depth: Optional[int] = ...,
    comparator_factory: Optional[Any] = ...,
    single_parent: bool = ...,
    innerjoin: Union[bool, str] = ...,
    distinct_target_key: Optional[bool] = ...,
    doc: Optional[str] = ...,
    active_history: bool = ...,
    cascade_backrefs: bool = ...,
    load_on_pending: bool = ...,
    bake_queries: bool = ...,
    _local_remote_pairs: Optional[Any] = ...,
    query_class: Optional[Any] = ...,
    info: Optional[MutableMapping[Any, Any]] = ...,
    omit_join: Optional[Literal[False]] = ...,
    sync_backref: Optional[Any] = ...,
) -> Mapped[_T]: ...
def declared_attr(
    fget: Callable[[Any], Mapped[_T]], cascading: bool = ...
) -> Mapped[_T]: ...
