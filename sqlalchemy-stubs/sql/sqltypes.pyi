from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
from decimal import Decimal
from enum import Enum as _Enum
from typing import Any
from typing import ClassVar
from typing import Dict
from typing import Generic
from typing import List
from typing import Mapping
from typing import Optional
from typing import overload
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from typing_extensions import Literal

from .base import SchemaEventTarget
from .elements import BinaryExpression
from .traversals import HasCacheKey
from .type_api import _BindProcessor
from .type_api import _LiteralProcessor
from .type_api import _ResultProcessor
from .type_api import Emulated
from .type_api import TypeDecorator
from .type_api import TypeEngine
from .. import util
from ..engine import Connection
from ..engine import Engine
from ..util import langhelpers

_T = TypeVar("_T")
_TE = TypeVar("_TE", bound=TypeEngine[Any])
_ST = TypeVar("_ST", bound=SchemaType)
_EN = TypeVar("_EN", bound=Enum)

_NumericType = Union[float, Decimal]
_JSONType = Union[str, Mapping[Any, Any], List[Any]]

class _LookupExpressionAdapter(Generic[_T]):
    class Comparator(TypeEngine.Comparator[_TE]): ...
    comparator_factory: Type[Comparator[TypeEngine[_T]]] = ...

class Concatenable(Generic[_T]):
    class Comparator(TypeEngine.Comparator[_TE]): ...
    comparator_factory: Type[Comparator[TypeEngine[_T]]] = ...

class Indexable(Generic[_T]):
    class Comparator(TypeEngine.Comparator[_TE]):
        def __getitem__(self, index: Any) -> Any: ...
    comparator_factory: Type[Comparator[TypeEngine[_T]]] = ...

class String(Concatenable[str], TypeEngine[str]):  # type: ignore[misc]
    __visit_name__: str = ...
    RETURNS_UNICODE: ClassVar[langhelpers._symbol] = ...
    RETURNS_BYTES: ClassVar[langhelpers._symbol] = ...
    RETURNS_CONDITIONAL: ClassVar[langhelpers._symbol] = ...
    RETURNS_UNKNOWN: ClassVar[langhelpers._symbol] = ...
    length: Optional[int] = ...
    collation: Optional[str] = ...
    @overload
    def __init__(
        self,
        length: Optional[int] = ...,
        collation: Optional[str] = ...,
        convert_unicode: bool = ...,
        _warn_on_bytestring: bool = ...,
        _expect_unicode: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        length: Optional[int],
        collation: Optional[str],
        convert_unicode: Literal["force"],
        unicode_error: str,
        _warn_on_bytestring: bool = ...,
        _expect_unicode: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        length: Optional[int],
        *,
        convert_unicode: Literal["force"],
        unicode_error: str,
        _warn_on_bytestring: bool = ...,
        _expect_unicode: bool = ...,
    ) -> None: ...
    def literal_processor(self, dialect: Any) -> _LiteralProcessor[str]: ...
    def bind_processor(
        self, dialect: Any
    ) -> Optional[_BindProcessor[str]]: ...
    def result_processor(
        self, dialect: Any, coltype: Any
    ) -> Optional[_ResultProcessor[str]]: ...
    @property
    def python_type(self) -> Union[Type[str], Type[util.text_type]]: ...
    def get_dbapi_type(self, dbapi: Any) -> Any: ...

class Text(String):
    __visit_name__: str = ...

class Unicode(String):
    __visit_name__: str = ...
    def __init__(self, length: Optional[Any] = ..., **kwargs: Any) -> None: ...

class UnicodeText(Text):
    __visit_name__: str = ...
    def __init__(self, length: Optional[Any] = ..., **kwargs: Any) -> None: ...

class Integer(_LookupExpressionAdapter[int], TypeEngine[int]):  # type: ignore[misc]
    __visit_name__: str = ...
    def get_dbapi_type(self, dbapi: Any) -> Any: ...
    @property
    def python_type(self) -> Type[int]: ...
    def literal_processor(self, dialect: Any) -> _LiteralProcessor[int]: ...

class SmallInteger(Integer):
    __visit_name__: str = ...

class BigInteger(Integer):
    __visit_name__: str = ...

