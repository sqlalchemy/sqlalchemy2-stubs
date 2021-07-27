from typing import Any
from typing import Generic
from typing import overload
from typing import Type
from typing import TypeVar

_T = TypeVar("_T")

class _TypeToInstance(Generic[_T]):
    @overload
    def __get__(self, instance: None, owner: Any) -> Type[_T]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> _T: ...
    @overload
    def __set__(self, instance: None, value: Type[_T]) -> None: ...
    @overload
    def __set__(self, instance: object, value: _T) -> None: ...
