from builtins import _NotImplementedType
import sys
from types import MethodType
from typing import Any
from typing import Callable
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Set
from typing import Tuple
from typing import TypeVar
from typing import Union

from _typeshed import SupportsKeysAndGetItem
from typing_extensions import Protocol

from .compat import _SortKeyFunction
from .compat import collections_abc as collections_abc
from .compat import threading

_I = TypeVar("_I", bound=immutabledict[Any, Any])
_PS = TypeVar("_PS", bound=Properties[str, Any])
_OD = TypeVar("_OD", bound=OrderedDict[Any, Any])
_OS = TypeVar("_OS", bound=OrderedSet[Any])
_IS = TypeVar("_IS", bound=IdentitySet[Any])
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_NKT = TypeVar("_NKT")
_NVT = TypeVar("_NVT")
_T = TypeVar("_T")
_U = TypeVar("_U")

if sys.version_info >= (3, 0):
    _B = TypeVar("_B", bound=Union[str, bytes])
else:
    _B = TypeVar("_B", bound=Union[basestring, bytes])  # noqa: F821

EMPTY_SET: frozenset[None]

class ImmutableContainer:
    def __delitem__(self, key: Any) -> NoReturn: ...
    def __setitem__(self, key: Any, value: Any) -> NoReturn: ...
    def __setattr__(self, key: Any, value: Any) -> NoReturn: ...