class Numeric(  # type: ignore[misc]
    _LookupExpressionAdapter[_NumericType], TypeEngine[_NumericType]
):
    __visit_name__: str = ...
    precision: Any = ...
    scale: Any = ...
    decimal_return_scale: Any = ...
    asdecimal: Any = ...
    def __init__(
        self,
        precision: Optional[Any] = ...,
        scale: Optional[Any] = ...,
        decimal_return_scale: Optional[Any] = ...,
        asdecimal: bool = ...,
    ) -> None: ...
    def get_dbapi_type(self, dbapi: Any) -> Any: ...
    def literal_processor(
        self, dialect: Any
    ) -> _LiteralProcessor[_NumericType]: ...
    @property
    def python_type(self) -> Union[Type[float], Type[Decimal]]: ...
    def bind_processor(
        self, dialect: Any
    ) -> Optional[_BindProcessor[_NumericType]]: ...
    def result_processor(
        self, dialect: Any, coltype: Any
    ) -> Optional[_ResultProcessor[_NumericType]]: ...

class Float(Numeric):
    __visit_name__: str = ...
    scale: Any = ...
    precision: Any = ...
    asdecimal: Any = ...
    decimal_return_scale: Any = ...
    def __init__(
        self,
        precision: Optional[Any] = ...,
        asdecimal: bool = ...,
        decimal_return_scale: Optional[Any] = ...,
    ) -> None: ...
    def result_processor(
        self, dialect: Any, coltype: Any
    ) -> Optional[_ResultProcessor[_NumericType]]: ...

class DateTime(_LookupExpressionAdapter[datetime], TypeEngine[datetime]):  # type: ignore[misc]
    __visit_name__: str = ...
    timezone: Any = ...
    def __init__(self, timezone: bool = ...) -> None: ...
    def get_dbapi_type(self, dbapi: Any) -> Any: ...
    @property
    def python_type(self) -> Type[datetime]: ...

class Date(_LookupExpressionAdapter[date], TypeEngine[date]):  # type: ignore[misc]
    __visit_name__: str = ...
    def get_dbapi_type(self, dbapi: Any) -> Any: ...
    @property
    def python_type(self) -> Type[date]: ...

class Time(_LookupExpressionAdapter[time], TypeEngine[time]):  # type: ignore[misc]
    __visit_name__: str = ...
    timezone: Any = ...
    def __init__(self, timezone: bool = ...) -> None: ...
    def get_dbapi_type(self, dbapi: Any) -> Any: ...
    @property
    def python_type(self) -> Type[time]: ...

class _Binary(TypeEngine[util.binary_type]):
    length: Any = ...
    def __init__(self, length: Optional[Any] = ...) -> None: ...
    def literal_processor(
        self, dialect: Any
    ) -> _LiteralProcessor[util.binary_type]: ...
    @property
    def python_type(self) -> Type[util.binary_type]: ...
    def bind_processor(
        self, dialect: Any
    ) -> Optional[_BindProcessor[util.binary_type]]: ...
    def result_processor(
        self, dialect: Any, coltype: Any
    ) -> _ResultProcessor[util.binary_type]: ...
    def coerce_compared_value(
        self, op: Any, value: Any
    ) -> TypeEngine[Any]: ...
    def get_dbapi_type(self, dbapi: Any) -> Any: ...

class LargeBinary(_Binary):
    __visit_name__: str = ...
    def __init__(self, length: Optional[Any] = ...) -> None: ...

class SchemaType(SchemaEventTarget):
    name: Any = ...
    schema: Any = ...
    metadata: Any = ...
    inherit_schema: Any = ...
    def __init__(
        self,
        name: Optional[Any] = ...,
        schema: Optional[Any] = ...,
        metadata: Optional[Any] = ...,
        inherit_schema: bool = ...,
        quote: Optional[Any] = ...,
        _create_events: bool = ...,
    ) -> None: ...
    def copy(self: _ST, **kw: Any) -> _ST: ...
    def adapt(self, __impltype: Type[_T], **kw: Any) -> _T: ...
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

