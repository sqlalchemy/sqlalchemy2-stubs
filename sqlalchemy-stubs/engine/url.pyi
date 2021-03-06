from typing import Any
from typing import Dict
from typing import List
from typing import Mapping
from typing import NamedTuple
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from .interfaces import Dialect
from .. import util

_TURL = TypeVar("_TURL", bound=URL)

class URL(NamedTuple):
    drivername: str = ...
    username: Optional[str] = ...
    password: Optional[Union[str, object]] = ...
    host: Optional[str] = ...
    port: Optional[int] = ...
    database: Optional[str] = ...
    query: Mapping[str, Union[str, Sequence[str]]] = ...
    def __new__(self: Type[_TURL], *arg: Any, **kw: Any) -> _TURL: ...  # type: ignore[misc]
    @classmethod
    def create(
        cls: Type[_TURL],
        drivername: str,
        username: Optional[str] = ...,
        password: Optional[Union[str, object]] = ...,
        host: Optional[str] = ...,
        port: Optional[int] = ...,
        database: Optional[str] = ...,
        query: Mapping[str, Union[str, Sequence[str]]] = ...,
    ) -> _TURL: ...
    def set(
        self: _TURL,
        drivername: Optional[str] = ...,
        username: Optional[str] = ...,
        password: Optional[Union[str, object]] = ...,
        host: Optional[str] = ...,
        port: Optional[int] = ...,
        database: Optional[str] = ...,
        query: Optional[Mapping[str, Union[str, Sequence[str]]]] = ...,
    ) -> _TURL: ...
    def update_query_string(
        self: _TURL, query_string: str, append: bool = ...
    ) -> _TURL: ...
    def update_query_pairs(
        self: _TURL,
        key_value_pairs: Sequence[Tuple[str, str]],
        append: bool = ...,
    ) -> _TURL: ...
    def update_query_dict(
        self: _TURL,
        query_parameters: Mapping[str, Union[str, Sequence[str]]],
        append: bool = ...,
    ) -> _TURL: ...
    def difference_update_query(
        self: _TURL, names: Sequence[str]
    ) -> _TURL: ...
    @util.memoized_property
    def normalized_query(self) -> util.immutabledict[str, Any]: ...
    def __to_string__(self, hide_password: bool = ...) -> str: ...
    def render_as_string(self, hide_password: bool = ...) -> str: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def get_backend_name(self) -> str: ...
    def get_driver_name(self) -> str: ...
    def get_dialect(self) -> Type[Dialect]: ...
    def translate_connect_args(
        self, names: List[str] = ..., **kw: Any
    ) -> Dict[str, Any]: ...

def make_url(name_or_url: Union[str, URL]) -> URL: ...