class immutabledict(ImmutableContainer, Dict[_KT, _VT]):
    def clear(self) -> NoReturn: ...
    def pop(self, key: Any, default: Any = ...) -> NoReturn: ...
    def popitem(self) -> NoReturn: ...
    def setdefault(self, key: Any, default: Any = ...) -> NoReturn: ...
    def update(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def __reduce__(self) -> Tuple[Any, ...]: ...
    @overload
    def union(self: _I) -> _I: ...
    @overload
    def union(
        self, __d: Mapping[_NKT, _NVT]
    ) -> immutabledict[Union[_KT, _NKT], Union[_VT, _NVT]]: ...
    @overload
    def union(
        self, __d: Iterable[Tuple[_NKT, _NVT]]
    ) -> immutabledict[Union[_KT, _NKT], Union[_VT, _NVT]]: ...
    @overload
    def merge_with(self: _I) -> _I: ...
    @overload
    def merge_with(
        self, *dicts: Dict[_NKT, _NVT]
    ) -> immutabledict[Union[_KT, _NKT], Union[_VT, _NVT]]: ...

@overload
def coerce_to_immutabledict(d: None) -> immutabledict[Any, Any]: ...
@overload
def coerce_to_immutabledict(d: _I) -> _I: ...
@overload
def coerce_to_immutabledict(
    d: SupportsKeysAndGetItem[_KT, _VT]
) -> immutabledict[_KT, _VT]: ...
@overload
def coerce_to_immutabledict(
    d: Iterable[Tuple[_KT, _VT]]
) -> immutabledict[_KT, _VT]: ...

EMPTY_DICT: immutabledict[Any, Any]

class FacadeDict(ImmutableContainer, Dict[_KT, _VT]):
    def clear(self) -> NoReturn: ...
    def pop(self, key: Any, default: Any = ...) -> NoReturn: ...
    def popitem(self) -> NoReturn: ...
    def setdefault(self, key: Any, default: Any = ...) -> NoReturn: ...
    def update(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def copy(self) -> NoReturn: ...
    def __reduce__(self) -> Tuple[Any, ...]: ...

class Properties(Generic[_KT, _VT]):
    def __init__(self, data: Dict[_VT, _KT]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_VT]: ...
    def __dir__(self) -> Iterable[str]: ...
    def __add__(self, other: Any) -> List[str]: ...
    def __setitem__(self, k: _KT, v: _VT) -> None: ...
    def __getitem__(self, k: _KT) -> _VT: ...
    def __delitem__(self, v: _KT) -> None: ...
    def __setattr__(self: _PS, key: str, obj: Any) -> None: ...
    def __getattr__(self: _PS, key: str) -> _VT: ...
    def __contains__(self, key: Any) -> bool: ...
    def as_immutable(self) -> ImmutableProperties[_KT, _VT]: ...
    @overload
    def update(self, value: Mapping[_KT, _VT]) -> None: ...
    @overload
    def update(self, value: Iterable[Tuple[_KT, _VT]]) -> None: ...
    @overload
    def get(self, key: _KT) -> Optional[_VT]: ...
    @overload
    def get(self, key: _KT, default: Union[_VT, _T]) -> Union[_VT, _T]: ...
    def keys(self) -> List[_KT]: ...
    def values(self) -> List[_VT]: ...
    def items(self) -> List[Tuple[_KT, _VT]]: ...
    def has_key(self, key: _KT) -> bool: ...
    def clear(self) -> None: ...

class OrderedProperties(Properties[_KT, _VT]):
    def __init__(self) -> None: ...

class ImmutableProperties(ImmutableContainer, Properties[_KT, _VT]): ...

def sort_dictionary(
    d: OrderedDict[Any, Any], key: Optional[_SortKeyFunction] = ...
) -> None: ...

if sys.version_info >= (3, 7):
    # This is required because dict is not subscriptable before 3.9
    class OrderedDict(Dict[_KT, _VT]): ...

else:
    class OrderedDict(Dict[_KT, _VT]):
        def __reduce__(self) -> Tuple[Any, ...]: ...
        @overload
        def __init__(self, **kwargs: _VT) -> None: ...
        @overload
        def __init__(
            self, ____sequence: Mapping[_KT, _VT] = ..., **kwargs: Any
        ) -> None: ...
        @overload
        def __init__(
            self, ____sequence: Iterable[Tuple[_KT, _VT]] = ..., **kwargs: Any
        ) -> None: ...
        def clear(self) -> None: ...
        def copy(self: _OD) -> _OD: ...
        def __copy__(self: _OD) -> _OD: ...
        @overload
        def update(
            self, ____sequence: Mapping[_KT, _VT], **kwargs: _VT
        ) -> None: ...
        @overload
        def update(
            self, ____sequence: Iterable[Tuple[_KT, _VT]], **kwargs: _VT
        ) -> None: ...
        @overload
        def update(self, **kwargs: _VT) -> None: ...
        def setdefault(self, key: _KT, value: _VT = ...) -> _VT: ...
        def __iter__(self) -> Iterator[_KT]: ...
        def keys(self) -> List[_KT]: ...  # type: ignore[override]
        def values(self) -> List[_VT]: ...  # type: ignore[override]
        def items(self) -> List[Tuple[_KT, _VT]]: ...  # type: ignore[override]
        if sys.version_info < (3, 0):
            def itervalues(self) -> Iterator[_VT]: ...
            def iterkeys(self) -> Iterator[_KT]: ...
            def iteritems(self) -> Iterator[Tuple[_KT, _VT]]: ...
        def __setitem__(self, key: _KT, obj: _VT) -> None: ...
        def __delitem__(self, key: _KT) -> None: ...
        @overload
        def pop(self, key: _KT) -> _VT: ...
        @overload
        def pop(
            self, key: _KT, default: Union[_VT, _T] = ...
        ) -> Union[_VT, _T]: ...
        def popitem(self) -> Tuple[_KT, _VT]: ...

class OrderedSet(Set[_T]):
    def __init__(self, d: Optional[Iterable[_T]] = ...) -> None: ...
    def add(self, element: _T) -> None: ...
    def remove(self, element: _T) -> None: ...
    def insert(self, pos: int, element: _T) -> None: ...
    def discard(self, element: _T) -> None: ...
    def clear(self) -> None: ...
    @overload
    def __getitem__(self, key: int) -> _T: ...
    @overload
    def __getitem__(self, s: slice) -> List[_T]: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __add__(self: _OS, other: Iterable[_T]) -> _OS: ...
    def update(self: _OS, iterable: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def __ior__(self: _OS, iterable: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def union(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def __or__(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def intersection(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def __and__(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def symmetric_difference(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def __xor__(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def difference(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def __sub__(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def intersection_update(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def __iand__(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def symmetric_difference_update(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def __ixor__(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def difference_update(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]
    def __isub__(self: _OS, other: Iterable[_T]) -> _OS: ...  # type: ignore[override]

class IdentitySet(Generic[_T]):
    def __init__(self, iterable: Optional[Iterable[_T]] = ...) -> None: ...
    def add(self, value: _T) -> None: ...
    def __contains__(self, value: Any) -> bool: ...
    def remove(self, value: _T) -> None: ...
    def discard(self, value: _T) -> None: ...
    def pop(self) -> _T: ...
    def clear(self) -> None: ...
    def __cmp__(self, other: Any) -> NoReturn: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def issubset(self, iterable: Iterable[Any]) -> bool: ...
    def __le__(self, other: Any) -> Union[_NotImplementedType, bool]: ...
    def __lt__(self, other: Any) -> Union[_NotImplementedType, bool]: ...
    def issuperset(self, iterable: Iterable[Any]) -> bool: ...
    def __ge__(self, other: Any) -> Union[_NotImplementedType, bool]: ...
    def __gt__(self, other: Any) -> Union[_NotImplementedType, bool]: ...
    def union(self, iterable: Iterable[_U]) -> IdentitySet[Union[_T, _U]]: ...
    def __or__(
        self, other: Iterable[_U]
    ) -> Union[_NotImplementedType, IdentitySet[Union[_T, _U]]]: ...
    def update(self, iterable: Iterable[_T]) -> None: ...
    def __ior__(self: _IS, other: Iterable[_T]) -> Union[_NotImplementedType, _IS]: ...  # type: ignore[misc]
    def difference(self: _IS, iterable: Iterable[_T]) -> _IS: ...
    def __sub__(
        self: _IS, other: Iterable[_T]
    ) -> Union[_NotImplementedType, _IS]: ...
    def difference_update(self, iterable: Iterable[_T]) -> None: ...
    def __isub__(
        self: _IS, other: Iterable[_T]
    ) -> Union[_NotImplementedType, _IS]: ...
    def intersection(
        self, iterable: Iterable[_U]
    ) -> IdentitySet[Union[_T, _U]]: ...
    def __and__(
        self, iterable: Iterable[_U]
    ) -> Union[_NotImplementedType, IdentitySet[Union[_T, _U]]]: ...
    def intersection_update(self, iterable: Iterable[_T]) -> None: ...
    def __iand__(self: _IS, other: Iterable[_T]) -> Union[_NotImplementedType, _IS]: ...  # type: ignore[misc]
    def symmetric_difference(
        self, iterable: Iterable[_U]
    ) -> IdentitySet[Union[_T, _U]]: ...
    def __xor__(
        self, other: Iterable[_U]
    ) -> Union[_NotImplementedType, IdentitySet[Union[_T, _U]]]: ...
    def symmetric_difference_update(
        self: _IS, iterable: Iterable[_T]
    ) -> None: ...
    def __ixor__(self: _IS, other: Iterable[_T]) -> Union[_NotImplementedType, _IS]: ...  # type: ignore
    def copy(self: _IS) -> _IS: ...
    def __copy__(self: _IS) -> _IS: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __hash__(self) -> int: ...

class WeakSequence(Generic[_T]):
    def __init__(self, __elements: Iterable[_T] = ...) -> None: ...
    def append(self, item: _T) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __getitem__(self, index: int) -> _T: ...

class OrderedIdentitySet(IdentitySet[_T]):
    def __init__(self, iterable: Optional[Iterable[_T]] = ...) -> None: ...

class PopulateDict(Dict[_KT, _VT]):
    creator: Callable[[_KT], _VT] = ...
    def __init__(self, creator: Callable[[_KT], _VT]) -> None: ...
    def __missing__(self, key: _KT) -> _VT: ...

class WeakPopulateDict(Dict[_KT, _VT]):
    creator: Callable[[Any, _KT], _VT] = ...
    weakself: Any = ...
    def __init__(self, creator_method: MethodType) -> None: ...
    def __missing__(self, key: _KT) -> _VT: ...

# The following two are required because builtins are not subscriptable before 3.9
class column_set(Set[_T]): ...
class column_dict(Dict[_KT, _VT]): ...

ordered_column_set = OrderedSet

def unique_list(
    seq: Iterable[_T], hashfunc: Optional[Callable[[_T], int]] = ...
) -> List[_T]: ...

class _DataAppender(Protocol[_T]):
    def append(self, value: _T) -> None: ...
    def __iter__(self) -> Iterable[_T]: ...

class _DataAdder(Protocol[_T]):
    def add(self, value: _T) -> None: ...
    def __iter__(self) -> Iterable[_T]: ...

class UniqueAppender(Generic[_T]):
    data: Any = ...
    @overload
    def __init__(self, data: Any, via: str) -> None: ...
    @overload
    def __init__(
        self, data: Union[_DataAppender[_T], _DataAdder[_T]]
    ) -> None: ...
    def append(self, item: _T) -> None: ...
    def __iter__(self) -> Iterator[_T]: ...

def coerce_generator_arg(arg: Any) -> Any: ...
@overload
def to_list(x: None, default: _T = ...) -> _T: ...
@overload
def to_list(x: Any, default: Optional[List[Any]] = ...) -> List[Any]: ...
def has_intersection(set_: Set[Any], iterable: Iterable[Any]) -> bool: ...
def to_set(x: Any) -> Set[Any]: ...
def to_column_set(x: Any) -> Set[Any]: ...
def update_copy(
    d: Dict[_KT, _VT],
    _new: Optional[
        Union[Mapping[_NKT, _NVT], Iterable[Tuple[_NKT, _NVT]]]
    ] = ...,
    **kw: _VT,
) -> Dict[Union[_KT, _NKT], Union[_VT, _NVT]]: ...
def flatten_iterator(x: Iterable[Any]) -> Iterator[Any]: ...

class LRUCache(Dict[_KT, _VT]):
    capacity: int = ...
    threshold: float = ...
    size_alert: Callable[[LRUCache[_KT, _VT]], Any] = ...
    def __init__(
        self,
        capacity: int = ...,
        threshold: float = ...,
        size_alert: Optional[Callable[[LRUCache[_KT, _VT]], Any]] = ...,
    ) -> None: ...
    @overload
    def get(self, key: _KT) -> Optional[_VT]: ...
    @overload
    def get(self, key: _KT, default: _T) -> Union[_VT, _T]: ...
    def __getitem__(self, key: _KT) -> _VT: ...
    def values(self) -> List[_VT]: ...  # type: ignore[override]
    def setdefault(self, key: _KT, value: _VT) -> Union[_KT, _VT]: ...  # type: ignore[override]
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    @property
    def size_threshold(self) -> float: ...

class ScopedRegistry(Generic[_T]):
    createfunc: Callable[[], _T] = ...
    scopefunc: Callable[[], Any] = ...
    registry: Dict[Any, _T] = ...
    def __init__(
        self, createfunc: Callable[[], _T], scopefunc: Callable[[], Any]
    ) -> None: ...
    def __call__(self) -> _T: ...
    def has(self) -> bool: ...
    def set(self, obj: _T) -> None: ...
    def clear(self) -> None: ...

class ThreadLocalRegistry(ScopedRegistry[_T]):
    createfunc: Callable[[], _T] = ...
    registry: threading.local = ...  # type: ignore[assignment]
    def __init__(self, createfunc: Callable[[], _T]) -> None: ...
    def __call__(self) -> _T: ...
    def has(self) -> bool: ...
    def set(self, obj: _T) -> None: ...
    def clear(self) -> None: ...

def has_dupes(sequence: Iterable[Any], target: Any) -> bool: ...