class Enum(Emulated, String, SchemaType):
    __visit_name__: str = ...
    def __init__(self, *enums: Any, **kw: Any) -> None: ...
    @property
    def sort_key_function(self) -> util._SortKeyFunction: ...  # type: ignore[override]
    @property
    def native(self) -> Any: ...
    class Comparator(String.Comparator["Enum"]): ...
    comparator_factory: Type[Comparator] = ...  # type: ignore[assignment]
    def as_generic(self: _EN, allow_nulltype: bool = ...) -> _EN: ...
    def adapt_to_emulated(self, impltype: Type[_T], **kw: Any) -> _T: ...
    def adapt(self, __impltype: Type[_T], **kw: Any) -> _T: ...
    def literal_processor(self, dialect: Any) -> _LiteralProcessor[str]: ...
    def bind_processor(self, dialect: Any) -> _BindProcessor[str]: ...
    def result_processor(
        self, dialect: Any, coltype: Any
    ) -> _ResultProcessor[str]: ...
    def copy(self: _EN, **kw: Any) -> _EN: ...
    @property
    def python_type(self) -> Union[Type[_Enum], Type[str], Type[util.text_type]]: ...  # type: ignore[override]

class PickleType(TypeDecorator[Any]):
    impl: Any = ...
    protocol: Any = ...
    pickler: Any = ...
    comparator: Any = ...
    def __init__(
        self,
        protocol: Any = ...,
        pickler: Optional[Any] = ...,
        comparator: Optional[Any] = ...,
    ) -> None: ...
    def __reduce__(self) -> Any: ...
    def bind_processor(self, dialect: Any) -> _BindProcessor[Any]: ...
    def result_processor(
        self, dialect: Any, coltype: Any
    ) -> _ResultProcessor[Any]: ...
    def compare_values(self, x: Any, y: Any) -> bool: ...

class Boolean(Emulated, TypeEngine[bool], SchemaType):  # type: ignore[misc]
    __visit_name__: str = ...
    native: bool = ...
    create_constraint: Any = ...
    name: Any = ...
    def __init__(
        self,
        create_constraint: bool = ...,
        name: Optional[Any] = ...,
        _create_events: bool = ...,
    ) -> None: ...
    @property
    def python_type(self) -> Type[bool]: ...
    def literal_processor(self, dialect: Any) -> _LiteralProcessor[bool]: ...
    def bind_processor(self, dialect: Any) -> _BindProcessor[bool]: ...
    def result_processor(
        self, dialect: Any, coltype: Any
    ) -> _ResultProcessor[bool]: ...

class _AbstractInterval(_LookupExpressionAdapter[_T], TypeEngine[_T]):  # type: ignore[misc]
    def coerce_compared_value(
        self, op: Any, value: Any
    ) -> TypeEngine[Any]: ...

# "comparator_factory" of "_LookupExpressionAdapter" and "TypeDecorator" are incompatible
class Interval(Emulated, _AbstractInterval[timedelta], TypeDecorator[timedelta]):  # type: ignore[misc]
    impl: Any = ...
    epoch: datetime = ...
    native: bool = ...
    second_precision: Optional[float] = ...
    day_precision: Optional[float] = ...
    def __init__(
        self,
        native: bool = ...,
        second_precision: Optional[float] = ...,
        day_precision: Optional[float] = ...,
    ) -> None: ...
    @property
    def python_type(self) -> Type[timedelta]: ...
    def adapt_to_emulated(self, impltype: Type[_T], **kw: Any) -> _T: ...
    def bind_processor(self, dialect: Any) -> _BindProcessor[timedelta]: ...
    def result_processor(
        self, dialect: Any, coltype: Any
    ) -> _ResultProcessor[timedelta]: ...

class JSON(
    Indexable[_JSONType],
    TypeEngine[_JSONType],
):
    __visit_name__: str = ...
    hashable: bool = ...
    NULL: Any = ...
    none_as_null: bool = ...
    should_evaluate_none: bool = ...
    def __init__(self, none_as_null: bool = ...) -> None: ...
    class JSONElementType(TypeEngine[Union[int, util.text_type]]):
        def string_bind_processor(
            self, dialect: Any
        ) -> Optional[_BindProcessor[util.text_type]]: ...
        def string_literal_processor(
            self, dialect: Any
        ) -> Optional[_LiteralProcessor[util.text_type]]: ...
        def bind_processor(
            self, dialect: Any
        ) -> _BindProcessor[Union[int, util.text_type]]: ...
        def literal_processor(
            self, dialect: Any
        ) -> _LiteralProcessor[Union[int, util.text_type]]: ...
    class JSONIndexType(JSONElementType): ...
    class JSONIntIndexType(JSONIndexType): ...
    class JSONStrIndexType(JSONIndexType): ...
    class JSONPathType(JSONElementType): ...
    class Comparator(
        Indexable.Comparator["JSON"], Concatenable.Comparator["JSON"]
    ):
        def as_boolean(self) -> Any: ...
        def as_string(self) -> Any: ...
        def as_integer(self) -> Any: ...
        def as_float(self) -> Any: ...
        def as_numeric(
            self, precision: Any, scale: Any, asdecimal: bool = ...
        ) -> Any: ...
        def as_json(self) -> Any: ...
    comparator_factory: Type[Comparator] = ...  # type: ignore[assignment]
    @property
    def python_type(self) -> Type[Dict[Any, Any]]: ...
    def bind_processor(self, dialect: Any) -> _BindProcessor[_JSONType]: ...
    def result_processor(
        self, dialect: Any, coltype: Any
    ) -> _ResultProcessor[_JSONType]: ...

class ARRAY(
    SchemaEventTarget,
    Indexable[List[_TE]],
    Concatenable[List[_TE]],
    TypeEngine[List[_TE]],
):
    __visit_name__: str = ...
    class Comparator(
        Indexable.Comparator["ARRAY[_TE]"],
        Concatenable.Comparator["ARRAY[_TE]"],
    ):
        def contains(self, *arg: Any, **kw: Any) -> None: ...  # type: ignore[override]
        def any(
            self, other: Any, operator: Optional[Any] = ...
        ) -> BinaryExpression[Any]: ...
        def all(
            self, other: Any, operator: Optional[Any] = ...
        ) -> BinaryExpression[Any]: ...
    comparator_factory: Type[Comparator[_TE]] = ...  # type: ignore[assignment]
    item_type: _TE = ...
    as_tuple: bool = ...
    dimensions: Optional[int] = ...
    zero_indexes: bool = ...
    def __init__(
        self,
        item_type: Union[_TE, Type[_TE]],
        as_tuple: bool = ...,
        dimensions: Optional[int] = ...,
        zero_indexes: bool = ...,
    ) -> None: ...
    @property
    def hashable(self) -> bool: ...  # type: ignore[override]
    @property
    def python_type(self) -> Type[List[Any]]: ...
    def compare_values(self, x: Any, y: Any) -> bool: ...

class TupleType(TypeEngine[_TE]):
    types: Tuple[_TE, ...] = ...
    def __init__(self, *types: _TE) -> None: ...

class REAL(Float):
    __visit_name__: str = ...

class FLOAT(Float):
    __visit_name__: str = ...

class NUMERIC(Numeric):
    __visit_name__: str = ...

class DECIMAL(Numeric):
    __visit_name__: str = ...

class INTEGER(Integer):
    __visit_name__: str = ...

INT = INTEGER

class SMALLINT(SmallInteger):
    __visit_name__: str = ...

class BIGINT(BigInteger):
    __visit_name__: str = ...

class TIMESTAMP(DateTime):
    __visit_name__: str = ...
    def __init__(self, timezone: bool = ...) -> None: ...
    def get_dbapi_type(self, dbapi: Any) -> Any: ...

class DATETIME(DateTime):
    __visit_name__: str = ...

class DATE(Date):
    __visit_name__: str = ...

class TIME(Time):
    __visit_name__: str = ...

class TEXT(Text):
    __visit_name__: str = ...

class CLOB(Text):
    __visit_name__: str = ...

class VARCHAR(String):
    __visit_name__: str = ...

class NVARCHAR(Unicode):
    __visit_name__: str = ...

class CHAR(String):
    __visit_name__: str = ...

class NCHAR(Unicode):
    __visit_name__: str = ...

class BLOB(LargeBinary):
    __visit_name__: str = ...

class BINARY(_Binary):
    __visit_name__: str = ...

class VARBINARY(_Binary):
    __visit_name__: str = ...

class BOOLEAN(Boolean):
    __visit_name__: str = ...

class NullType(TypeEngine[None]):
    __visit_name__: str = ...
    hashable: bool = ...
    def literal_processor(self, dialect: Any) -> _LiteralProcessor[None]: ...
    class Comparator(TypeEngine.Comparator["NullType"]): ...
    comparator_factory: Type[Comparator] = ...  # type: ignore[assignment]

class TableValueType(HasCacheKey, TypeEngine[Any]):
    def __init__(self, *elements: Any) -> None: ...

class MatchType(Boolean): ...

NULLTYPE: NullType
BOOLEANTYPE: Boolean
STRINGTYPE: String
INTEGERTYPE: Integer
MATCHTYPE: MatchType
TABLEVALUE: TableValueType
